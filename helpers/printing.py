import sys
import inspect
import os
import datetime
import traceback

this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)

import menu_tools as tools


# constants
_error_print_periodicity = 2.0  # As seconds
_error_signatures_stack_size = 32
# variables
# WARNING: Adding variables here is potentially dangerous; variables are reset each time a script loads this module
_prev_error_signatures = [""] * _error_signatures_stack_size
_prev_error_index = 0
_prev_time = datetime.datetime.now()
_accumulated_dt = 0.0


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _try_print(signature, title, func_name, line_num, filename, comment, suggestion, call_stack):
    if _signatures_stack_has_signature(signature) is False:
        # New error ==> PRINT
        _insert_error_signature(signature)
        print(_create_print_message(title, func_name, line_num, filename, comment, suggestion, call_stack))
        # Reset time-variables here to avoid inconsistent printing
        globals()['_prev_time'] = datetime.datetime.now()
        globals()['_accumulated_dt'] = 0
    else:
        # Error already reported ==> adjust time-variables
        curr_time = datetime.datetime.now()
        dt = curr_time - globals()['_prev_time']
        globals()['_accumulated_dt'] += dt.total_seconds()
        globals()['_prev_time'] = curr_time
        # Timer has passed 'print periodicity' ==> PRINT
        if globals()['_accumulated_dt'] > globals()['_error_print_periodicity']:
            _insert_error_signature(signature)
            print(_create_print_message(title, func_name, line_num, filename, comment, suggestion, call_stack))
            # Reset accumulated time
            globals()['_accumulated_dt'] = 0


def _create_print_message(title, func_name, line_num, filename, comment, suggestion, call_stack):
    result = ""
    result += ("\n" + title[:7] + "\t|FUNCTION NAME: " + func_name)
    result += (" (line " + line_num + " in '" + filename + "')")
    if comment != "":
        result += "\n"
        result += "-" * len(title[:7])
        result += ("\t|COMMENT:" + "\t" + comment)
    if suggestion != "":
        result += ("\n\t|SUGGESTION: " + "\t" + suggestion)
    if call_stack != "":
        result += ("\n" + call_stack)
    return result


def _signatures_stack_has_signature(signature):
    if signature in globals()['_prev_error_signatures']:
        return True
    return False


def _insert_error_signature(signature):
    curr_error_index = globals()['_prev_error_index'] + 1
    if curr_error_index == globals()['_error_signatures_stack_size']:
        curr_error_index = 0
    globals()['_prev_error_signatures'][curr_error_index] = signature
    globals()['_prev_error_index'] = curr_error_index


def _traceback_list_to_array(traceback_list):
    return_array = [[0]*4 for i in range(len(traceback_list))]
    for i in range(len(traceback_list)):
        temp_string = traceback_list[i]
        # Filepath
        temp_string = temp_string.split("\"", 2)
        return_array[i][1] = temp_string[1]
        # Line number
        temp_string = temp_string[2].split("line ", 1)[1].split(",", 1)
        return_array[i][2] = temp_string[0]
        # Function name
        temp_string = temp_string[1].split("in ", 1)[1].split("\n", 1)
        return_array[i][3] = temp_string[0]
        # The actual line of code
        return_array[i][0] = temp_string[1].lstrip()
    return return_array


def _get_call_stack_as_str(call_stack_2d_array, prune_depth, reverse_order=False):
    prune_depth = tools.clamp(prune_depth, 0, len(call_stack_2d_array))
    return_str = "\tCALL STACK:"
    if (prune_depth == len(call_stack_2d_array)):
        return ""  # E A R L Y   E X I T
    else:
        total_depth = len(call_stack_2d_array)
        curr_depth = 0
        # Remove 'prune_depth' number of entries, bot -> top
        for i in range(total_depth - prune_depth):
            if reverse_order:
                index = total_depth-i-1
            else:
                index = i
            return_str += ("\n\t\t")
            if (i != 0):
                return_str += (" "*(curr_depth-1) + "\\" + " ")
            return_str += call_stack_2d_array[index][3]
            return_str += " (line "
            return_str += str(call_stack_2d_array[index][2])
            return_str += " in "
            return_str += os.path.basename(call_stack_2d_array[index][1])
            return_str += ")"
            curr_depth += 1
    return return_str


def _get_call_stack_exception_last_layer():
    return_array = [0]*4
    traceback_as_2d_array = _traceback_list_to_array(traceback.extract_tb(sys.exc_info()[2]).format())
    last_index = len(traceback_as_2d_array) - 1
    for i in range(4):
        return_array[i] = traceback_as_2d_array[last_index][i]
    return return_array


def _get_call_stack_exception(prune_depth=0):
    traceback_as_2d_array = _traceback_list_to_array(traceback.extract_tb(sys.exc_info()[2]).format())
    return _get_call_stack_as_str(traceback_as_2d_array, prune_depth)
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E X P O R T E D   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def get_this_method_name():
    return inspect.stack()[1][3]


def get_parent_method_name():
    try:
        inspect.stack()[2][3]
    except IndexError as e:
        try_print_except(str(e), "The parent method wasn't found. Perhaps the function calling this passed as a lambda?")
        return "Parent method not found!"
    return inspect.stack()[2][3]


def get_this_method_line_num():
    return inspect.stack()[1][2]


def get_parent_method_line_num():
    try:
        inspect.stack()[2][2]
    except IndexError as e:
        try_print_except(str(e), "The parent method wasn't found. Perhaps the function calling this was passed as a lambda?")
        return "Parent method not found!"
    return inspect.stack()[2][2]


def get_this_method_filename():
    return inspect.stack()[1][1]


def get_parent_method_filename():
    try:
        inspect.stack()[2][2]
    except IndexError as e:
        try_print_except(str(e), "The parent method wasn't found. Perhaps the function calling this was passed as a lambda?")
        return "Parent method not found!"
    return inspect.stack()[2][1]


def try_print_except(comment="", suggestion="", only_filename=False):
    # Append the exception type to the comment
    comment = str(sys.exc_info()[0]).split("'", 2)[1] + " - " + comment
    call_stack_bot_layer_info = _get_call_stack_exception_last_layer()
    func_name = call_stack_bot_layer_info[3]
    line_num = call_stack_bot_layer_info[2]
    if only_filename:
        filename = call_stack_bot_layer_info[1].rsplit("\\", 1)[1]
    else:
        filename = call_stack_bot_layer_info[1]
    call_stack = _get_call_stack_exception()
    signature = func_name + line_num
    _try_print(signature, "EXCEPT", func_name, line_num, filename, comment, suggestion, call_stack)


def force_print_except(comment="", suggestion="", only_filename=False):
    # Append the exception type to the comment
    comment = str(sys.exc_info()[0]).split("'", 2)[1] + " - " + comment
    call_stack_bot_layer_info = _get_call_stack_exception_last_layer()
    func_name = call_stack_bot_layer_info[3]
    line_num = call_stack_bot_layer_info[2]
    if only_filename:
        filename = call_stack_bot_layer_info[1].rsplit("\\", 1)[1]
    else:
        filename = call_stack_bot_layer_info[1]
    call_stack = _get_call_stack_exception()
    print(_create_print_message("EXCEPT", func_name, line_num, filename, comment, suggestion, call_stack))


def try_print(title_short="MSG", comment="", suggestion="", only_filename=False):
    func_name = get_parent_method_name()
    line_num = str(get_parent_method_line_num())
    if only_filename:
        filename = get_parent_method_filename().rsplit("\\", 1)[1]
    else:
        filename = get_parent_method_filename()
    signature = func_name + line_num
    _try_print(signature, title_short, func_name, line_num, filename, comment, suggestion, "")


def force_print(title_short, comment="", suggestion="", only_filename=False):
    func_name = get_parent_method_name()
    line_num = str(get_parent_method_line_num())
    if only_filename:
        filename = get_parent_method_filename().rsplit("\\", 1)[1]
    else:
        filename = get_parent_method_filename()
    print(_create_print_message(title_short, func_name, line_num, filename, comment, suggestion, ""))
# endregion
