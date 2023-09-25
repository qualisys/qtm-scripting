'''Tool template "Hello world".

Hello world script as a basic template for a tool script, consisting of:
* An execution function (print hello world)
* A QTM command associated with the execution function
* A menu button to call the command
* Add the menu_priority variable for automatic loading of multiple scripts
through startup_tools.py in order of priority
'''

# Make sure to import the QTM Scripting interface
import qtm

menu_priority = 10

# Execution function: print "Hello world!" to the terminal
def _echo_hello():
    print("Hello world!") # Use QTM Scripting Interface method for writing to terminal

# Function for defining the commands and set up the menu
def add_menu():
    # Add command for display of script doc string to the terminal
    help_command = "disp_hello_world_script_doc" # Use a unique command name for display of script help
    qtm.gui.add_command(help_command)
    qtm.gui.set_command_execute_function(help_command, lambda:(print(__doc__)))

    # Add QTM command and set _echo_hello as execute function
    qtm.gui.add_command("echo_hello")
    qtm.gui.set_command_execute_function("echo_hello", _echo_hello)

    # Add menu
    menu_id = qtm.gui.insert_menu_submenu(None, "Template")

    # Add Help button for display of the script doc string
    qtm.gui.insert_menu_button(menu_id, "Help", help_command)
    qtm.gui.insert_menu_separator(menu_id)

    # Add Hello world button
    qtm.gui.insert_menu_button(menu_id, "Hello world", "echo_hello")

# Call add_menu() function when running the script as stand-alone
if __name__ == "__main__":
    add_menu()
