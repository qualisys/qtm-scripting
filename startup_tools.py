"""
Startup for tools. Invoke the add_menu function for scripts found at the top level of the tools folder.
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

# if you create a new tools menu, add the import here then add the menu below
import tools.gap_fill
importlib.reload(tools.gap_fill)

import tools.filter
importlib.reload(tools.filter)

import tools.markerset
importlib.reload(tools.markerset)

import tools.refine_rigid_body
importlib.reload(tools.refine_rigid_body)

def add_menu():
    tools.gap_fill.add_menu()
    tools.filter.add_menu()
    tools.markerset.add_menu()
    tools.refine_rigid_body.add_menu()

if __name__ == '__main__':
    add_menu()