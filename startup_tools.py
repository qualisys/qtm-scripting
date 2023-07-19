"""
Startup for tool menus. Invoke the add_menu function for scripts found at the top level of the tools folder.
"""
import sys
import os
import inspect
import importlib

# Set scripts 'path' to your repo location
# NOTE: This needs to be done before importing custom libraries
this_file = inspect.getfile(inspect.currentframe())
this_dir = os.path.dirname(os.path.abspath(this_file))
if this_dir not in sys.path:
    sys.path.append(this_dir)

# NOTE ON ADDING NEW MENU FILES
#
# If you create a new tools menu file just copy it to the tools
# folder.  Make sure it has the module variable 'menu_priority' set 
# to something other than 0 (the larger the value the further
# to the right in the menus it will appear) AND have the add_menu() function which
# creates a QTM menu.  This script will automatically find your file and call the 
# function to make the menu.
#
# Menus with the same priority value will be added in alphabetical order (well, 
# the order in which listdir() returns the file names).
#
# Support for a "user" folder is included.  If a user wishes to keep their own
# custom menus separate from the tools folder then create a "user" folder and put
# the scripts in there.
#
def _add_subfolder(folder, verbose = False):
    try:
        filenames = os.listdir(os.path.join(this_dir,folder))
    except:
        if verbose:
            print(f"{this_file}: Unable to list sub-folder '{folder}', does it exist?")
        return
    menu_files = []
    for filename in filenames:
        if "__" not in filename[0]:
            modname = filename.split('.',1)[0]
            try:
                mod = importlib.import_module(modname)
                importlib.reload(mod)
            except ModuleNotFoundError as err:
                print(err)
                print(f"{this_file}: Could not load {filename} as a module, skipping...")
            except Exception as e:
                print(f"{this_file}: Exception: {str(e)} in {filename}, skipping...")   
            else:             
                if mod is not None:
                    d = dir(mod)
                    priority_level = 0
                    if 'menu_priority' in d:
                        priority_level = mod.menu_priority
                    if priority_level > 0:
                        if 'add_menu' in d:
                            menu_files.append({'mod': mod, 'modname': modname, 'priority_level': priority_level})
                else:
                    if verbose:
                        print(f"{this_file}: Unable to load {modname}")    
    menu_files.sort(key=lambda x: x['priority_level'])

    for menu_file in menu_files:
        menu_file['mod'].add_menu()
        print(f"Added {menu_file['modname']} menu.")
    
def add_menus():
    _add_subfolder("tools",True) 
    _add_subfolder("user") 

if __name__ == '__main__':
    add_menus()