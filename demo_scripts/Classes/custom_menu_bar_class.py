import helpers.menu_tools
import helpers.printing

from helpers.menu_tools import add_command, add_menu_item, add_menu_item_toggleable, set_toggleable_command_hotkey
from helpers.selection import select_all_trajectories, select_labeled_trajectories, select_unlabeled_trajectories
from helpers.printing import force_print
import subprocess
import os
import sys
import qtm
import importlib

importlib.reload(helpers.menu_tools)
importlib.reload(helpers.selection)
importlib.reload(helpers.printing)

# constants
menu_name_basic = "Script Examples (Basic)"
menu_name_advanced = "Script Examples (Advanced)"


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   C L A S S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
class custom_menu_bar:
    # - - - - - - - - - - - - - - - - - - -
    # ////////   P R I V A T E   ////////
    # - - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def __init__(self):
        # constants
        self._root_help_command = "root_help_"
        # variables
        self._buttons_enabled = True
        self._menu_id = 0
        self._menu_index = None
        # Dummy command, used to reset hotkeys between menus
        qtm.gui.add_command("dummy_func")
        qtm.gui.set_command_execute_function("dummy_func", None)

    def _update_menu_index(self):
        if (self._menu_index is None):
            self._menu_index = qtm.gui.get_menu_item_count(0)
        else:
            self._menu_index = qtm.gui.get_menu_item_count(0)
            menu_items = qtm.gui.get_menu_items(0)
            for curr_menu_item_index in range(len(menu_items)):
                if menu_items[curr_menu_item_index]["submenu"] == self._menu_id:
                    self._menu_index = curr_menu_item_index
        return self._menu_index

    def _toggle_buttons(self):
        self._buttons_enabled = not self._buttons_enabled
        state_str = "ENABLED" if self._buttons_enabled else "DISABLED"
        print("\n" + f"Buttons in '{menu_name_basic}' have now been {state_str}.")

    @staticmethod
    def _print_string():
        print("\nClicking the 'String' button calls the '_print_string' function which prints this message.")

    @staticmethod
    def _print_structured_string():
        comment_msg = "Clicking the 'Structured String' button calls the '_print_structured_string' function which prints this message."
        suggestion_msg = "Use 'force_print' or 'try_print' from 'HelpFuncsInternal.printing' to create these structured messages."
        force_print("PRINT", comment_msg, suggestion_msg)

    @staticmethod
    def _print_all_menus_formatted():
        list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
        print_msg = ""
        for curr_menu in list_of_all_menus_as_dicts:
            print_msg += "\n"
            print_msg += curr_menu["text"].replace("&", "")
            print_msg += " (ID: " + str(curr_menu["submenu"]) + ")"
        print(print_msg)

    @staticmethod
    def _print_all_submenus_formatted():
        list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
        print_msg = ""
        for curr_menu in list_of_all_menus_as_dicts:
            temp_msg = ""
            for curr_item in qtm.gui.get_menu_items(curr_menu["submenu"]):
                if curr_item["submenu"] != 0:
                    temp_msg += "\n\t"
                    temp_msg += curr_item["text"].replace("&", "")
                    temp_msg += " (ID: " + str(curr_item["submenu"]) + ")"
            if temp_msg != "":
                print_msg += "\n"
                print_msg += curr_menu["text"].replace("&", "")
                print_msg += temp_msg
        print(print_msg)

    @staticmethod
    def _add_button_to_all_menus():
        menu_count = 0
        list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
        for curr_menu in list_of_all_menus_as_dicts:
            success = add_menu_item(curr_menu["submenu"], "NEW BUTTON", "new_button_command")
            if success:
                menu_count += 1
        print("\n" + "'NEW BUTTON' added to '" + str(menu_count) + "' menu(s).")

    def _delete_top_button(self):
        list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
        for curr_menu in list_of_all_menus_as_dicts:
            if curr_menu["submenu"] == self._menu_id:
                if qtm.gui.get_menu_item(curr_menu["submenu"], 0)["text"] == "" and qtm.gui.get_menu_item(curr_menu["submenu"], 0)["command"] == "":
                    print("\n" + "A menu divider / separator line was successfully removed.")
                else:
                    print("\n" + "The '" + qtm.gui.get_menu_item(curr_menu["submenu"], 0)["text"] + "' button was successfully removed.")
                qtm.gui.delete_menu_item(self._menu_id, 0)
                break

    def _delete_this_menu(self):
        list_of_all_menus_as_dicts = qtm.gui.get_menu_items()
        for i in range(len(list_of_all_menus_as_dicts)):
            if list_of_all_menus_as_dicts[i]["submenu"] == self._menu_id:
                qtm.gui.delete_menu_item(None, i)
                self._menu_id = 0
                self._buttons_enabled = True
                break

    def _add_commands_printing(self):
        lambda_print_msg = "\nClicking the 'String (Lambda)' button calls a created lambda which prints this message."
        add_command("print_lambda", lambda: (print(lambda_print_msg)), lambda: (self._buttons_enabled is True))
        add_command("print_structured_string", custom_menu_bar._print_structured_string, lambda: (self._buttons_enabled is True))
        add_command("print_string", custom_menu_bar._print_string, lambda: (self._buttons_enabled is True))

    def _add_commands_commands(self):
        lambda_print_msg = ("\n" + "To call an existing command you can (in a script or in the terminal):" + "\n"
                            f"{'-' * 69}" + "\n"
                            f"- Run 'qtm.gui.send_command(\"<COMMAND_NAME>\")'" + "\n"
                            f"- Add a clickable button by running 'add_menu_item(<MENU_ID>, \"<BUTTON_TEXT>\", \"<COMMAND_NAME>\")'" + "\n\n"
                            f"To see a list of all available commands you can either:" + "\n"
                            f"{'-' * 55}" + "\n"
                            f"- In the '{menu_name_basic}' menu, click the 'Get All Commands' button" + "\n"
                            f"- In a script or in the terminal, run 'qtm.gui.get_commands()'"
                            )
        add_command("commands_information", lambda: (print(lambda_print_msg)), lambda: (self._buttons_enabled is True))
        add_command("list_all_commands", lambda: (print("\n" + str(qtm.gui.get_commands()))), lambda: (self._buttons_enabled is True))
        add_command("list_custom_commands", lambda: (print("\n" + str(qtm.gui.get_commands("user")))), lambda: (self._buttons_enabled is True))

    def _add_commands_menus(self):
        lambda_print_msg = ("\n" + "To modify the submenus you can (in a script or in the terminal):" + "\n"
                            f"{'-' * 64}" + "\n"
                            f"- Run 'add_menu_item(<MENU_ID>, \"<BUTTON_TEXT>\", \"<COMMAND_NAME>\", <INDEX>)'" + "\n"
                            f"- Run 'qtm.gui.insert_menu_separator(<MENU_ID>, <INDEX>)'" + "\n"
                            f"- Run 'qtm.gui.insert_menu_submenu(<MENU_ID>, <\"<MENU_TEXT>\">, <INDEX>)'" + "\n"
                            f"- Run 'qtm.gui.delete_menu_item(<MENU_ID>, <INDEX>)" + "\n"
                            f"NOTE: If <MENU_ID> is 'None'(null), the main menu will be used. Also, if <INDEX> is 'None'(null), the item will be placed at the top." + "\n\n"
                            f"To see a list of all available menus:" + "\n"
                            f"{'-' * 37}" + "\n"
                            f"- In the '{menu_name_basic}' menu, click the 'List All Menus' button to get a formatted list" + "\n"
                            f"- Run 'qtm.gui.get_menu_items()' to get an unformatted list" + "\n\n"
                            f"To see a list of all available submenus:" + "\n"
                            f"{'-' * 40}" + "\n"
                            f"- In the '{menu_name_basic}' menu, click the 'List All Submenus' button to get a formatted list" + "\n"
                            f"- Run 'qtm.gui.get_menu_items(<MENU_ID>) to get an unformatted list"
                            )
        add_command("menus_information", lambda: (print(lambda_print_msg)), lambda: (self._buttons_enabled is True))
        add_command("list_all_menus", lambda: (custom_menu_bar._print_all_menus_formatted()), lambda: (self._buttons_enabled is True))
        add_command("list_all_submenus", lambda: (custom_menu_bar._print_all_submenus_formatted()), lambda: (self._buttons_enabled is True))
        add_command("new_button_command", lambda: (print("\n" + "HOW DID THIS BUTTON GET HERE!?")))
        add_command("add_button_to_all_menus", lambda: (custom_menu_bar._add_button_to_all_menus()), lambda: (self._buttons_enabled is True))
        add_command("delete_top_button", lambda: (self._delete_top_button()), lambda: (self._buttons_enabled is True))
        add_command("delete_this_menu", lambda: (self._delete_this_menu()), lambda: (self._buttons_enabled is True))

    @staticmethod
    def _add_commands_miscellaneous():
        add_command("select_all_trajectories", select_all_trajectories)
        add_command("select_labeled_trajectories", select_labeled_trajectories)
        add_command("select_unlabeled_trajectories", select_unlabeled_trajectories)

    @staticmethod
    def _add_command_clear_terminal():
        add_command("clear_terminal", qtm.gui.terminal.clear)

    def _add_commands_root_help(self):
        root_help_topics = custom_menu_bar._get_root_help_topics()
        for curr_root_topic in root_help_topics:
            add_command((self._root_help_command + curr_root_topic), lambda topic=curr_root_topic: (print("\n\n\n" + qtm.utilities.documentation.get_help_text(topic))))

    @staticmethod
    def set_hotkeys_basic():
        # NOTE: Use this helper function when setting hotkey for a 'toggleable' button
        set_toggleable_command_hotkey(True, False, False, "1", "toggle_3d_scene_basic")
        set_toggleable_command_hotkey(True, False, False, "2", "toggle_overlay_basic")
        # NOTE: Helper function 'set_command_hotkey' can be used for 'normal' buttons too
        qtm.gui.set_accelerator({"ctrl": False, "alt": False, "shift": True, "key": "r"}, "clear_terminal")

    @staticmethod
    def set_hotkeys_advanced():
        set_toggleable_command_hotkey(True, False, False, "1", "toggle_3d_scene_advanced")
        set_toggleable_command_hotkey(True, False, False, "2", "toggle_overlay_advanced")
        set_toggleable_command_hotkey(True, False, False, "3", "toggle_drawing_arrows_unlabeled_traj")
        set_toggleable_command_hotkey(True, False, False, "4", "toggle_drawing_decaying_arrows_unlabeled_traj")
        qtm.gui.set_accelerator({"ctrl": False, "alt": False, "shift": True, "key": "r"}, "clear_terminal")
    
    @staticmethod
    def _reset_hotkeys():
        qtm.gui.set_accelerator({"ctrl": True, "alt": False, "shift": False, "key": "1"}, "dummy_func")
        qtm.gui.set_accelerator({"ctrl": True, "alt": False, "shift": False, "key": "2"}, "dummy_func")
        qtm.gui.set_accelerator({"ctrl": True, "alt": False, "shift": False, "key": "3"}, "dummy_func")
        qtm.gui.set_accelerator({"ctrl": True, "alt": False, "shift": False, "key": "4"}, "dummy_func")

    @staticmethod
    def _add_commands_and_buttons_open_files_folders(open_folders_menu_id, open_scripts_menu_id):
        target_dir = "qtm-scripting"
        project_dir = next((path for path in sys.path if target_dir in path), None)

        if project_dir:
            for folder_path, directories, files in os.walk(project_dir, topdown=True):
                # Skip unwanted folders
                directories[:] = [d for d in directories if d not in ["__pycache__", "Tests", ".git"]]
                base_folder_name = os.path.basename(folder_path)

                add_command("open_folder_" + base_folder_name, lambda local_var=folder_path: subprocess.Popen("explorer \"" + local_var + "\""))
                add_menu_item(open_folders_menu_id, base_folder_name, "open_folder_" + base_folder_name)

                for curr_file in files:
                    file_name, file_extension = os.path.splitext(curr_file)
                    # Skip unwanted files
                    if file_extension == ".py" and curr_file != "__init__.py":
                        file_path = os.path.join(folder_path, curr_file)
                        add_command("open_script_" + curr_file, lambda local_var=file_path: subprocess.Popen(["notepad.exe", local_var], shell=True))
                        add_menu_item(open_scripts_menu_id, curr_file, "open_script_" + curr_file)

    @staticmethod
    def _parse_help_output(output):
        topics = []
        for line in output.splitlines():
            if '|' in line and 'Topic' not in line:
                topic = line.split('|')[1].strip()
                topic = topic.strip('"')  # Remove quotation marks from found 'topics' 
                topics.append(topic)
        return topics

    @staticmethod
    def _get_root_help_topics():
        help_output = qtm.utilities.documentation.get_help_text()
        return custom_menu_bar._parse_help_output(help_output)

    def _add_root_help_menu_items(self):
        sub_menu_index = qtm.gui.insert_menu_submenu(self._menu_id, "Help (Main Topics)")
        for curr_command in qtm.gui.get_commands():
            if self._root_help_command in curr_command:
                saved_command = curr_command
                button_text = curr_command[len(self._root_help_command):]
                button_text = button_text.capitalize()
                add_menu_item(sub_menu_index, button_text, saved_command)

    @staticmethod
    def _all_modules_help_create_commands_and_sub_menu_menu_items(sub_menu_id, module_names_arr, module_funcs_arr):
        for curr_module_name in module_names_arr:
            # Dynamically access the module using getattr, navigating through nested modules
            module_parts = curr_module_name.split('.')
            curr_module = qtm  # Start from the root module
            for part in module_parts[1:]:  # Skip the 'qtm' part
                try:
                    curr_module = getattr(curr_module, part)
                except AttributeError as e:
                    print(f"Error accessing part '{part}' of '{curr_module_name}': {e}")
                    continue  # Skip and continue
            try:
                curr_sub_menu_id = qtm.gui.insert_menu_submenu(sub_menu_id, curr_module_name)
            except Exception as e:
                print(f"Error inserting submenu for '{curr_module_name}': {e}")
                continue  # Skip to the next module if submenu insertion fails

            for curr_func_name in module_funcs_arr[curr_module_name]:
                try:
                    command_name = (curr_module_name + "_" + curr_func_name)
                    command_func = None
                    # If function name is 'help', it's the module-level 'help'...
                    if curr_func_name == "help":
                        # ... so we call 'help' without a parameter
                        command_func = lambda curr_module=curr_module: (print(str("\n\n\n" + curr_module.help())))
                    else: # Otherwise, pass the function name as a parameter
                        command_func = lambda curr_func_name=curr_func_name, curr_module=curr_module: print(str("\n\n\n" + curr_module.help(curr_func_name)))
                    add_command(command_name, command_func)
                    # Use the dynamically defined command function for the menu button
                    qtm.gui.insert_menu_button(curr_sub_menu_id, curr_func_name, command_name)
                except Exception as e:
                    print(f"Error inserting button for '{curr_func_name}' in '{curr_module_name}': {e}")

    def _add_all_modules_help_menu_items(self):
        module_names = []
        module_functions = {}  # Dictionary uses module names as keys

        try:
            module_count = qtm.utilities.documentation.get_module_count()
            for curr_module_index in range(module_count):
                curr_module_name = qtm.utilities.documentation.get_module_path(curr_module_index)
                curr_module_method_count = qtm.utilities.documentation.get_method_count(curr_module_index)
                module_names.append(curr_module_name)
                module_functions[curr_module_name] = []
                for curr_function_index in range(curr_module_method_count):
                    method_name = qtm.utilities.documentation.get_method_name(curr_module_index, curr_function_index)
                    module_functions[curr_module_name].append(method_name)
        except Exception as e:
            print(f"Error loading module documentation: {e}")
            return  # Exit the function if there's an error in loading documentation
        try:
            index = qtm.gui.insert_menu_submenu(self._menu_id, "Help (Modules)")
            custom_menu_bar._all_modules_help_create_commands_and_sub_menu_menu_items(index, module_names, module_functions)
        except Exception as e:
            print(f"Error setting up help menu: {e}")
    # endregion

    # - - - - - - - - - - - - - - - - - -
    # ////////   P U B L I C   ////////
    # - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def setup_menu_basic(self):
        self._menu_id = qtm.gui.insert_menu_submenu(None, menu_name_basic, self._menu_index)
        if (self._menu_index is None):
            self._menu_index = qtm.gui.get_menu_item_count(0)
        # Create the commands, which are callable by either running them directly or via a button
        # NOTE: Trying to create a command with the same name more than once will generate an error. The
        #       reason it works here is because we are calling 'add_command()' from 'HelpFuncsInternal.tools'.
        add_command("toggle_buttons", self._toggle_buttons)
        self._add_commands_printing()
        self._add_commands_commands()
        self._add_commands_menus()
        self._add_command_clear_terminal()
        self._add_commands_root_help()

        # Add Switch to Advanced Menu Button
        add_menu_item(self._menu_id, "Switch to " + menu_name_advanced, "toggle_menu_script_example")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        add_menu_item_toggleable(self._menu_id, "Enable 3D Scene (Basic)", "Disable 3D Scene (Basic)", "toggle_3d_scene_basic")
        add_menu_item_toggleable(self._menu_id, "Enable Overlay (Basic)", "Disable Overlay (Basic)", "toggle_overlay_basic")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add 'Commands' Buttons
        add_menu_item(self._menu_id, "Commands Information", "commands_information")  # No index : Placed at the very bottom
        add_menu_item(self._menu_id, "List All Commands", "list_all_commands")  # No index : Placed below...
        add_menu_item(self._menu_id, "List Custom Commands", "list_custom_commands")  # No index : Placed below...

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add 'Menus' Buttons
        add_menu_item(self._menu_id, "Menus Information", "menus_information")
        add_menu_item(self._menu_id, "List All Menus", "list_all_menus")
        add_menu_item(self._menu_id, "List All Submenus", "list_all_submenus")
        # Add 'Printing' Submenu
        printing_sub_menu_id = qtm.gui.insert_menu_submenu(self._menu_id, "Printing Submenu")
        # Add 'Printing' Buttons (into the 'Printing' submenu)
        add_menu_item(printing_sub_menu_id, "String (Lambda)", "print_lambda", 0) # Index 0 : Placed at top
        add_menu_item(printing_sub_menu_id, "String", "print_string", 0)  # Index 0 (again) : Placed above 'String (Lambda)'
        add_menu_item(printing_sub_menu_id, "Structured String", "print_structured_string", 1)  # Index 1 : Placed between first two

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add "Insert / Delete" Buttons
        add_menu_item(self._menu_id, "Insert Button Into ALL Menus", "add_button_to_all_menus")
        add_menu_item(self._menu_id, "Delete Top Button", "delete_top_button")
        add_menu_item(self._menu_id, "Delete This Menu", "delete_this_menu")
        # Add 'Enable / Disable Buttons' Button
        add_menu_item_toggleable(self._menu_id, "Disable Buttons", "Enable Buttons", "toggle_buttons")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add 'Clear Terminal' Button
        add_menu_item(self._menu_id, "Clear Terminal", "clear_terminal")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add Submenus, Commands, & Buttons for Opening Script Files / Folders
        self._add_commands_and_buttons_open_files_folders(qtm.gui.insert_menu_submenu(self._menu_id, "Open Folder"), qtm.gui.insert_menu_submenu(self._menu_id, "Open Script"))

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        # Add help-related GUI buttons
        self._add_root_help_menu_items()
        self._add_all_modules_help_menu_items() # NOTE: Also creates commands

        # Add hotkeys last to ensure all commands have been created
        self.set_hotkeys_basic()

    def setup_menu_advanced(self):
        self._menu_id = qtm.gui.insert_menu_submenu(None, menu_name_advanced, self._menu_index)
        if (self._menu_index is None):
            self._menu_index = qtm.gui.get_menu_item_count(0)
        # Create the commands
        # NOTE: Trying to create a command with the same name more than once will generate an error. The
        #       reason it works here is because we are calling 'add_command()' from 'HelpFuncsInternal.tools'.
        self._add_commands_printing()
        self._add_commands_commands()
        self._add_commands_menus()
        self._add_commands_miscellaneous()
        self._add_command_clear_terminal()
        self._add_commands_root_help()
        
        add_menu_item(self._menu_id, "Switch to " + menu_name_basic, "toggle_menu_script_example")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        add_menu_item_toggleable(self._menu_id, "Enable 3D Scene (Advanced)", "Disable 3D Scene (Advanced)", "toggle_3d_scene_advanced")
        add_menu_item_toggleable(self._menu_id, "Enable Overlay (Advanced)", "Disable Overlay (Advanced)", "toggle_overlay_advanced")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        add_menu_item(self._menu_id, "List All Commands", "list_all_commands")  # No index : Placed below...
        add_menu_item(self._menu_id, "List Custom Commands", "list_custom_commands")  # No index : Placed below...

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        add_menu_item(self._menu_id, "List All Menus", "list_all_menus")
        add_menu_item(self._menu_id, "List All Submenus", "list_all_submenus")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        miscellaneous_commands_sub_menu_id = qtm.gui.insert_menu_submenu(self._menu_id, "Miscellaneous Commands")
        add_menu_item(miscellaneous_commands_sub_menu_id, "Select All Trajectories", "select_all_trajectories")
        add_menu_item(miscellaneous_commands_sub_menu_id, "Select Labeled Trajectories", "select_labeled_trajectories")
        add_menu_item(miscellaneous_commands_sub_menu_id, "Select Unlabeled Trajectories", "select_unlabeled_trajectories")
        add_menu_item_toggleable(miscellaneous_commands_sub_menu_id, "Identify Unlabeled Trajectories", "Stop Identifying Unlabeled Trajectories", "toggle_drawing_arrows_unlabeled_traj")
        add_menu_item_toggleable(miscellaneous_commands_sub_menu_id, "Identify Unlabeled Trajectories (With Decay)", "Stop Identifying Unlabeled Trajectories (With Decay)", "toggle_drawing_decaying_arrows_unlabeled_traj")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        add_menu_item(self._menu_id, "Clear Terminal", "clear_terminal")

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        self._add_commands_and_buttons_open_files_folders(qtm.gui.insert_menu_submenu(self._menu_id, "Open Folder"), qtm.gui.insert_menu_submenu(self._menu_id, "Open Script"))

        qtm.gui.insert_menu_separator(self._menu_id)  # - - - - - - - - - - - - - - - - - - - - - - - -

        self._add_root_help_menu_items()
        self._add_all_modules_help_menu_items()

        self.set_hotkeys_advanced()

    def delete_menu(self):
        self._update_menu_index()
        self._delete_this_menu()
        self._reset_hotkeys()
    # endregion
