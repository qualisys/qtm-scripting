from helpers import traj, selection
import qtm


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   C L A S S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
class custom_overlay:
    # - - - - - - - - - - - - - - - - - - -
    # ////////   P R I V A T E   ////////
    # - - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def __init__(self):
        # constants
        self._grey = qtm.utilities.color.rgb(0.65, 0.65, 0.65)
        self._green = qtm.utilities.color.rgb(0.0, 1.0, 0.0)
        self._red = qtm.utilities.color.rgb(1.0, 0.0, 0.0)
        self._blue = qtm.utilities.color.rgb(0.0, 0.6, 0.9)
        self._yellow = qtm.utilities.color.rgb(0.92, 0.92, 0.31)
        self._update_periodicity = 5.0
        self._hsl_hue_update_speed = 50.0
        # variables
        self._accumulated_dt = 0.0
        self._total_count = 0
        self._labeled_count = 0
        self._unlabeled_count = 0
        self._selected_markers_count = 0
        self._selected_bones_count = 0
        self._avg_residual_labeled = 0.0
        self._avg_speed_labeled = 0.0
        self._avg_acc_labeled = 0.0
        self._avg_residual_selected = 0.0
        self._avg_speed_selected = 0.0
        self._avg_acceleration_selected = 0.0

    @staticmethod
    def _create_str_timestamp(measurement_time):
        return ("Timestamp: " + str(measurement_time))

    def _create_str_total_markers(self):
        return ("Total Markers: " + str(self._total_count))

    def _create_str_labeled_markers(self):
        return ("Labeled Markers: " + str(self._labeled_count))

    def _create_str_unlabeled_markers(self):
        return ("Unlabeled Markers: " + str(self._unlabeled_count))

    def _create_str_selected_markers(self):
        return ("Selected Markers: " + str(self._selected_markers_count))

    def _create_str_selected_bones(self):
        return ("Selected Bones: " + str(self._selected_bones_count))

    def _create_str_averages_labeled_markers(self):
        return_string = f"Avg. Residual (m): {self._avg_residual_labeled:.2f}\n"
        return_string += f"Avg. Speed (m/s): {self._avg_speed_labeled:.2f}\n"
        return_string += f"Avg. Acceleration (m/s/s): {self._avg_acc_labeled:.2f}"
        return return_string

    def _create_str_averages_selected_markers(self):
        return_string = f"Avg. Residual (m): {self._avg_residual_selected:.2f}\n"
        return_string += f"Avg. Speed (m/s): {self._avg_speed_selected:.2f}\n"
        return_string += f"Avg. Acceleration (m/s/s): {self._avg_acceleration_selected:.2f}"
        return return_string

    @staticmethod
    def _create_str_hyphens(count, spacing=0):
        result = ''
        for _ in range(count):
            result += '-'
            for _ in range(spacing):
                result += ' '
        return result
    # endregion

    # - - - - - - - - - - - - - - - - - -
    # ////////   P U B L I C   ////////
    # - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def draw_advanced(self, measurement_time):
        qtm.gui._3d.draw_text_2d([50, 20], 10, self._create_str_timestamp(measurement_time), None, {"horizontal": "left", "vertical": "top"}, self._red)
        qtm.gui._3d.draw_text_2d([50, 38], 10, self._create_str_total_markers(), {"horizontal": "left", "vertical": "top"}, {"horizontal": "left", "vertical": "top"})
        qtm.gui._3d.draw_text_2d([50, 56], 10, self._create_str_unlabeled_markers(), {"horizontal": "left", "vertical": "top"}, None, self._grey)
        qtm.gui._3d.draw_text_2d([50, 74], 10, self._create_str_selected_bones(), None, None, self._yellow)
        qtm.gui._3d.draw_text_2d([50, 110], 10, self._create_str_labeled_markers(), None, None, self._green)
        qtm.gui._3d.draw_text_2d([50, 118], 10, self._create_str_hyphens(31), None, None, self._green)
        qtm.gui._3d.draw_text_2d([64, 136], 10, self._create_str_averages_labeled_markers())
        qtm.gui._3d.draw_text_2d([50, 202], 10, self._create_str_selected_markers(), None, None, self._blue)
        qtm.gui._3d.draw_text_2d([50, 210], 10, self._create_str_hyphens(31), None, None, self._blue)
        qtm.gui._3d.draw_text_2d([64, 228], 10, self._create_str_averages_selected_markers())

    def update_advanced(self, measurement_time):
        # Average Residual, Speed, & Acceleration
        if self._accumulated_dt > self._update_periodicity:
            # reset dt
            self._accumulated_dt = 0
            # Marker counts
            self._total_count, self._labeled_count, self._unlabeled_count = traj.get_marker_counts_three()
            self._selected_markers_count = len(selection.get_selected_marker_ids())
            self._selected_bones_count = len(selection.get_selected_bone_ids())
            # Labeled markers
            self._avg_residual_labeled = traj.calc_avg_residual(traj.get_labeled_marker_ids(), measurement_time)
            self._avg_speed_labeled = traj.calc_avg_speed(traj.get_labeled_marker_ids(), measurement_time)
            self._avg_acc_labeled = traj.calc_avg_acceleration(traj.get_labeled_marker_ids(), measurement_time)
            # Selected Markers
            self._avg_residual_selected = traj.calc_avg_residual(selection.get_selected_marker_ids(), measurement_time)
            self._avg_speed_selected = traj.calc_avg_speed(selection.get_selected_marker_ids(), measurement_time)
            self._avg_acceleration_selected = traj.calc_avg_acceleration(selection.get_selected_marker_ids(), measurement_time)
        else:
            self._accumulated_dt += 1

    def draw_basic(self, measurement_time):
        # Arguments: Position, Size, Text, Origin(optional), Alignment(optional), Color(optional)
        #   The most basic version leaves out optional arguments, resulting in the following:
        #     - Origin is auto-set to the top-left corner ({"horizontal": "left", "vertical": "top"})
        #     - The alignment of the text is auto-set to top-left
        #     - The color is auto-set to white (0xffffff)

        str_1 = "50 pixels right / 20 pixels down from the top-left corner (size: 20)"
        qtm.gui._3d.draw_text_2d([50, 20], 20, str_1)

        str_2 = "50 pixels right / 440 pixels up from the bot-left corner (size: 18)"
        qtm.gui._3d.draw_text_2d([50, -440], 18, str_2, {"horizontal": "left", "vertical": "bottom"})

        str_3 = "1000 pixels left / 400 pixels up from the bot-right corner (size: 16)"
        qtm.gui._3d.draw_text_2d([-1000, -400], 16, str_3, {"horizontal": "right", "vertical": "bottom"})

        str_4 = "1000 pixels left / 140 pixels down from the top-right corner (size: 14)"
        qtm.gui._3d.draw_text_2d([-1000, 140], 14, str_4, {"horizontal": "right", "vertical": "top"})

        str_5 = "The center-most point within this block of text is 438p/186p down/right from the top-left corner"
        # NOTE: In this case 'None' == {"horizontal": "left", "vertical": "top"}
        qtm.gui._3d.draw_text_2d([438, 186], 14, str_5, None, {"horizontal": "center", "vertical": "center"})

        str_6 = "Resize This Window"
        qtm.gui._3d.draw_text_2d([0, 0], 18, str_6, {"horizontal": "center", "vertical": "center"}, {"horizontal": "center", "vertical": "center"}, qtm.utilities.color.rgb(1.0, 1.0, 0.0))

        str_7 = "This text is colored red using rgb: (255, 0, 0)"
        qtm.gui._3d.draw_text_2d([50, -75], 14, str_7, {"horizontal": "left", "vertical": "bottom"}, None, qtm.utilities.color.rgb(1.0, 0.0, 0.0))

        hsl_hue = (self._hsl_hue_update_speed * measurement_time) % 360
        str_8 = f"This text is colored using hsl with a varying hue value: ({int(hsl_hue)}, 100%, 65%)"
        qtm.gui._3d.draw_text_2d([50, -50], 14, str_8, {"horizontal": "left", "vertical": "bottom"}, None, qtm.utilities.color.hsl(hsl_hue, 1.0, 0.65))
    # endregion
