"""
Example script created in the "Getting Started with Scripting in QTM: A Crash Course" video: https://youtu.be/m0Ff6Jkdf-U
To run this, open QTM and navigate to "Project Options" --> "Miscellaneous" --> "Scripting", click on "Add", and then add this script
"""
import sys
import os
import inspect
import importlib
# Set scripts 'path' to your repo location
# NOTE: This needs to be done before importing custom libraries
this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)
import qtm

from helpers.printing import try_print_except
from helpers.menu_tools import add_command, add_menu_item

#try:
     #import demo_scripts.custom_menu_bar as custom_menu_bar
#except ModuleNotFoundError as e:
     #try_print_except(str(e), "Press 'Reload scripts' to try again.")
# variables
_custom_button_command = "Custom Button Command"
_custom_function_command = "Custom Function Command"


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _reload_script_modules():
    print("do nothing")
    #importlib.reload(custom_menu_bar)

def _custom_command_execution():
    print("This is a custom function that is attached to a command which is attached to a button.")

def _setup_menu_commands():
    qtm.gui.add_command(_custom_button_command)
    qtm.gui.set_command_execute_function(_custom_button_command, lambda: (print("Custom button was pressed")))
    add_command(_custom_function_command, lambda: (_custom_command_execution()))

def _setup_menu():
    custom_menu_name = "Custom Menu"
    custom_sub_menu_name = "Custom Sub Menu"
    custom_button_name = "Custom Button"
    custom_button_two_name = "Top Button"
    custom_button_main_name = "Main Menu Button"
    menu_id = qtm.gui.insert_menu_submenu(None, custom_menu_name)
    sub_menu_id = qtm.gui.insert_menu_submenu(menu_id, custom_sub_menu_name)
    qtm.gui.insert_menu_button(sub_menu_id, custom_button_name, _custom_button_command)
    qtm.gui.insert_menu_button(sub_menu_id, custom_button_two_name, _custom_button_command, 0)
    qtm.gui.insert_menu_button(menu_id, custom_button_main_name, _custom_button_command)
    add_menu_item(menu_id, "Main Button Custom Function", _custom_function_command)
    qtm.gui.insert_menu_separator(menu_id)
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E N T R Y   P O I N T (local 'main')   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add_menu():
    try:
        _reload_script_modules()
        print("Modules loaded.")
        # Set callback for drawing in the OpenGL window
        #qtm.gui._3d.set_draw_function(_update_and_draw_callbacks)
        _setup_menu_commands()
        _setup_menu()
    except Exception as e:
        try_print_except(str(e), "Press 'Reload scripts' to try again.")

if __name__ == '__main__':
    add_menu()
