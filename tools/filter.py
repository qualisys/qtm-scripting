"""
Filter tools menu

Functions for printing and eliminating spikes in the currently selected trajectories.

Printing is done to the terminal window.  Spikes are found using a hardcoded acceleration value that
is similar to the default value in the Trajectory Window (150m/s^2).  It is not currently possible to
query the value in the Trajectory editor.

The median cut filter is a special filter that finds the median value of the curve around the location
of the spike then replaces the 'spike' with that median value.  One characteristic of this filter is
that applying it twice (or more) has no effect on the data.  This filter in conjunction with a smoothing
filter makes for a great way of eliminating spikes in trajectories.
"""
import sys
import os
import inspect
import importlib
import math

this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)

import qtm

import helpers.menu_tools
import helpers.traj

importlib.reload(helpers.menu_tools)
importlib.reload(helpers.traj)

from helpers.menu_tools import add_menu_item, add_command
from helpers.traj import get_default_markerset_marker, get_selected_markerset_marker

def _markerAcceleration(id : int, frame :int, deltat: float):
    try:
        trajData = qtm.data.series._3d.get_sample(id,frame)
    except:
        return 0
    if trajData is None:
        return 0
    try:
        trajDataLeft = qtm.data.series._3d.get_sample(id,frame-1)
    except:
        trajDataLeft = trajData
    try:
        trajDataRight = qtm.data.series._3d.get_sample(id,frame+1)
    except:
        trajDataRight = trajData
    if trajDataLeft is None or trajDataRight is None:
        return 0
        
    p0 = trajDataLeft["position"]
    p1 = trajData["position"]
    p2 = trajDataRight["position"]
        

    a  = [0.0,0.0,0.0]

    a[0] = (p0[0] - 2 * p1[0] + p2[0])
    a[1] = (p0[1] - 2 * p1[1] + p2[1])
    a[2] = (p0[2] - 2 * p1[2] + p2[2])

    acc = (math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2]))/(deltat*deltat)

    return acc
def _get_spike_ranges(id:int):
    # QTM default is 150
    threshold = 150.0 
    frames = qtm.gui.timeline.get_frame_count()
    freq = qtm.data.series._3d.get_frequency(id)

    width = 3 #number of frames before and after the values above the threshold
    inSpike = False
    inWidth = False
    widthCount = 0
    start = 0
    end = 0
    spikeRanges = []
    f = 1
    while f < frames:
        acc = _markerAcceleration(id,f,1.0/freq) /1000.0
        try:
            trajData = qtm.data.series._3d.get_sample(id,f)
        except:
            trajData = None
        if trajData is None:
            if inSpike:
                end = f-1
                spikeRanges.append({"start":start, "end":end})

            inSpike = False
            inWidth = False
            start = 0
            end = 0
            f = f+width #skip ahead
        else:
            if not inSpike:
                if acc > threshold:
                    inSpike = True
                    start = f-width
                    widthCount = 0
                    #print(f"InSpike: frame={f}  start={start} acc={acc:.4f}")
            else:

                if inWidth:
                    if acc < threshold:
                        widthCount = widthCount+1
                        if widthCount >= width:
                            inSpike = False
                            widthCount = 0
                            end = f
                            spikeRanges.append({"start":start, "end":end})
                    else:
                        widthCount = 0
                else:
                    if acc < threshold:
                        inWidth = True
                    else:
                        inWidth = False
                        widthCount=0
        f = f + 1

    return spikeRanges
def _medianValue(X: [], width: int, debug: bool = False):
    # simple bubble sort, it's a short array
    i = width * 2 + 1
    if debug:
        print(f"Before: X{X}")
    while i >= 0:
        r = range(0,i-1,1)
        for j in r:
            #print (f"j: {j}")
            if X[j] > X[j+1]:
                tmp = X[j]
                X[j] = X[j+1]
                X[j+1] = tmp
        i=i-1
    if debug:
        print(f"After : X{X}; median={X[width]}")
    return X[width]

# just calculate the median cut result, don't update any data
def _medianCutFrameResult(id:int, frame: int, width:int=2):
    X=[]
    Y=[]
    Z=[]
    r = range(0, 2* width+1, 1)
    for i in r:
        X.append(0)
        Y.append(0)
        Z.append(0)

    trajDataCurrentFrame = qtm.data.series._3d.get_sample(id,frame)
    if trajDataCurrentFrame is None:
        return None
    defXYZ = trajDataCurrentFrame["position"]
    residual = trajDataCurrentFrame["residual"]
    widthRange = range(frame-width, frame+width, 1)
    j = 0
    k = frame-width
    while k <= (frame+width):
        trajData = qtm.data.series._3d.get_sample(id,k)
        if trajData is not None:
            xyz = trajData["position"]
            X[j] = xyz[0]
            Y[j] = xyz[1]
            Z[j] = xyz[2]
        else:
            X[j] = defXYZ[0]
            Y[j] = defXYZ[1]
            Z[j] = defXYZ[2]
        j=j+1
        k=k+1
    
    newX = _medianValue(X, width, False)
    newY = _medianValue(Y, width, False)
    newZ = _medianValue(Z, width, False)
    return {'position':[newX,newY,newZ], 'residual':residual}

def _isclose_position(a: [], b: []):
    if math.isclose(a[0],b[0], abs_tol = 1e-04) and math.isclose(a[1],b[1], abs_tol = 1e-04) and math.isclose(a[2],b[2], abs_tol = 1e-04):
        return True
    return False
    
# Save new values in temp array to avoid updating data
# during the middle of the calculations (have to use old values for
# all calculations).  Then update data only when it's different
def _medianCutRange(id: int, start: int, end: int, width:int = 2):

    r = range(start+width, end-width, 1) 
    origTrajData = []
    newTrajData = []
    for frame in r:
        origTrajData.append(qtm.data.series._3d.get_sample(id,frame))
        newTrajData.append(_medianCutFrameResult(id, frame, width))

    i = 0
    for frame in r:
        oTJ = origTrajData[i]
        nTJ = newTrajData[i]
        if oTJ is not None and nTJ is not None:
            origXYZ = oTJ["position"]
            newXYZ = nTJ["position"]
            if not _isclose_position(origXYZ, newXYZ):
                qtm.data.series._3d.set_sample(id,frame,nTJ)
        i = i+1

# get the mediam cut result, update the data if it's a new value
def _medianCutFrame(id: int, frame: int, width:int=2):
    origTrajData = qtm.data.series._3d.get_sample(id,frame)
    if origTrajData is None:
        return
    newTrajData = _medianCutFrameResult(id, frame, width)
    if newTrajData is None:
        return
    origXYZ = origTrajData["position"]
    newXYZ = newTrajData["position"]
    if not _isclose_position(origXYZ, newXYZ):
        qtm.data.series._3d.set_sample(id,frame,newTrajData)

# - - - - - - - - - - - - - - - - - -
# ////////   P U B L I C   ////////
# - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def printSpikeRangesSelected():
    if qtm.gui.selection.get_selection_count() == 0:
        return 0
    selections = qtm.gui.selection.get_selections()
    for s in selections:
        id = s["id"]
        name = qtm.data.object.trajectory.get_label(id)

        spikeRanges = _get_spike_ranges(id)
        print(f"{name}")
        if len(spikeRanges) == 0:
            print(f"    No spikes")
        else:
            for r in spikeRanges:
                print(f"    {r}")

# Callback function for QTM menu
def medianCutFilterSelected():
    if qtm.gui.selection.get_selection_count() == 0:
        return 0
    selections = qtm.gui.selection.get_selections()
    for s in selections:
        id = s["id"]
        spikeRanges = _get_spike_ranges(id)
        for r in spikeRanges:
            start = r["start"]
            end = r["end"]
            _medianCutRange(id,start, end)

# Callback function for QTM menu
def medianCutFilterSelectedFrame():
    if qtm.gui.selection.get_selection_count() == 0:
        return 0
    selections = qtm.gui.selection.get_selections()
    s = selections[0]
    id = s["id"]
    currentFrame = qtm.gui.timeline.get_current_frame()

    _medianCutFrame(id,currentFrame)

# callback funtion for QTM menu
# smooth only the spiked regions
def smoothSpikesSelected():
    if qtm.gui.selection.get_selection_count() == 0:
        return 0
    selections = qtm.gui.selection.get_selections()
    s = selections[0]
    id = s["id"]
    spikeRanges = _get_spike_ranges(id)
    if len(spikeRanges) == 0:
        print(f"No spikes found")
    else:
        for r in spikeRanges:
            qtm.data.object.trajectory.smooth_trajectory(id,None,r, None)

def medianCutThenSmoothSelected():
    
    if qtm.gui.selection.get_selection_count() == 0:
        return 0
    selections = qtm.gui.selection.get_selections()
    s = selections[0]
    id = s["id"]
    spikeRanges = _get_spike_ranges(id)
    if len(spikeRanges) == 0:
        print(f"No spikes found")
    else:
        for r in spikeRanges:
            start = r["start"]
            end = r["end"]
            _medianCutRange(id,start, end)
            qtm.data.object.trajectory.smooth_trajectory(id,None,r, None)

menu_priority = 10
def add_menu():

    add_command("filter_median_cut_selected", medianCutFilterSelected)
    add_command("filter_median_cut_selected_frame", medianCutFilterSelectedFrame)
    add_command("filter_median_cut_then_smooth_spikes_selected", medianCutThenSmoothSelected)
    add_command("filter_smooth_spikes_selected", smoothSpikesSelected)
    add_command("filter_print_spike_ranges_selected", printSpikeRangesSelected)
    add_command("filter_help", lambda:(print(__doc__)))


    menu_id = qtm.gui.insert_menu_submenu(None,"Filter")
    add_menu_item(menu_id, "Help", "filter_help")
    qtm.gui.insert_menu_separator(menu_id)
    add_menu_item(menu_id, "Median Cut Filter Selected", "filter_median_cut_selected")
    add_menu_item(menu_id, "Median Cut Filter Selected Frame", "filter_median_cut_selected_frame")
    add_menu_item(menu_id, "Median Cut Filter Then Smooth Spikes", "filter_median_cut_then_smooth_spikes_selected")
    add_menu_item(menu_id, "Smooth Spikes Selected", "filter_smooth_spikes_selected")
    qtm.gui.insert_menu_separator(menu_id)
    add_menu_item(menu_id, "Print Spike Ranges Selected", "filter_print_spike_ranges_selected")
# endregion

if __name__ == "__main__":
    add_menu()