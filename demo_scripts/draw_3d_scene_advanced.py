import Classes.custom_3d_scene_class
from helpers.printing import try_print_except
import importlib
import qtm


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _reload_script_modules():
    # Python's default behaviour is to cache imported scripts. This
    # means that changes you make to these scripts will not show up in
    # QTM despite pressing the "Reload scripts" button. However, running
    # "importlib.reload()" on these scripts will force Python to reload them.
    importlib.reload(Classes.custom_3d_scene_class)
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E X P O R T E D   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def update_and_draw_scene(measurement_time):
    try:
        custom_3d_scene_instance.update_and_draw_advanced(measurement_time)
    except Exception as e:
        try_print_except(str(e))


def update_and_draw_arrows_unlabeled_traj(measurement_time):
    try:
        custom_3d_scene_instance.update_and_draw_arrows_unlabeled_traj(measurement_time)
    except Exception as e:
        try_print_except(str(e))


def update_and_draw_decaying_arrows_unlabeled_traj(measurement_time):
    try:
        custom_3d_scene_instance.update_and_draw_decaying_arrows_unlabeled_traj(measurement_time)
    except Exception as e:
        try_print_except(str(e))
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E N T R Y   P O I N T (local 'main')   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
_reload_script_modules()
custom_3d_scene_instance = Classes.custom_3d_scene_class.custom_3d_scene()
