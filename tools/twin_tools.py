"""twin_tools.py: Tools for twin system

General info
Tools for twin system. Currently, one method is included for twin calibration
based on 6DOF rigid bodies with a fixed relationship that can be used as an alternative
to the twin wand calibration, for example for application in which it is difficult to
access the volume with a wand.

Description of menu
This scripts adds a menu "Twin" to the QTM menu bar.
* Help: display help text for twin_tools.py
* Twin calibration (6DOF): 

Twin calibration (6DOF)
* Make sure that the Euler Angles definition setting in the QTM Project Options is set to
    "Qualisys standard".
* Create a single rigid body with two sets of markers that are visible to the respective
    systems (master and slave systems).
* Create a single rigid body definition including both sets of markers.
* Split the rigid body definition into two separate ones, for example by exporting and
    editing the XML and loading it into QTM again. This way, two rigid body definitions are
    created with a common origin and orientation.
    Note: Both rigid bodies should use global coordinates.
* Do a twin measurement with the rigid body in a central location in both volumes. Merge
    with zero twin calibration and Calculate 6DOF with the two rigid body definitions.
* Select a representative frame and press the "Twin calibration (6DOF)" button. This will
    display the calculated twin calibration parameters in the terminal window.
* In QTM Project Options, fill in the twin calibration parameters as a manual calibration in
    the twin calibration dialog and reprocess the file with the updated twin calibration.
* Make sure that the rigid body data is the same in the frame that was used for the
    calibration and not too different in the rest of the measurement. If ok, use the twin
    calibration for subsequent measurements.

Requirements:
* numpy

"""

#import importlib

import qtm

import qtm.data.series._6d as data_6d
import qtm.settings.processing._6d as rb

import qtm.gui.timeline as tline
import qtm.gui.message as msg

import math

have_numpy = True
try:
    import numpy as np
except:
    have_numpy = False


# Script variables (global)
# rb_refine_write_mode = "replace" # "replace"/"add": replace points in current rigid body definition, or add new refined rigid body
# rb_refine_menu_name = "Refine rigid body"

# --- Copied and adapted from qmath.py (from Jeffrey Thingvold)
# Checked definition in Diebel, J. (2006), Representing attitude
# Calculates rotation matrix to euler angles (Qualisys standard xyz)
def rotationMatrixToEulerAngles(R):
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6
 
    if  not singular :
        x = math.atan2(R[2,1] , R[2,2]) # roll
        y = math.atan2(-R[2,0], sy)     # pitch
        z = math.atan2(R[1,0], R[0,0])  # yaw
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
 
    return np.array([math.degrees(x), math.degrees(y), math.degrees(z)])
# ---

def _twin_calib_6dof():
    """Function for 6dof twin calibration."""

    # For algorithm, see Matlab script under C:\Users\labbuser\Documents\EST\Data\2023-08-25 Twin Oostende
    
    # Checks
    # - Check number of rigid bodies in file
    try:
        nrb_file = rb.get_body_count("measurement")
    except:
        msg_str = "A file should be open including two rigid bodies."
        msg.add_message("twin_tools: Parsing error (double click for info)", msg_str, "error")
        return
    
    if nrb_file != 2:
        msg_str = "The file must contain two rigid bodies."
        msg.add_message("twin_tools: Requirements not fulfilled (double click for info)", msg_str, "error")
        return
    
    # - Check coordinate system
    if not(rb.get_body_coordinate_system("measurement", 0)["type"] == "global") or \
            not(rb.get_body_coordinate_system("measurement", 1)["type"] == "global"):
        msg_str = "Rigid bodies' coordinate systems must be global for this operation."
        msg.add_message("twin_tools: Requirements not fulfilled (double click for info)", msg_str, "error")
        return
    
    # Check Euler convention
    if not(qtm.settings.euler.get_convention() == "qualisys"):
        msg_str = "Euler convention must be Qualisys standard for this operation."
        msg.add_message("twin_tools: Requirements not fulfilled (double click for info)", msg_str, "error")
        return

    # Get current frame
    try:
        cf = tline.get_current_frame()
    except: 
        msg_str = "6DOF twin calibration not supported in Preview mode.\nMake a capture and try again."
        msg.add_message("twin_tools: Parsing error (double click for info)", msg_str, "error")
        return
        
    # Calculate rotation of rigid body 2 (slave) relative to rigid body 1 (master) at current frame
    series_id_0 = data_6d.get_series_id(0)
    RT_0 = np.array(data_6d.get_sample(series_id_0, cf)["transform"])
    T_0 = RT_0.transpose()[3,0:3]

    series_id_1 = data_6d.get_series_id(1)
    RT_1 = np.array(data_6d.get_sample(series_id_1, cf)["transform"])
    T_1 = RT_1.transpose()[3,0:3]
    
    R_align = np.matmul(RT_1[0:3,0:3], RT_0[0:3,0:3].transpose())

    # Rotate rigid body 2 position (align rigid body 2 to rigid body 1)
    T1_aligned = np.matmul(T_1, R_align)

    # Calculate translation of rigid body 2 (slave after rotation) relative to rigid body 1 (master)
    D = T_0 - T1_aligned

    # Convert rotation to Euler (RPY)
    RPYs = -rotationMatrixToEulerAngles(R_align)

    # Put twin calibration parameters in list (negative Euler angles for QTM coordinate rotation)
    tp = [D[0], D[1], D[2], \
            RPYs[0], RPYs[1], RPYs[2]]

    print(f"\n--- Twin calibration (6DOF) ---")
    print(f"Twin System calibration parameters (X, Y, Z, Roll, Pitch, Yaw): ")
    print(f"{tp[0]:.3f}, {tp[1]:.3f}, {tp[2]:.3f}, {tp[3]:.3f}, {tp[4]:.3f}, {tp[5]:.3f}\n\n")
    print(f"Fill in as 'Manual Calibration' in the twin calibration dialog.")

    msg_str = f"Twin parameters (XYZRPY): {tp[0]:.3f}, {tp[1]:.3f}, {tp[2]:.3f}, {tp[3]:.3f}, {tp[4]:.3f}, {tp[5]:.3f}"
    msg.add_message("twin_tools: Done (see terminal for result)", msg_str, "info")


def add_my_commands():
    """Function for adding new commands used in this script to QTM"""

    # Add command for display of script doc string
    command_name = "disp_twin_tools_doc"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(print(__doc__)))

    # Add command for 6dof twin calibration 
    qtm.gui.add_command("twin_calib_6dof")
    qtm.gui.set_command_execute_function("twin_calib_6dof", _twin_calib_6dof)


def setup_my_menu():
    """Function for setting up the menu."""
    my_menu_id = qtm.gui.insert_menu_submenu(None, "Twin")
    
    # Add Help button for display of the script doc string
    qtm.gui.insert_menu_button(my_menu_id, "Help", "disp_twin_tools_doc")
    qtm.gui.insert_menu_separator(my_menu_id)

    # Add button for updating Refine rigid body menu items.
    qtm.gui.insert_menu_button(my_menu_id, "Twin calibration (6DOF)", "twin_calib_6dof")

menu_priority = 1

def add_menu():
    if have_numpy:
        # - Add commanads and set up menu
        add_my_commands()
        setup_my_menu()
    else:
        print(f"You need Numpy installed in Python to use the Twin menu.")

if __name__ == "__main__":
    add_menu()