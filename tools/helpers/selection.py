import tools.helpers.traj as traj
import sys
import qtm


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E X P O R T E D   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def get_selected_marker_ids():
    selections = qtm.gui.selection.get_selections()
    return [selection["id"] for selection in selections if selection["type"] == "trajectory"]


def get_selected_bone_ids():
    selections = qtm.gui.selection.get_selections()
    return [selection["id"] for selection in selections if selection["type"] == "bone"]


def select_all_trajectories():
    selections = [{"type": "trajectory", "id": id} for id in qtm.data.series._3d.get_series_ids()]
    qtm.gui.selection.set_selections(selections)


def select_labeled_trajectories():
    selections = [{"type": "trajectory", "id": id} for id in traj.get_labeled_marker_ids()]
    qtm.gui.selection.set_selections(selections)


def select_unlabeled_trajectories():
    selections = [{"type": "trajectory", "id": id} for id in traj.get_unlabeled_marker_ids()]
    qtm.gui.selection.set_selections(selections)
# endregion
