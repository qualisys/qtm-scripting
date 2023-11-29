"""gap_fill_presets.py: Script for applying gap filling according to specific definitions

When loading the script, a menu "Gap fill presets" is added to QTM with a submenu "Gap fill..." containing a list of
gap fill action buttons.

When pressing a gap fill action button, the action is applied to all the gaps of the target trajectory in the
current measurement.

This script is especially helpful for applying relational or virtual gap filling according to a predefined set
of relations.

The gap fill actions are compiled from a list of gap fill definitions specified by the global variable
`list_of_gap_fill_presets` in this script. The list can easily be customized by editing this script variable.

The list items in list_of_gap_fill_presets are formatted as a dictionary with the following key-value combinations:
  * display_name: Name of the definition appearing in the submenu
  * target: Name of the trajectory to be filled
  * method: gap fill method, corresponding to the `algorithm` variable in the QTM Scripting Interface `fill_trajectory` method
  * settings: settings definition for relational and virtual gap fill, which is a dictionary with key-value combinations:
    - origin: Name of trajectory to be used as origin in the gap fill relation (automatically converted to trajectory ID)
    - line: Name of trajectory defining the line in the gap fill relation (automatically converted to trajectory ID)
    - plane: Name of the trajectory defining the plane in the gap fill relation (automatically converted to trajectory ID)
    - offset: XYZ offset (vec3f, directly passed to the `fill_trajectory` method)
    - is_rigid_body (bool, directly passed to the `fill_trajectory` method)
    - is_relative_offset (bool, directly passed to the `fill_trajectory` method)
  
  For more information about settings, see the QTM Scripting Interface documentation for the `fill_trajectory` method.

Script valiables:
  * list_of_gap_fill_presets: predefined gap-fill actions. Initial example based on the Qualisys sports marker set for
    the skeleton solver.

Current limitations of the script:
  * The number of gap fill relations is limited to a maximum of 10 items. This can be expanded by adding new commands in
      this script under add_my_commands.

"""

#import importlib

import qtm

import qtm.data.object.trajectory as traj
import qtm.data.series._3d as data_3d
import qtm.gui.message as msg

import copy

# Edit the list of presets defining the gap fill actions (example based on Qualisys Sports markerset for the skeleton solver)
list_of_gap_fill_presets = [\
    {"display_name": "Q_WaistBack (polynomial)", "target": "Q_WaistBack", "method": "polynomial"},\
    {"display_name": "Q_WaistBack (kinematic)", "target": "Q_WaistBack", "method": "kinematic"},\
    {"display_name": "Q_WaistLFront (rel): WaistBack-WaistRFront-WaistL", "target": "Q_WaistLFront", "method": "relational", "settings": {"origin": "Q_WaistBack", "line": "Q_WaistRFront", "plane": "Q_WaistL"}},\
    {"display_name": "Q_WaistRFront (rel): WaistBack-WaistLFront-WaistR", "target": "Q_WaistRFront", "method": "relational", "settings": {"origin": "Q_WaistBack", "line": "Q_WaistLFront", "plane": "Q_WaistR"}}\
    ]


def _gap_fill_def(def_id):
    """Function for parsing and applying gap fill definitions"""
    #find trajectory ID of target
    gf_def = list_of_gap_fill_presets[def_id]
    marker_name = gf_def["target"]
    try:
        id_target = traj.find_trajectory(marker_name)
    except:
        msg_str = "Open a file"
        msg.add_message("gap_fill_presets: No file", msg_str, "error")
        return
    
    if id_target == None:
        msg_str = f"Target trajectory {marker_name} not found in measurement."
        msg.add_message("gap_fill_presets: Missing trajectory", msg_str, "warning")
        return
    
    #find gap ranges
    gap_ranges = data_3d.get_gap_ranges(id_target)
    
    gf_method = gf_def["method"]
    if gf_method in ["relational", "virtual"]:
        # Convert settings (modify local copy of the settings definition)
        settings = copy.deepcopy(gf_def["settings"])
        if "origin" in settings.keys():
            marker_name = settings["origin"]
            id_orig =  traj.find_trajectory(marker_name)
            if id_orig == None:
                msg_str = f"Origin trajectory {marker_name} not found in measurement."
                msg.add_message("gap_fill_presets: Missing trajectory", msg_str, "warning")
                return
            else:
                settings["origin"] = id_orig
        if "line" in settings.keys():
            marker_name = settings["line"]
            id_line =  traj.find_trajectory(marker_name)
            if id_line == None:
                msg_str = f"Line trajectory {marker_name} not found in measurement."
                msg.add_message("gap_fill_presets: Missing trajectory", msg_str, "warning")
                return
            else:
                settings["line"] = id_line
        if "plane" in settings.keys():
            marker_name = settings["plane"]
            id_plane =  traj.find_trajectory(marker_name)
            if id_plane == None:
                msg_str = f"Plane trajectory {marker_name} not found in measurement."
                msg.add_message("gap_fill_presets: Missing trajectory", msg_str, "warning")
                return
            else:
                settings["plane"] = id_plane
    else:
        settings = None
    
    gf_action = gf_def["display_name"]
    not_all_gaps_filled_flag = False
    for gap in gap_ranges:
        try:
            traj.fill_trajectory(id_target, gf_method, gap, settings)
        except:
            not_all_gaps_filled_flag = True
            continue
    
    if not_all_gaps_filled_flag:
        msg_str = f"Gap fill action {gf_action}:\nNot all gaps could be filled."
        msg.add_message("gap_fill_presets: Done (not all gaps)", msg_str, "warning")
    else:
        msg_str = f"Gap fill action {gf_action} successfully applied."
        msg.add_message("gap_fill_presets: Done", msg_str, "info")


def add_my_commands():
    """Function for adding new commands used in this script to QTM"""

    command_name = "disp_gap_fill_presets_doc"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(print(__doc__)))

    # Add commands for 10 relations (maximum number of relations, you can add more here if you want)
    # Work around for adding commands in for-loop since Python uses call by assignment
    command_name = "gap_fill_def_0"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(0)))
    
    command_name = "gap_fill_def_1"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(1)))
    
    command_name = "gap_fill_def_2"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(2)))
    
    command_name = "gap_fill_def_3"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(3)))
    
    command_name = "gap_fill_def_4"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(4)))
    
    command_name = "gap_fill_def_5"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(5)))
    
    command_name = "gap_fill_def_6"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(6)))
    
    command_name = "gap_fill_def_7"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(7)))
    
    command_name = "gap_fill_def_8"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(8)))
    
    command_name = "gap_fill_def_9"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_gap_fill_def(9)))
    


def setup_my_menu():
    """Function for setting up the menu."""
    my_menu_id = qtm.gui.insert_menu_submenu(None, "Gap fill presets")

    # Add Help button for display of the script doc string
    qtm.gui.insert_menu_button(my_menu_id, "Help", "disp_gap_fill_presets_doc")
    qtm.gui.insert_menu_separator(my_menu_id)

    # Add buttons for respective relations
    for i in range(len(list_of_gap_fill_presets)):
        disp_name = list_of_gap_fill_presets[i]["display_name"]
        command_name = "gap_fill_def_" + str(i)
        if not(any(uc == command_name for uc in qtm.gui.get_commands("user"))):
            msg_str = f"Number of gap fill definitions exceeds maximum:\n" + \
                f"Definitions {i+1} and higher are ignored."
            msg.add_message("gap_fill_presets: too many gap fill definitions", msg_str, "warning")
            break
            
        # Add button to Refine rigid body submenu with the rigid body name and associated command
        qtm.gui.insert_menu_button(my_menu_id, disp_name, command_name)

menu_priority = 1

def add_menu():
    # - Add commands and set up menu
    add_my_commands()
    setup_my_menu()


if __name__ == "__main__":
    add_menu()
