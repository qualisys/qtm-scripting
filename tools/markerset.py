"""
Markerset tools
 * Display markerset summary
 * Select Whole Markerset
 * Fix illegal characters for animation
 * Remove namespace characters up to the ':' for imported C3D files.
"""
import importlib

import qtm

import helpers.menu_tools
import helpers.traj

importlib.reload(helpers.menu_tools)
importlib.reload(helpers.traj)

from helpers.menu_tools import add_menu_item, add_command
from helpers.traj import get_default_markerset_marker, get_selected_markerset_marker

def _selectWholeMarkerset(markersetname) -> int:
	seriesIDs = qtm.data.series._3d.get_series_ids()
	newSelections = []
	for id in seriesIDs:
		fullname = qtm.data.object.trajectory.get_label(id)
		if fullname is not None and "_" in fullname:
			s = fullname.split("_",1)
			if markersetname == s[0]:
				newSelections.append({"type":"trajectory", "id":id})
	if len(newSelections) > 0:
		qtm.gui.selection.set_selections(newSelections)
		return len(newSelections)
	return 0
def _fixName(oldName) ->str:
	newName = ""
	for c in oldName:
		if c == " " or c == "." or c == "-" or c == ":":
			newName = newName+"_"
		else:
			newName = newName + c
	return newName

def _fix_C3D_name(oldName : str) ->str:
	return oldName.split(":")[-1]

# - - - - - - - - - - - - - - - - - -
# ////////   P U B L I C   ////////
# - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def summary():
    try:
        seriesIDs = qtm.data.series._3d.get_series_ids()
    except:
        print(f"No measurement")
        return
    noMarkersetCnt = 0
    noLabelCnt = 0
    invalidCnt = 0
    markersets = {}
    for id in seriesIDs:
        fullname = qtm.data.object.trajectory.get_label(id)
        if fullname is None:
            noLabelCnt = noLabelCnt + 1
        else:
            if " " in fullname or "." in fullname or "-" in fullname or ":" in fullname:
                invalidCnt = invalidCnt + 1
            if "_" in fullname:
                s = fullname.split("_",1)
                markersetname = s[0]
                markername = [1]
                if markersetname in markersets:
                    markerset = markersets[markersetname]
                    markersets.update({markersetname:markerset+1})
                else:
                    markersets[markersetname] = 1
            else:
                noMarkersetCnt = noMarkersetCnt + 1
    print(f"")
    print(f"Total markers: {len(seriesIDs)}")
    print(f"Total markersets: {len(markersets)}")
    for markersetname in markersets:
        markerset = markersets[markersetname]
        print(f"    {markersetname} has {markerset} markers")
    print(f"Total unlabeled: {noLabelCnt}")
    print(f"Total invalid  : {invalidCnt}")
    print(f"Total outside a markerset: {noMarkersetCnt}")
    
    # Force
    seriesIDs = qtm.data.series.force.get_series_ids()
    print(f"Found {len(seriesIDs)} force data series")

    seriesIDs = qtm.data.series._6d.get_series_ids()
    print(f"Found {len(seriesIDs)} rigid bodies")
    for id in seriesIDs:
        print(f"    ID is {id}")

def selectWholeMarkerset():
	if qtm.gui.selection.get_selection_count() == 0:
		print(f"Select a marker in the markerset.")
		return
	selections = qtm.gui.selection.get_selections()
	s = selections[0]
	id = s["id"]
	fullname = qtm.data.object.trajectory.get_label(id)
	if not fullname:
		print(f"An unnamed marker is selected.")
		return
	if not "_" in fullname:
		print(f"Selected marker is not in a markerset.")
		return
	s = fullname.split("_",1)
	markersetname = s[0]
	cnt =_selectWholeMarkerset(markersetname) 
	if cnt == 0:
		print(f"Nothing selected")
	else:
		print(f"Selected {cnt} markers.")
		
def fixInvalidMarkerNames():
	seriesIDs = qtm.data.series._3d.get_series_ids()
	fixedCnt = 0
	for id in seriesIDs:
		fullname = qtm.data.object.trajectory.get_label(id)
		if fullname is not None:
			if " " in fullname or "." in fullname or "-" in fullname or ":" in fullname:
				fixedName = _fixName(fullname)
				qtm.data.object.trajectory.set_label(id,fixedName)
				fixedCnt = fixedCnt + 1
	if fixedCnt > 0:
		print(f"Fixed {fixedCnt} marker names")
	else:
		print(f"No markers needed fixing.")		

def fix_C3D_names():
	seriesIDs = qtm.data.series._3d.get_series_ids()
	fixedCnt = 0
	for id in seriesIDs:
		fullname = qtm.data.object.trajectory.get_label(id)
		if fullname is not None:
			if ":" in fullname:
				fixedName = _fix_C3D_name(fullname)
				qtm.data.object.trajectory.set_label(id,fixedName)
				fixedCnt = fixedCnt + 1
	if fixedCnt > 0:
		print(f"Fixed {fixedCnt} marker names")
	else:
		print(f"No markers needed fixing.")		

menu_priority = 1

def add_menu():
	add_command("markerset_summary", summary)
	add_command("markerset_select_whole_markerset", selectWholeMarkerset)
	add_command("markerset_fix_invalid_marker_names", fixInvalidMarkerNames)
	add_command("markerset_fix_C3D_names", fix_C3D_names)
	add_command("markerset_help", lambda:(print(__doc__)))

	menu_id = qtm.gui.insert_menu_submenu(None,"Markerset")
	add_menu_item(menu_id, "Help", "markerset_help")
	qtm.gui.insert_menu_separator(menu_id)
	add_menu_item(menu_id, "Markerset Summary", "markerset_summary")
	add_menu_item(menu_id, "Select Whole Markerset", "markerset_select_whole_markerset")
	qtm.gui.insert_menu_separator(menu_id)
	add_menu_item(menu_id, "Fix Invalid Names", "markerset_fix_invalid_marker_names")
	add_menu_item(menu_id, "Fix C3D Names", "markerset_fix_C3D_names")


# endregion
if __name__ == "__main__":
    add_menu()