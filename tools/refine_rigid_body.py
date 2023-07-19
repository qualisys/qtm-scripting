"""refine_rigid_body.py: Script for refining rigid body definition based on a measurement

Use this script to refine the points in a rigid body definition in
the QTM project, based on a measurement with the same rigid body.

This can be useful for adapting a default rigid body defintion to an actually
measured one, for example for tracking of Tobii glasses.

When loading the script, a menu "Refine rigid body" is added to QTM containing
a list of rigid bodies in the project.

The menu contains the following buttons:
* Update rigid body list... Use this to update the rigid bodies listed in the submenu
* Buttons for the rigid bodies in the project. The number of rigid bodies is limited
to 10, but this can be changed by editing the script.

Use of the script:
* Make sure that a file is opened that is processed with the same rigid bodies as
  in the project.
* Set the current frame to a frame where all markers of the rigid body are present and
  without artifact.
* Press the button for a rigid body to update it or add a new, refined version of the
  rigid body to the project, dependent on the rb_refine_write_mode (script variable).
* Make sure to press the Update button when rigid body definitions are added or removed
  from the project.

Script variables (global):
* rb_refine_write_mode: ("replace" or "add") replace points in current rigid body definition, or add
  new refined rigid body
* rb_refine_menu_name: Name of the QTM menu added by the script

Requirements:
* numpy

"""

import importlib

import qtm

import qtm.data.object.trajectory as traj
import qtm.data.series._3d as data_3d

import qtm.data.series._6d as data_6d
import qtm.settings.processing._6d as rb

import qtm.gui.timeline as tline
import qtm.gui.terminal as trm
import qtm.utilities.color as clr
have_numpy = True
try:
    import numpy as np
except:
    have_numpy = False


# Script variables (global)
rb_refine_write_mode = "replace" # "replace"/"add": replace points in current rigid body definition, or add new refined rigid body
rb_refine_menu_name = "Refine rigid body"

def _refine_rigid_body(rb_id):
    """Function for creating the refined definition of the selected rigid body."""
    # Refine points of rigid body with id rb_id
    #trm.write(f"Refining rb_id {rb_id}")
    
    # Checks
    # - Check index
    if rb.get_body_count("project") < rb_id+1:
        #raise Exception("Index to non-existing rigid body: " + str(rb_id+1))
        trm.write("Index to non-existing rigid body: " + str(rb_id+1))
        #sys.exit()
        return
    
    # - Check coordinate system
    if not(rb.get_body_coordinate_system("project", rb_id)["type"] == "global"):
        #raise Exception("Rigid body '{name}' coordinate system should be global for this operation."
        #    .format(name = rb.get_body_name("project", rb_id)))
        trm.write("Rigid body '{name}' coordinate system should be global for this operation."
            .format(name = rb.get_body_name("project", rb_id)))
        return
    
    # Add a check that a file is open including the rigid body referenced in the project.
    # The rigid bodies in the project and the file should be the same.
    # Check for current rigid body if this is the case (no check for points, it is assumed that the axes definitions are the same; if not the refined points can be very different from the original definition).
    try:
        nrb_file = rb.get_body_count("measurement")
        rb_file_name = rb.get_body_name("measurement",rb_id)
        rb_file_type = rb.get_body_coordinate_system("measurement", rb_id)["type"]
    except:
        # logging.error("A file should be open with the same rigid bodies as in the project.")
        trm.write("A file should be open with the same rigid bodies as in the project.")
        return
    if nrb_file < rb_id:
        trm.write("A file should be open with the same rigid bodies as in the project.")
        return
    if not(rb_file_name == rb.get_body_name("project",rb_id)):
        trm.write("A file should be open with the same rigid bodies as in the project.")
        return
    if not(rb_file_type == "global"):
        trm.write("A file should be open with the same rigid bodies as in the project.")
        return
    
    
    # Make a list of points (names and positions)
    n_pts = rb.get_point_count("project", rb_id)
    pt_names = []
    pt_idx = []
    #pt_pos = []
    for i in range(n_pts):
        if not(rb.get_point_is_virtual("project",rb_id, i)):
            pt_names.append(rb.get_point_name("project", rb_id, i))
            pt_idx.append(i)
            #pt_pos.append(rb.get_point_position("project", rb_id, i))
    #trm.write(str(pt_names))
    #trm.write("Rigid body points:\n" + str(pt_pos))
    
    # Find corresponding trajectories (current file, current sample)
    traj_points = []
    try:
        cf = tline.get_current_frame()
    except: 
        trm.write("Refine rigid body not supported in Preview mode.\nMake a capture and try again.")
        return
    
    try:
        for pt_name in pt_names:
            traj_id = traj.find_trajectory(pt_name)
            traj_points.append(data_3d.get_sample(traj_id, cf)["position"])
        tpts = np.array(traj_points)
    except:
        trm.write(f"All trajectories of the rigid body '{rb_file_name}' must be present and filled at the current frame.")
        return
    
    # Transform trajectories to local coordinates of the rigid body
    series_id = data_6d.get_series_id(rb_id)
    RT = np.array(data_6d.get_sample(series_id, cf)["transform"])
    #trm.write("Current rigid body pose:\n" + str(RT))
    T = RT.transpose()[3,0:3]
    tpts_trl = tpts-T
    tpts_trf = np.matmul(tpts_trl,RT[0:3,0:3])
    #trm.write("Transformed points:\n" + str(tpts_trf))
    
    if (rb_refine_write_mode == "replace"):
        # Overwrite point coordinates (virtual points are ignored)
        for i in range(len(pt_idx)):
            rb.set_point_position("project", rb_id, pt_idx[i], tpts_trf[i].tolist())
            
        trm.write("The rigid body '{name}' has been successfully refined."
            .format(name = rb.get_body_name("project", rb_id)))
    else:
        # Add new rigid body with refined points (virtual points are not included)
        new_id = rb.add_body("project")
        rb.set_body_name("project", new_id, 
            rb.get_body_name("project", rb_id) + "_refined")
        rb.set_body_color("project", new_id, clr.rgb(0,192/255,0))
        i = 0
        for i in range(len(pt_names)):
            rb.add_point("project", new_id)
            rb.set_point_name("project", new_id, i, pt_names[i])
            rb.set_point_position("project", new_id, i, tpts_trf[i].tolist())
            
        trm.write("The refined rigid body '{name}' has been successfully added to the project."
            .format(name = rb.get_body_name("project", new_id)))


def _update_rb_refine_items():
    """Function for updating the rigid body refine submenu."""
    # Retrieve menu handles
    list_of_dicts_all_menus = qtm.gui.get_menu_items()
    for curr_menu_dict in list_of_dicts_all_menus:
        if curr_menu_dict["text"] == rb_refine_menu_name:
            my_menu_id = curr_menu_dict["submenu"]
            break
    
    # Clear current rigid body items (associated with refine command)
    # list_of_dicts_items = qtm.gui.get_menu_items(rfrb_id)
    list_of_dicts_items = qtm.gui.get_menu_items(my_menu_id)
    for i in reversed(range(len(list_of_dicts_items))):
        if list_of_dicts_items[i]["command"][:6] == "refine":
            qtm.gui.delete_menu_item(my_menu_id,i)
    
    n_rb = rb.get_body_count("project")
    if n_rb == 0:
        trm.write(f"No rigid body definitions found in the current project.")
        return
    
    for i in range(n_rb):
        rb_name = rb.get_body_name("project",i)
        # Check if command exists (write warning to terminal if not)
        # If not, add command and define execute function
        command_name = "refine_rigid_body_" + str(i)
        if not(any(uc == command_name for uc in qtm.gui.get_commands("user"))):
            trm.write(f"Number of rigid bodies in the project exceeds index:\n" + \
                f"- Rigid bodies no. {i+1} and higher are ignored.")
            break
            
        # Add button to Refine rigid body submenu with the rigid body name and associated command
        qtm.gui.insert_menu_button(my_menu_id, rb_name, command_name)
        #trm.write(f"Added button {rb_name} with command {command_name}")


def add_my_commands():
    """Function for adding new commands used in this script to QTM"""

    # Add command for display of script doc string
    command_name = "disp_refine_rigid_body_doc"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(print(__doc__)))

    # Add command for updating the rigid body list for the 
    qtm.gui.add_command("update_rb_refine_items")
    qtm.gui.set_command_execute_function("update_rb_refine_items", _update_rb_refine_items)
    
    # Add commands for 10 rigid bodies (maximum number that can be refined this way, you can add more here if you want)
    # Work around for adding commands in for-loop since Python uses call by assignment
    command_name = "refine_rigid_body_0"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(0)))
    
    command_name = "refine_rigid_body_1"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(1)))
    
    command_name = "refine_rigid_body_2"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(2)))
    
    command_name = "refine_rigid_body_3"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(3)))
    
    command_name = "refine_rigid_body_4"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(4)))
    
    command_name = "refine_rigid_body_5"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(5)))
    
    command_name = "refine_rigid_body_6"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(6)))
    
    command_name = "refine_rigid_body_7"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(7)))
    
    command_name = "refine_rigid_body_8"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(8)))
    
    command_name = "refine_rigid_body_9"
    qtm.gui.add_command(command_name)
    qtm.gui.set_command_execute_function(command_name, lambda:(_refine_rigid_body(9)))
    


def setup_my_menu():
    """Function for setting up the menu."""
    my_menu_id = qtm.gui.insert_menu_submenu(None, rb_refine_menu_name)
    
    # Add Help button for display of the script doc string
    qtm.gui.insert_menu_button(my_menu_id, "Help", "disp_refine_rigid_body_doc")
    qtm.gui.insert_menu_separator(my_menu_id)

    # Add button for updating Refine rigid body menu items.
    qtm.gui.insert_menu_button(my_menu_id, "Update rigid body list...", "update_rb_refine_items")
    qtm.gui.insert_menu_separator(my_menu_id)

    # Add rigid body items
    _update_rb_refine_items()

menu_priority = 1

def add_menu():
    if have_numpy:
        # - Add commanads and set up menu
        add_my_commands()
        setup_my_menu()
    else:
        print(f"You need Numpy installed in Python to use the Refine Rigid Body menu.")

if __name__ == "__main__":
    add_menu()