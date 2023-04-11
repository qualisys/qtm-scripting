"""
Default startup for user examples.  Invoke the startup script
in demo_scripts.
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

import demo_scripts.startup
importlib.reload(demo_scripts.startup)


def add_menu():
    demo_scripts.startup.add_menu()

if __name__ == '__main__':
    add_menu()


