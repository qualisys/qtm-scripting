# QTM Scripting
Crash Course Video: https://youtu.be/m0Ff6Jkdf-U
Scripting examples and tools for QTM.  Lua and Python are supported in the QTM Scripting Interface.  But for now these examples are all in Python.
## Installation
1. Download the repo to your machine.
2. In QTM Project Options->Miscellaneous->Scripting:
    - Set Language to Python (this only affects which terminal is shown)
    - Add the Python file "startup_demo_scripts.py"
    - Add the Python file "startup_tools.py"
    - Select the checkbox next to the scripts you wish to have add menus, you can have either one or both at the same time.

## What is in this repository
This repository contains example scripts and useful script based tools for QTM.
1. Demo Scripts contains example scripts demonstrating various capabilities of the scripting engine.
2. Tools contains various helpful tools for use in QTM
    - *GapFill* has a selection of gap trimming and filling tools using stored relational information based on marker names from the standard Animation markerset
    - *Filter* has spike reporting and removal/smoothing tools
    - *Markerset* has miscellaneous tools for reporting, modifying and selecting markersets.
    - *Refine rigid body* can be used to adapt rigid body definitions to measured markers.
    - *Gap fill presets* can be used to define and use custom gap fill actions, including relational gap fill.
    - *Twin* contains an alternative twin calibration method using a rigid body (6DOF).
## Adding your own script menus
1. Follow the example of the scripts, such as "gap_fill.py" in the tools folder:
    - Have an exported function to create a menu, call it "add_menu()"
    - Have a module variable, an integer, called "menu_priority" and give it a value greater than 0 
    - The startup_tools.py script will find your file and function and invoke it upon startup.  You can create a "user" sub-folder and use it instead of the tools folder if you wish to keep your files separated.
## Installing modules such as numpy
1. Open a command prompt window (as administrator):
    - Go to the QTM installation folder, usually "C:\Program Files\Qualisys\Qualisys Track Manager"
    - Invoke the pip installer with a command like this, "python -m pip install numpy"
    
## Documentation
https://qualisys.github.io/qtm-scripting/

## External Links
1. [This Repository](https://github.com/qualisys/qtm-scripting.git)
2. [www.python.org](https://www.python.org/)




