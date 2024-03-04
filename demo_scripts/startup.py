from io import StringIO
import sys
import os
import inspect
import importlib
# Set scripts 'path' to your repo location
# NOTE: This needs to be done before importing custom libraries
this_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if this_dir not in sys.path:
    sys.path.append(this_dir)
import qtm

from helpers.printing import try_print_except
from helpers.menu_tools import add_command 

try:
    import draw_overlay_advanced
    import draw_3d_scene_advanced
    import draw_overlay_basic
    import draw_3d_scene_basic
    import custom_menu_bar
except ModuleNotFoundError as e:
    try_print_except(str(e), "Press 'Reload scripts' to try again.")
# variables
_is_menu_bar_advanced = False
_is_drawing_3d_scene_basic = False
_is_drawing_3d_scene_advanced = False
_is_drawing_arrows_unlabeled_traj = False
_is_drawing_decaying_arrows_unlabeled_traj = False
_is_drawing_overlay_basic = False
_is_drawing_overlay_advanced = False
_help_root_topics = []


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _reload_script_modules():

    # Python's default behaviour is to cache imported scripts. This
    # means that changes you make to these scripts will not show up in
    # QTM despite pressing the "Reload scripts" button. However, running
    # "importlib.reload()" on these scripts will force Python to reload them.
    importlib.reload(draw_overlay_advanced)
    importlib.reload(draw_3d_scene_advanced)
    importlib.reload(draw_overlay_basic)
    importlib.reload(draw_3d_scene_basic)
    importlib.reload(custom_menu_bar)


def _update_and_draw_callbacks(measurement_time):
    # You can set exactly one callback function for drawing in the 3D scene
    # (setting a new one replaces the old one). This callback is continuously
    # invoked as QTM runs. Although this callback is mainly for updating
    # logic & drawing, you're free to do more as long as it's within this function.

    # This function must receive the 'measurement_time' variable.

    # The draw order between Overlay(2D) and 3D matters; make sure to draw
    # the overlay after the 3D objects. On the contrary, the draw order of
    # the 3D objects does not matter as this is handled internally by QTM.

    # 3D
    if globals()["_is_drawing_3d_scene_basic"]:
        draw_3d_scene_basic.update_and_draw_scene()
    if globals()["_is_drawing_3d_scene_advanced"]:
        draw_3d_scene_advanced.update_and_draw_scene(measurement_time)
    if globals()["_is_drawing_decaying_arrows_unlabeled_traj"]:
        draw_3d_scene_advanced.update_and_draw_decaying_arrows_unlabeled_traj(measurement_time)
    if globals()["_is_drawing_arrows_unlabeled_traj"]:
        draw_3d_scene_advanced.update_and_draw_arrows_unlabeled_traj(measurement_time)
    # Overlay
    if globals()["_is_drawing_overlay_basic"]:
        draw_overlay_basic.update_and_draw_overlay(measurement_time)
    if globals()["_is_drawing_overlay_advanced"]:
        draw_overlay_advanced.update_and_draw_overlay(measurement_time)


def _toggle_menu_script_example():
    try:
        if globals()["_is_menu_bar_advanced"]:
            globals()["_is_menu_bar_advanced"] = False
            globals()["_is_drawing_3d_scene_advanced"] = False
            globals()["_is_drawing_overlay_advanced"] = False
            globals()["_is_drawing_arrows_unlabeled_traj"] = False
            globals()["_is_drawing_decaying_arrows_unlabeled_traj"] = False
            custom_menu_bar.delete()
            custom_menu_bar.setup_basic()
        else:
            globals()["_is_menu_bar_advanced"] = True
            globals()["_is_drawing_3d_scene_basic"] = False
            globals()["_is_drawing_overlay_basic"] = False
            custom_menu_bar.delete()
            custom_menu_bar.setup_advanced()
    except Exception as e:
        try_print_except(str(e), "Press 'Reload scripts' to try again.")


def _toggle_3d_scene_basic():
    globals()["_is_drawing_3d_scene_basic"] = not globals()["_is_drawing_3d_scene_basic"]


def _toggle_3d_scene_advanced():
    globals()["_is_drawing_3d_scene_advanced"] = not globals()["_is_drawing_3d_scene_advanced"]


def _toggle_drawing_arrows_unlabeled_traj():
    globals()["_is_drawing_arrows_unlabeled_traj"] = not globals()["_is_drawing_arrows_unlabeled_traj"]


def _toggle_drawing_decaying_arrows_unlabeled_traj():
    globals()["_is_drawing_decaying_arrows_unlabeled_traj"] = not globals()["_is_drawing_decaying_arrows_unlabeled_traj"]


def _toggle_overlay_basic():
    globals()["_is_drawing_overlay_basic"] = not globals()["_is_drawing_overlay_basic"]


def _toggle_overlay_advanced():
    globals()["_is_drawing_overlay_advanced"] = not globals()["_is_drawing_overlay_advanced"]


def _capture_help_output():
    old_stdout = sys.stdout # Store original stdout
    new_stdout = StringIO() # Capture output into string buffer
    sys.stdout = new_stdout
    help()
    sys.stdout = old_stdout  # Restore original stdout
    return new_stdout.getvalue()


def _parse_help_output(output):
    topics = []
    for line in output.splitlines():
        if '|' in line and 'Topic' not in line:
            topic = line.split('|')[1].strip()
            topic = topic.strip('"')  # Remove quotation marks from found 'topics' 
            topics.append(topic)
    return topics


def _get_help_root_topics():
    help_output = _capture_help_output()
    return _parse_help_output(help_output)


def _add_help_root_commands():
    help_root_topics = _get_help_root_topics()
    for curr_root_topic in help_root_topics:
        add_command(("help_root_" + curr_root_topic), lambda topic=curr_root_topic: (print("\n\n\n"), help(topic)))


def _setup_menu_commands():
    add_command("toggle_menu_script_example", lambda: (_toggle_menu_script_example()))
    add_command("toggle_3d_scene_basic", lambda: (_toggle_3d_scene_basic()))
    add_command("toggle_3d_scene_advanced", lambda: (_toggle_3d_scene_advanced()))
    add_command("toggle_drawing_arrows_unlabeled_traj", lambda: (_toggle_drawing_arrows_unlabeled_traj()))
    add_command("toggle_drawing_decaying_arrows_unlabeled_traj", lambda: (_toggle_drawing_decaying_arrows_unlabeled_traj()))
    add_command("toggle_overlay_basic", lambda: (_toggle_overlay_basic()))
    add_command("toggle_overlay_advanced", lambda: (_toggle_overlay_advanced()))
    _add_help_root_commands()
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E N T R Y   P O I N T (local 'main')   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def add_menu():
    try:
        _reload_script_modules()
        print("Modules loaded.")
        # Set callback for drawing in the OpenGL window
        qtm.gui._3d.set_draw_function(_update_and_draw_callbacks)
        # Setup menu commands
        _setup_menu_commands()
        # Setup menu bar
        custom_menu_bar.setup_basic()
    except Exception as e:
        try_print_except(str(e), "Press 'Reload scripts' to try again.")

if __name__ == '__main__':
    add_menu()
