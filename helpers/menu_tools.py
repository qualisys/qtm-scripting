import sys
import os
import inspect
this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)
    
from vector import Vec3
import printing as printing
import qtm

# variables
# WARNING: Adding variables here is potentially dangerous; variables are reset each time a script loads this module


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _look_for_duplicate_button_texts_and_print_warning(menu_id, list_of_menu_items_as_dicts, button_text_state_one, button_text_state_two):
    for menu_item_as_dict in list_of_menu_items_as_dicts:
        found_text = ""
        if menu_item_as_dict["text"] == button_text_state_one:
            found_text = button_text_state_one
        elif menu_item_as_dict["text"] == button_text_state_two:
            found_text = button_text_state_two
        if found_text != "":
            comment_str = "Duplicate button text '" + found_text + "' found in menu '" + str(menu_id) + "'(ID)."
            comment_suggestion = "For toggleable buttons to work properly, all buttons in that menu/submenu must have unique names."
            printing.force_print("WARNING", comment_str, comment_suggestion, only_filename=True)
            break


def _find_menu_button_in_submenus_and_toggle_it(menu_id, button_text_state_one, button_text_state_two, toggle_command):
    child_submenu_ids = []
    list_of_all_menu_items_as_dicts = qtm.gui.get_menu_items(menu_id)
    menu_button_found = False
    # Loop through all items
    for i in range(len(list_of_all_menu_items_as_dicts)):
        # Check if item is a submenu child
        if list_of_all_menu_items_as_dicts[i]["submenu"] != 0:
            child_submenu_ids.append(list_of_all_menu_items_as_dicts[i]["submenu"])
        else:
            if list_of_all_menu_items_as_dicts[i]["text"] == button_text_state_one:
                # Successful match with 'button_text_state_one' text
                qtm.gui.delete_menu_item(menu_id, i)
                add_menu_item(menu_id, button_text_state_two, toggle_command, i)
                menu_button_found = True
                _look_for_duplicate_button_texts_and_print_warning(menu_id, list_of_all_menu_items_as_dicts[i+1:], button_text_state_two, button_text_state_one)
                break
            elif list_of_all_menu_items_as_dicts[i]["text"] == button_text_state_two:
                # Successful match with 'button_text_state_two' text
                qtm.gui.delete_menu_item(menu_id, i)
                add_menu_item(menu_id, button_text_state_one, toggle_command, i)
                menu_button_found = True
                _look_for_duplicate_button_texts_and_print_warning(menu_id, list_of_all_menu_items_as_dicts[i+1:], button_text_state_two, button_text_state_one)
                break
    if menu_button_found is False:
        # No matches found ==> Recursive search (one for each additional child submenu)
        for id in child_submenu_ids:
            menu_button_found = _find_menu_button_in_submenus_and_toggle_it(id, button_text_state_one, button_text_state_two, toggle_command)
            if menu_button_found is True:
                # A match was found ==> break recursion
                break
    return menu_button_found


def _toggle_menu_button(menu_id, button_text_state_one, button_text_state_two, toggle_command, action_command):
    list_of_all_menu_items_as_dicts = qtm.gui.get_menu_items(menu_id)
    menu_button_found = False
    # Search through the 'top-layer' of menu items
    for i in range(len(list_of_all_menu_items_as_dicts)):
        if list_of_all_menu_items_as_dicts[i]["text"] == button_text_state_one:
            # Successful match with 'button_text_state_one' text
            qtm.gui.delete_menu_item(menu_id, i)
            add_menu_item(menu_id, button_text_state_two, toggle_command, i)
            menu_button_found = True
            _look_for_duplicate_button_texts_and_print_warning(menu_id, list_of_all_menu_items_as_dicts[i+1:], button_text_state_one, button_text_state_one)
            break
        elif list_of_all_menu_items_as_dicts[i]["text"] == button_text_state_two:
            # Successful match with 'button_text_state_two' text
            qtm.gui.delete_menu_item(menu_id, i)
            add_menu_item(menu_id, button_text_state_one, toggle_command, i)
            menu_button_found = True
            _look_for_duplicate_button_texts_and_print_warning(menu_id, list_of_all_menu_items_as_dicts[i+1:], button_text_state_two, button_text_state_one)
            break
    if menu_button_found is False:
        # No matches found ==> Begin recursive search through this menu's submenus
        menu_button_found = _find_menu_button_in_submenus_and_toggle_it(menu_id, button_text_state_one, button_text_state_two, toggle_command)
    if menu_button_found is False:
        comment_str = "Toggle button '" + button_text_state_one + " / " + button_text_state_two + "' was not found."
        suggestion_str = "This might be due to the button's original text not matching the text expected by '_toggle_menu_button'."
        printing.force_print("WARNING", comment_str, suggestion_str, only_filename=True)
    # Call the ACTUAL command (irregardless if button-text toggling worked correctly)
    qtm.gui.send_command(action_command)
#endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E X P O R T E D   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def clamp(value, lower, upper):
    return min(max(lower, value), upper)


def calculate_acceleration(p1, p2, p3, dt):
    return (Vec3(p3) - (Vec3(p2) * 2) + Vec3(p1)) / (dt * dt)


def set_command_hotkey(ctrl_modifier, alt_modifier, shift_modifier, key, command_name):
    qtm.gui.set_accelerator({"ctrl": ctrl_modifier, "alt": alt_modifier, "shift": shift_modifier, "key": key}, command_name)


def set_toggleable_command_hotkey(ctrl_modifier, alt_modifier, shift_modifier, key, command_name):
    set_command_hotkey(ctrl_modifier, alt_modifier, shift_modifier, key, str(command_name + "_internal"))


def add_command(name, execute_func, update_func=None):
    if name in qtm.gui.get_commands():
        return False  # E A R L Y   E X I T
    qtm.gui.add_command(name)
    qtm.gui.set_command_execute_function(name, execute_func)
    if update_func is not None:
        qtm.gui.set_command_update_function(name, update_func)
    return True


def add_menu_item(menu_id, button_text, command_name, index=None):
    # Get menu name
    list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
    menu_name = ""
    for curr_menu in list_of_all_menus_as_dicts:
        if curr_menu["submenu"] == menu_id:
            menu_name = curr_menu["text"].replace("&", "")
    # Check for duplicate button-text in submenu
    list_of_all_menu_items_as_dicts = qtm.gui.get_menu_items(menu_id)
    for curr_item in list_of_all_menu_items_as_dicts:
        if curr_item["text"] == button_text:
            comment_str = str("Tried to add item to menu '" + menu_name + "' (ID: " + str(menu_id) + ") using existing button text '" + button_text + "'.")
            suggestion_str = "For toggleable buttons to work, all button texts (in a specific menu / submenu) must be unique."
            printing.force_print("ERROR", comment_str, suggestion_str)
            return False  # E A R L Y   E X I T
    qtm.gui.insert_menu_button(menu_id, button_text, command_name, index)
    return True


def add_menu_item_toggleable(menu_id, button_text_state_one, button_text_state_two, command_name, index=None):
    # Generate command-name that toggles the button (also calls the ACTUAL command)
    toggle_command_name = str(command_name + "_internal")
    if toggle_command_name not in globals()["_toggle_button_menu_ids"]:
        # This is the first time creating this toggle, so we add the command
        add_command(toggle_command_name, lambda: (_toggle_menu_button(globals()["_toggle_button_menu_ids"][toggle_command_name], button_text_state_one, button_text_state_two, toggle_command_name, command_name)))
    # Update (or add, if first time) 'toggle_command_name' & menu ID key-value pair
    globals()["_toggle_button_menu_ids"][toggle_command_name] = menu_id
    add_menu_item(globals()["_toggle_button_menu_ids"][toggle_command_name], button_text_state_one, toggle_command_name, index)
# endregion
