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
import demo_scripts.tools.gap_fill
importlib.reload(demo_scripts.tools.gap_fill)

import demo_scripts.tools.filter
importlib.reload(demo_scripts.tools.filter)

import demo_scripts.tools.markerset
importlib.reload(demo_scripts.tools.markerset)

import demo_scripts.tools.refine_rigid_body
importlib.reload(demo_scripts.tools.refine_rigid_body)

import demo_scripts.tools.gap_fill_presets
importlib.reload(demo_scripts.tools.gap_fill_presets)

def add_menu():
    demo_scripts.tools.gap_fill.add_menu()
    demo_scripts.tools.filter.add_menu()
    demo_scripts.tools.markerset.add_menu()
    demo_scripts.tools.refine_rigid_body.add_menu()
    demo_scripts.tools.gap_fill_presets.add_menu()

if __name__ == '__main__':
    add_menu()