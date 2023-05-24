from vector import Vec3
import menu_tools as tools
import qtm



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def _calc_marker_speed(id, sample_index, dt):
    sample_prev = None
    sample_next = None
    sample_curr = qtm.data.series._3d.get_sample(id, sample_index)

    if sample_curr is None:
        return 0  # E A R L Y   E X I T

    if sample_index != 0:
        sample_prev = qtm.data.series._3d.get_sample(id, sample_index - 1)
    if sample_index != qtm.data.series._3d.get_sample_range(id)['end']:
        sample_next = qtm.data.series._3d.get_sample(id, sample_index + 1)

    if sample_prev is None and sample_next is None:
        return 0  # E A R L Y   E X I T

    position_curr = sample_curr["position"]
    velocity_prev = [0.0, 0.0, 0.0]
    velocity_next = [0.0, 0.0, 0.0]
    speed_prev = 0
    speed_next = 0

    if sample_prev:
        position_prev = sample_prev["position"]
        velocity_prev = Vec3(position_curr) - Vec3(position_prev)
        speed_prev = velocity_prev.magnitude() / dt
    if sample_next:
        position_next = sample_next["position"]
        velocity_next = Vec3(position_next) - Vec3(position_curr)
        speed_next = velocity_next.magnitude() / dt

    if sample_prev is not None and sample_next is not None:
        return ((speed_prev + speed_next) * 0.5)
    elif sample_prev is not None:
        return speed_prev
    else:
        return speed_next


def _calc_marker_acceleration(id, sample_index, dt):
    sample_prev = None
    sample_next = None
    sample_curr = None
    sample_curr = qtm.data.series._3d.get_sample(id, sample_index)

    if sample_curr is None:
        return 0  # E A R L Y   E X I T

    if sample_index != 0:
        sample_prev = qtm.data.series._3d.get_sample(id, sample_index - 1)
    else:
        sample_prev = sample_curr
    if sample_index != qtm.data.series._3d.get_sample_range(id)['end']:
        sample_next = qtm.data.series._3d.get_sample(id, sample_index + 1)
    else:
        sample_next = sample_curr
    if sample_prev is None or sample_next is None:
        return 0  # E A R L Y   E X I T

    p1 = sample_curr["position"]
    p2 = sample_curr["position"]
    p3 = sample_curr["position"]

    if sample_index != 0:
        p1 = sample_prev["position"]
    if sample_index != qtm.data.series._3d.get_sample_range(id)['end']:
        p3 = sample_next["position"]

    return tools.calculate_acceleration(p1, p2, p3, dt).magnitude()
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E X P O R T E D   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
def get_marker_counts_three():
    total_count = 0
    labeled_count = 0
    unlabeled_count = 0

    all_traj_ids = qtm.data.series._3d.get_series_ids()
    for id in all_traj_ids:
        total_count += 1
        if qtm.data.object.trajectory.get_label(id) is not None:
            labeled_count += 1

    unlabeled_count = total_count - labeled_count
    return (total_count, labeled_count, unlabeled_count)


def get_labeled_marker_ids():
    all_traj_ids = qtm.data.series._3d.get_series_ids()
    return [id for id in all_traj_ids if qtm.data.object.trajectory.get_label(id) is not None]


def get_unlabeled_marker_ids():
    all_traj_ids = qtm.data.series._3d.get_series_ids()
    return [id for id in all_traj_ids if qtm.data.object.trajectory.get_label(id) is None]


def get_marker_positions(measurement_time, marker_ids, include_none_values=False):
    return_list = []
    for id in marker_ids:
        index = qtm.data.series._3d.get_sample_index_at_time(id, measurement_time)
        curr_marker = qtm.data.series._3d.get_sample(id, index)
        if curr_marker != None:
            return_list.append(curr_marker["position"])
        elif include_none_values:
            return_list.append(None)
    return return_list


def calc_avg_residual(list_of_marker_ids, measurement_time):
    if len(list_of_marker_ids) == 0:
        return 0  # E A R L Y   E X I T

    sum_of_residuals = 0

    for id in list_of_marker_ids:
        sample_index = qtm.data.series._3d.get_sample_index_at_time(id, measurement_time)
        curr_traj_curr_sample_data = qtm.data.series._3d.get_sample(id, sample_index)
        if curr_traj_curr_sample_data is not None:
            sum_of_residuals += curr_traj_curr_sample_data['residual']

    return (sum_of_residuals / len(list_of_marker_ids))


def calc_avg_speed(list_of_marker_ids, measurement_time):
    if len(list_of_marker_ids) == 0:
        return 0  # E A R L Y   E X I T

    sum_of_speeds = 0

    for id in list_of_marker_ids:
        sample_index = qtm.data.series._3d.get_sample_index_at_time(id, measurement_time)
        # Freq is reciprocal of dt
        dt = 1.0 / qtm.data.series._3d.get_frequency(id)
        # Convert millimeters to meters
        sum_of_speeds += _calc_marker_speed(id, sample_index, dt) / 1000.0

    return (sum_of_speeds / len(list_of_marker_ids))


def calc_avg_acceleration(list_of_marker_ids, measurement_time):
    if len(list_of_marker_ids) == 0:
        return 0  # E A R L Y   E X I T

    sum_of_accelerations = 0

    for id in list_of_marker_ids:
        sample_index = qtm.data.series._3d.get_sample_index_at_time(id, measurement_time)
        # Freq is reciprocal of dt
        dt = 1.0 / qtm.data.series._3d.get_frequency(id)
        # Convert millimeters to meters
        sum_of_accelerations += _calc_marker_acceleration(id, sample_index, dt) / 1000.0

    return (sum_of_accelerations / len(list_of_marker_ids))

def get_selected_markerset_marker(noisy = False):
    """
    Convenience function to return the currently selected marker and its
    markerset.
    """
    if qtm.gui.selection.get_selection_count() == 0:
        if noisy:
            print(f"Select a marker in the markerset.")
        return None, None
    selections = qtm.gui.selection.get_selections()
    s = selections[0]
    id = s["id"]
    try:
        fullname = qtm.data.object.trajectory.get_label(id)
    except:
        return None,None

    if not fullname:
        print(f"An unnamed marker is selected.")
        return None, None
    if not "_" in fullname:
        print(f"Selected marker is not in a markerset.")
        return None, None
    s = fullname.split("_",1)
    markersetname = s[0]
    markername = s[1]

    return markersetname, markername

def get_default_markerset_marker():
    """
    Return the selected marker and markerset.  If one isn't
    selected, find the first marker in a markerset and return
    that one.
    """
    markerset, marker = get_selected_markerset_marker()
    if markerset:
        return markerset, marker
    try:
        seriesIDs = qtm.data.series._3d.get_series_ids()
    except:
        print(f"No measurement")
        return None, None

    for id in seriesIDs:
        fullname = qtm.data.object.trajectory.get_label(id)
        if fullname:
            if "_" in fullname:
                s = fullname.split("_",1)
                return s[0], s[1]
    return None, None

# endregion
