"""
Gap filling tools
 * Relational fills for the animation markerset.
 * Trim gaps
 * Filling in the beginning or ending of a trajectory.

 There are two relational fill definitions for the markers.  Various combinations of using the
 first, second or both in multiple passes can be invoked.  It works on the currently selected
 trajectories.
"""
import sys
import os
import inspect
import importlib

import qtm

this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)

# import tools.helpers.tools
# import tools.helpers.traj

# importlib.reload(tools.helpers.tools)
# importlib.reload(tools.helpers.traj)

# from tools.helpers.tools import add_menu_item, add_command
# from tools.helpers.traj import get_default_markerset_marker, get_selected_markerset_marker
import helpers.menu_tools
import helpers.traj

importlib.reload(helpers.menu_tools)
importlib.reload(helpers.traj)

from helpers.menu_tools import add_menu_item, add_command
from helpers.traj import get_default_markerset_marker, get_selected_markerset_marker

# Hardcoded relationships for all animation markers
# Two of them is usually enough, the first is a 
# sensible set of relations, the second is CRAZY :-)
#
Arel = []
Arel.append({"HeadL":("HeadR","HeadFront","HeadTop"),
        "HeadTop":("HeadR","HeadFront","HeadL"),
        "HeadR":("HeadL","HeadFront","HeadTop"),
        "HeadFront":("HeadTop","HeadL","HeadR"),
        "LShoulderTop":("LShoulderBack","SpineTop","Chest"),
        "LShoulderBack":("LShoulderTop","SpineTop","Chest"),
        "LArm":("LShoulderTop","LShoulderBack","LElbowOut"),
        "LElbowOut":("LArm","LWristOut","LWristIn"),
        "LWristOut":("LWristIn","LHandOut","LElbowOut"),
        "LWristIn":("LWristOut","LHandOut","LArm"),
        "LHandOut":("LeftHandExtra","LWristIn","LWristOut"),
        "LeftHandExtra":("LHandOut","LWristIn","LWristOut"),
        "LThumbTip":("LHandIn","LWristIn","LWristOut"),
        "LIndexTip":("LHandIn","LWristIn","LWristOut"),
        "LPinkyTip":("LHandOut","LWristOut","LWristIn"),
        "RShoulderTop":("RShoulderBack","SpineTop","Chest"),
        "RShoulderBack":("RShoulderTop","SpineTop","Chest"),
        "RArm":("RShoulderTop","RShoulderBack","RElbowOut"),
        "RElbowOut":("RArm","RWristOut","RWristIn"),
        "RWristOut":("RWristIn","RHandOut","RElbowOut"),
        "RWristIn":("RWristOut","RHandOut","RArm"),
        "RHandOut":("RightHandExtra","RWristIn","RWristOut"),
        "RightHandExtra":("RHandOut","RWristIn","RWristOut"),
        "RThumbTip":("RHandIn","RWristIn","RWristOut"),
        "RIndexTip":("RHandIn","RWristIn","RWristOut"),
        "RPinkyTip":("RHandOut","RWristOut","RWristIn"),
        "Chest":("SpineTop","BackR","BackL"),
        "SpineTop":("Chest","BackR","BackL"),
        "BackL":("BackR","Chest","WaistLBack"),
        "BackR":("BackL","Chest","WaistRBack"),
        "WaistLFront":("WaistRFront","WaistLBack","WaistRBack"),
        "WaistLBack":("WaistLFront","WaistRBack","WaistRFront"),
        "WaistRBack":("WaistRFront","WaistLBack","WaistLFront"),
        "WaistRFront":("WaistLFront","WaistRBack","WaistLBack"),
        "LThigh":("WaistLFront","LKneeOut","WaistLBack"),
        "LKneeOut":("LThigh","LShin","LAnkleOut"),
        "LShin":("LKneeOut","LAnkleOut","LHeelBack"),
        "LAnkleOut":("LShin","LHeelBack","LForefootOut"),
        "LHeelBack":("LAnkleOut","LForefootOut","LToeTip"),
        "LForefootOut":("LHeelBack","LToeTip","LAnkleOut"),
        "LForefootIn":("LForefootOut","LToeTip","LAnkleOut"),
        "LToeTip":("LForefootOut","LHeelBack","LAnkleOut"),
        "RThigh":("WaistRFront","RKneeOut","WaistRBack"),
        "RKneeOut":("RThigh","RShin","RAnkleOut"),
        "RShin":("RKneeOut","RAnkleOut","RHeelBack"),
        "RAnkleOut":("RShin","RHeelBack","RForefootOut"),
        "RHeelBack":("RAnkleOut","RForefootOut","RToeTip"),
        "RForefootOut":("RHeelBack","RToeTip","RAnkleOut"),
        "RForefootIn":("RForefootOut","RToeTip","RAnkleOut"),
        "HeadFL":("HeadFR","HeadBR","SpineTop"),
        "HeadFR":("HeadFL","HeadBR","SpineTop"),
        "HeadBR":("HeadFR","HeadFL","SpineTop"),
        "ChestLow":("SpineLow","WaistLBack","WaistRBack"),
        "SpineLow":("ChestLow","WaistRFront","WaistLFront"),
        "LForeArm":("LWristOut","LElbowOut","LArm"),
        "RForeArm":("RWristOut","RElbowOut","RArm")
        })

Arel.append({"HeadL":("SpineTop","LShoulderTop","RShoulderTop"),
        "HeadTop":("SpineTop","LShoulderTop","RShoulderTop"),
        "HeadR":("SpineTop","LShoulderTop","RShoulderTop"),
        "HeadFront":("SpineTop","LShoulderTop","RShoulderTop"),
        "LShoulderTop":("LShoulderBack","SpineTop","Chest"),
        "LShoulderBack":("RShoulderBack","RArm","Chest"),
        "LArm":("Chest","BackL","LWristOut"),
        "LElbowOut":("LShoulderTop","LArm","Chest"),
        "LWristOut":("LElbowOut","LArm","Chest"),
        "LWristIn":("LElbowOut","LArm","Chest"),
        "LHandOut":("LElbowOut","LArm","Chest"),
        "LeftHandExtra":("LElbowOut","LArm","Chest"),
        "RShoulderTop":("LShoulderTop","SpineTop","Chest"),
        "RShoulderBack":("LShoulderBack","SpineTop","Chest"),
        "RArm":("Chest","BackR","RWristOut"),
        "RElbowOut":("RShoulderTop","RArm","Chest"),
        "RWristOut":("RElbowOut","RArm","Chest"),
        "RWristIn":("RElbowOut","RArm,","Chest"),
        "RHandOut":("RElbowOut","RArm","Chest"),
        "RightHandExtra":("RElbowOut","RArm","Chest"),
        "Chest":("LShoulderBack","RShoulderBack","RShoulderTop"),
        "SpineTop":("WaistRFront","WaistLFront","RShoulderTop"),
        "BackL":("WaistLFront","WaistRFront","LThigh"),
        "BackR":("WaistRFront","WaistLFront","RThigh"),
        "WaistLFront":("BackL","BackR","SpineTop"),
        "WaistLBack":("BackR","BackL","SpineTop"),
        "WaistRBack":("Chest","SpineTop","BackL"),
        "WaistRFront":("Chest","BackL","BackR"),
        "LThigh":("WaistRFront","WaistRBack","BackR"),
        "LKneeOut":("WaistLFront","WaistLBack","LAnkleOut"),
        "LShin":("LThigh","LForefootOut","LToeTip"),
        "LAnkleOut":("LToeTip","LShin","LThigh"),
        "LHeelBack":("LShin","LThigh","WaistLFront"),
        "LForefootOut":("LShin","LThigh","WaistLFront"),
        "LForefootIn":("LShin","LThigh","WaistLFront"),
        "LToeTip":("LShin","LThigh","WaistLFront"),
        "RThigh":("WaistLFront","WaistLBack","BackL"),
        "RKneeOut":("WaistRFront","WaistRBack","RAnkleOut"),
        "RShin":("RThigh","RForefootOut","RToeTip"),
        "RAnkleOut":("RToeTip","RShin","RThigh"),
        "RHeelBack":("RShin","RThigh","WaistRFront"),
        "RForefootOut":("RShin","RThigh","WaistRFront"),
        "RForefootIn":("RShin","RThigh","WaistRFront"),
        "RToeTip":("RShin","RThigh","WaistRFront"),
        "HeadFL":("Chest","ChestLow","SpineLow"),
        "HeadFR":("Chest","ChestLow","SpineLow"),
        "HeadBR":("Chest","ChestLow","SpineLow"),
        "ChestLow":("SpineTop","WaistRFront","WaistLFront"),
        "SpineLow":("Chest","WaistRFBack","WaistLBack"),
        "LForeArm":("LArm","LShoulderTop","LShoulderBack"),
        "RForeArm":("RArm","RShoulderTop","RShoulderBack")})


def _print_gaps(mname):
    """
    Print All the gaps for the markerset where a relational fill is available
    """
    nogaps = True
    for marker in Arel[0]:
        (oname, lname, pname) = Arel[0][marker]
        m_id = qtm.data.object.trajectory.find_trajectory(mname+"_"+marker)
        if m_id == None:
            # print(f"Bad marker name: {marker}")
            pass
        else:
            gaps = qtm.data.series._3d.get_gap_ranges(m_id)
            for g in gaps:
                start = g["start"]
                end = g["end"]
                print(f"Marker:{marker} start:{start} end:{end}")
                nogaps = False
    if nogaps:
        print(f"No Gaps!")

                    
def _doFillGapsSelected(rels):
    selections = qtm.gui.selection.get_selections()
    for s in selections:
        m_id = s["id"]
        fullmarker = qtm.data.object.trajectory.get_label(m_id)
        s = fullmarker.split("_",1)
        mname = s[0]
        marker = s[1]
        
        if marker in rels:
            (oname, lname, pname) = rels[marker]
            o_id = qtm.data.object.trajectory.find_trajectory(mname+"_"+oname)
            l_id = qtm.data.object.trajectory.find_trajectory(mname+"_"+lname)
            p_id = qtm.data.object.trajectory.find_trajectory(mname+"_"+pname)

            gaps = qtm.data.series._3d.get_gap_ranges(m_id)
            if len(gaps)>0:
                for g in gaps:
                    start = g["start"]
                    end = g["end"]
                    try:
                        qtm.data.object.trajectory.fill_trajectory(m_id,"relational",{"start":start,"end":end},{"origin":o_id, "line":l_id,"plane":p_id})
                    except RuntimeError:
                        print(f"  {marker} failed at frame {start}")
                        pass
        else:
            print(f"Marker relationship not found for {marker}.")



# constantValue not True means to use velocity
def _FillEndGap(constantValue: bool = True):

    mRange = qtm.gui.timeline.get_measured_range()
    end = mRange["end"]

    selections = qtm.gui.selection.get_selections()
    for s in selections:
        m_id = s["id"]
        fullmarker = qtm.data.object.trajectory.get_label(m_id)
        velocity = [0.0,0.0,0.0]
        value = [0.0,0.0,0.0]
        if qtm.data.series._3d.get_sample(m_id,end):
            print(f"{fullmarker} has no end gap")
        else:
            frame = end - 1
            valueFound = False
            gapStart = 0
            while not valueFound:
                frameData = qtm.data.series._3d.get_sample(m_id,frame)
                if frameData:
                    valueFound = True
                    beginValue = frameData["position"]
                    residual = frameData["residual"]
                    gapStart = frame + 1
                    if not constantValue:
                        frameData = qtm.data.series._3d.get_sample(m_id,frame-1)
                        if frameData:
                            value = frameData["position"]
                            velocity[0] = beginValue[0] - value[0]
                            velocity[1] = beginValue[1] - value[1]
                            velocity[2] = beginValue[2] - value[2]
                        else:
                            print(f"{fullmarker} Can not compute velocity")
                frame = frame -1
                if frame <= 0:
                    print(f"Whoa! No data at all for {fullmarker}!")
                    return
            if valueFound:
                print(f"{fullmarker} end range: ({gapStart},{end})  Value is {beginValue} Velocity is {velocity}")
                value[0] = beginValue[0] + velocity[0]
                value[1] = beginValue[1] + velocity[1]
                value[2] = beginValue[2] + velocity[2]
                for frame in range(gapStart,end+1):
                    qtm.data.series._3d.set_sample(m_id,frame, {'position':value, 'residual':residual})
                    value[0] = value[0] + velocity[0]
                    value[1] = value[1] + velocity[1]
                    value[2] = value[2] + velocity[2]

                    
# constantValue not True means to use velocity
def _FillStartGap(constantValue: bool = True):

    mRange = qtm.gui.timeline.get_measured_range()
    start = mRange["start"]
    end = mRange["end"]

    selections = qtm.gui.selection.get_selections()
    for s in selections:
        m_id = s["id"]
        fullmarker = qtm.data.object.trajectory.get_label(m_id)
        velocity = [0.0,0.0,0.0]
        value = [0.0,0.0,0.0]
        if qtm.data.series._3d.get_sample(m_id,start):
            print(f"{fullmarker} has no start gap")
        else:
            frame = start + 1
            valueFound = False
            gapEnd = 0
            while not valueFound:
                frameData = qtm.data.series._3d.get_sample(m_id,frame)
                if frameData:
                    valueFound = True
                    beginValue = frameData["position"]
                    velocity = [0.0,0.0,0.0]
                    residual = frameData["residual"]
                    gapEnd = frame - 1
                    if not constantValue:
                        frameData = qtm.data.series._3d.get_sample(m_id,frame+1)
                        if frameData:
                            value = frameData["position"]
                            velocity[0] = beginValue[0] - value[0]
                            velocity[1] = beginValue[1] - value[1]
                            velocity[2] = beginValue[2] - value[2]
                        else:
                            print(f"{fullmarker} Can not compute velocity")
                frame = frame + 1
                if frame > end:
                    print(f"Whoa! No data at all for {fullmarker}!")
                    return
            if valueFound:
                print(f"{fullmarker} end range: ({start},{gapEnd})  Value is {beginValue} Velocity is {velocity}")
                value[0] = beginValue[0] + velocity[0]
                value[1] = beginValue[1] + velocity[1]
                value[2] = beginValue[2] + velocity[2]
                frame = gapEnd
                while frame >= start:
                    qtm.data.series._3d.set_sample(m_id,frame, {'position':value, 'residual':residual})
                    value[0] = value[0] + velocity[0]
                    value[1] = value[1] + velocity[1]
                    value[2] = value[2] + velocity[2]
                    frame = frame - 1

def _trim(id,start,end,xframes):
    #print(f"_trim: start{start} end {end}")
    s = start - xframes
    e = start -1
    qtm.data.series._3d.delete_samples(id, {"start":s,"end":e})
    s = end + 1
    e = end + xframes
    qtm.data.series._3d.delete_samples(id, {"start":s,"end":e})

# - - - - - - - - - - - - - - - - - -
# ////////   P U B L I C   ////////
# - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]

def gap_trim(xframes : int = 1):
    """
    Trim the gaps of selected markers.  
    This means deleting some number of frames at the beginning 
    and end of gaps to get rid of translations that happen when 
    a marker gers occluded.
    :param xframes: integer
    """

    if qtm.gui.selection.get_selection_count() == 0:
        print(f"GapTrim: Nothing selected")
        return
    selections = qtm.gui.selection.get_selections()
    for s in selections:
        t = s["type"]
        if t != 'trajectory':
            print(f"How did you pick something other than a trajectory?")
            return
        id = s["id"]
        name = qtm.data.object.trajectory.get_label(id)
        #print(f"Selected marker: {name}")
        gaps = qtm.data.series._3d.get_gap_ranges(id)
        for g in gaps:
            start = g["start"]
            end = g["end"]
            _trim(id,start,end,xframes)
def gap_trim2():
    gap_trim(2)


def FillEndGapConstantValue():
    _FillEndGap(True)

def FillEndGapConstantVelocity():
    _FillEndGap(False)

def FillStartGapConstantValue():
    _FillStartGap(True)

def FillStartGapConstantVelocity():
    _FillStartGap(False)

def FillGapsSelected():
    if qtm.gui.selection.get_selection_count() == 0:
        print(f"Select which markers to fill.")
        return 
    strPass = "First Pass"
    i = 1
    for r in Arel:
        print(f"# Definition {i}: {strPass}")
        _doFillGapsSelected(r)
        i = i+1
    strPass = "Second Pass"
    i = 1
    for r in Arel:
        print(f"# Definition {i}: {strPass}")
        _doFillGapsSelected(r)
        i = i+1

def FillGapsSelected1():
    _doFillGapsSelected(Arel[0])
def FillGapsSelected2():
    _doFillGapsSelected(Arel[1])

def PrintGaps():
    markerset, marker = get_default_markerset_marker()
    if markerset:
        _print_gaps(markerset)
menu_priority = 1

def add_menu():

    add_command("gap_fill_relational_selected", FillGapsSelected)
    add_command("gap_fill_relational_definition1", FillGapsSelected1)
    add_command("gap_fill_relational_definition2", FillGapsSelected2)
    add_command("gap_fill_trim_gaps", gap_trim)
    add_command("gap_fill_trim_gaps2", gap_trim2)
    add_command("gap_fill_start_gap_constant_value", FillStartGapConstantValue)
    add_command("gap_fill_start_gap_constant_velocity", FillStartGapConstantVelocity)
    add_command("gap_fill_end_gap_constant_value", FillEndGapConstantValue)
    add_command("gap_fill_end_gap_constant_velocity", FillEndGapConstantVelocity)
    add_command("gap_fill_print_all_gaps", PrintGaps)
    add_command("gap_fill_help", lambda:(print(__doc__)))

    menu_id = qtm.gui.insert_menu_submenu(None,"GapFill")
    add_menu_item(menu_id, "Help", "gap_fill_help")
    qtm.gui.insert_menu_separator(menu_id)    
    add_menu_item(menu_id, "Relational Gap Fill - Multi Pass", "gap_fill_relational_selected")
    add_menu_item(menu_id, "Relational Gap Fill - One Pass Definition 1", "gap_fill_relational_definition1")
    add_menu_item(menu_id, "Relational Gap Fill - One Pass Definition 2", "gap_fill_relational_definition2")
    qtm.gui.insert_menu_separator(menu_id)
    add_menu_item(menu_id, "Trim Gaps by 1", "gap_fill_trim_gaps")
    add_menu_item(menu_id, "Trim Gaps by 2", "gap_fill_trim_gaps2")
    qtm.gui.insert_menu_separator(menu_id)
    add_menu_item(menu_id, "Fill Start Gap Constant Value", "gap_fill_start_gap_constant_value")
    add_menu_item(menu_id, "Fill Start Gap Constant Velocity", "gap_fill_start_gap_constant_velocity")
    add_menu_item(menu_id, "Fill End Gap Constant Value", "gap_fill_end_gap_constant_value")
    add_menu_item(menu_id, "Fill End Gap Constant Velocity", "gap_fill_end_gap_constant_velocity")
    qtm.gui.insert_menu_separator(menu_id)
    add_menu_item(menu_id, "Print All Gaps", "gap_fill_print_all_gaps")
# endregion

if __name__ == "__main__":
    add_menu()