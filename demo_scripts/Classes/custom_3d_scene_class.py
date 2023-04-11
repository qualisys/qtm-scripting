from tools.helpers.tools import clamp
from tools.helpers.traj import get_marker_positions, get_unlabeled_marker_ids
from tools.helpers.matrix import Mat4x4
import sys
import os
import inspect
import shutil
import datetime
import math
import qtm


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   C L A S S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
class custom_3d_scene:
    # - - - - - - - - - - - - - - - - - - -
    # ////////   P R I V A T E   ////////
    # - - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def __init__(self):
        # constants
        self._red = qtm.utilities.color.rgb(1.0, 0.0, 0.0)
        self._green = qtm.utilities.color.rgb(0.0, 1.0, 0.0)
        self._blue = qtm.utilities.color.rgb(0.0, 0.0, 1.0)
        self._white = qtm.utilities.color.rgb(1.0, 1.0, 1.0)
        self._orange_from_hsl = qtm.utilities.color.hsl(20, 1.0, 0.5)
        # variables
        self._prev_time = datetime.datetime.now()
        self._sphere_max_height = 3000.0
        self._sphere_travel_distance = 0.0
        self._sphere_travel_switch = True
        self._hovering_arrow_positions_dict = {}

    def _draw_rainbow_arrows_field(self, measurement_time, count, total_length, max_height):
        step_distance = total_length / count
        curr_x = total_length * 0.5
        curr_y = total_length * 0.5

        wave_speed = measurement_time * 0.005
        color_variator = measurement_time * 0.8
        wave_freq_x = 0.5
        wave_freq_y = 0.40

        for index_y in range(count):
            for index_x in range(count):
                curr_arrow_color = qtm.utilities.color.hsl(abs(math.sin(((index_x + index_y) + color_variator))) * 255, 1.0, 0.5)
                qtm.gui._3d.draw_arrow([curr_x, curr_y, 0], [curr_x, curr_y, abs(math.sin((index_x * wave_freq_x + index_y * wave_freq_y + wave_speed) * step_distance)) * max_height], curr_arrow_color)
                # Step once, x-axis
                curr_x -= step_distance
            # Step once, y-axis
            curr_y -= step_distance
            # Reset
            curr_x = total_length * 0.5

    def _draw_bouncing_spheres(self, measurement_time, radius, weight, distance_from_center, travel_speed):
        curr_time = datetime.datetime.now()
        dt = curr_time - self._prev_time
        self._prev_time = curr_time

        # NOTE: Using dt to calculate height incurs a risk of the spheres disappearing from
        #       the scene since it continues to update even when the measurement is paused.
        self._sphere_height = self._sphere_max_height * abs((math.sin(measurement_time * weight)))

        if self._sphere_travel_distance < 1.0 and self._sphere_travel_switch:
            self._sphere_travel_switch = True
            self._sphere_travel_distance += travel_speed * dt.total_seconds()
        elif self._sphere_travel_distance > 0.0:
            self._sphere_travel_switch = False
            self._sphere_travel_distance -= travel_speed * dt.total_seconds()
        else:
            self._sphere_travel_switch = True

        # Guard against spheres leaving area during pause of measurement
        if self._sphere_travel_distance > 1.0:
            self._sphere_travel_distance = 1.0
        elif self._sphere_travel_distance < 0.0:
            self._sphere_travel_distance = 0.0

        qtm.gui._3d.draw_sphere([distance_from_center-(distance_from_center*2*self._sphere_travel_distance), distance_from_center, self._sphere_height], radius, self._red)
        qtm.gui._3d.draw_sphere([-distance_from_center, distance_from_center-(distance_from_center*2*self._sphere_travel_distance), self._sphere_height], radius, self._green)
        qtm.gui._3d.draw_sphere([distance_from_center, -distance_from_center+(distance_from_center*2*self._sphere_travel_distance), self._sphere_height], radius, self._blue)
        qtm.gui._3d.draw_sphere([-distance_from_center+(distance_from_center*2*self._sphere_travel_distance), -distance_from_center, self._sphere_height], radius, self._orange_from_hsl)

    def _draw_hovering_arrows(self, measurement_time, positions, arrow_length, color, hover_distance, hover_speed):
        for pos in positions:
            hover_val = clamp(abs(math.sin(measurement_time * hover_speed)), 0.0, 1.0) * hover_distance
            qtm.gui._3d.draw_arrow([pos[0], pos[1], pos[2] + arrow_length + hover_val], [pos[0], pos[1], pos[2] + hover_val], color)

    def _draw_hovering_arrows_with_decay(self, measurement_time, marker_ids, max_length, color, hover_distance, hover_speed, lifetime_in_frames):
        # Need marker IDs to keep track of arrows, but we also need the positions
        marker_positions = get_marker_positions(measurement_time, marker_ids, include_none_values=True)
        # Update / Add arrows
        for i in range(len(marker_ids)):
            # NOTE: len(marker_positions) == len(marker_ids)
            if marker_positions[i] != None:
                self._hovering_arrow_positions_dict.update({marker_ids[i]:{"pos": marker_positions[i], "lifetime": lifetime_in_frames}})
        # Draw arrows
        hover_val = clamp(abs(math.sin(measurement_time * hover_speed)), 0.0, 1.0) * hover_distance
        keys_to_remove = []  # NOTE: 'keys' from key-value pair objects (one for each arrow)
        lifetime_divisor = 1 / lifetime_in_frames
        for arrow_as_dict_item in self._hovering_arrow_positions_dict.items():
            pos = arrow_as_dict_item[1]["pos"]
            arrow_length = (max_length * arrow_as_dict_item[1]["lifetime"] * lifetime_divisor)
            qtm.gui._3d.draw_arrow([pos[0], pos[1], pos[2] + arrow_length + hover_val], [pos[0], pos[1], pos[2] + hover_val], color)
            arrow_as_dict_item[1]["lifetime"] -= 1
            if arrow_as_dict_item[1]["lifetime"] == 0:
                keys_to_remove.append(arrow_as_dict_item[0])
        # Remove arrows with '0' lifetime
        for key in keys_to_remove:
            del self._hovering_arrow_positions_dict[key]

    def _draw_arrows(self):
        # Draw an arrow between the two given 3D positions with the default color (white)
        qtm.gui._3d.draw_arrow([0, 2000, 0], [0, 2000, 1000])
        # Draw another shorter arrow next to the first one with the color red
        qtm.gui._3d.draw_arrow([0, 2500, 0], [0, 2500, 500], self._red)

    def _draw_spheres(self):
        # Draw a sphere at the given 3D position, with the given radius, with the default color (white)
        qtm.gui._3d.draw_sphere([0, -2000, 1500], 400)
        # Draw another sphere under the first one with the color red
        qtm.gui._3d.draw_sphere([0, -2000, 750], 200, self._red)

    def _draw_axis(self):
        # Create matrix defining the position at which the axes should be moved to
        translation_matrix = Mat4x4.create_translation_matrix([2000.0, 0.0, 1000.0])
        # Draw a 3-dimensional axis using the 'translation_matrix' to determine its position
        # NOTE: x_axis == red arrow, y_axis == green arrow, z_axis == blue arrow (as depicted in QTM)
        qtm.gui._3d.draw_axes(list(translation_matrix), 1000)

    def _draw_mesh(self):
        # NOTE: If you're not able to see your mesh (and no exception is being thrown),
        #       it is likely because the format (presumably the faces) is not as QTM is expecting.
        #       Here is one step-by-step alternative as to how you can reformat your obj:
        #   1. Download Blender (free and open source software)
        #   2. Open an empty project, delete default starting objects (collection, camera, cube, light, etc.)
        #   3. In the top menu bar, click on 'File' --> 'Import' --> 'Wavefront (.obj)' and find your mesh
        #   4. Select your object (typically left-click) and then click on 'UV Editing' in the top menu bar
        #   5. Hover the mouse over the object, then first press 'A', then press 'U', and then click on 'Unwrap'
        #   6a. In the top menu bar, click on 'File' --> 'Export' --> 'Wavefront (.obj)(legacy)'
        #   6b. 'File' --> 'Export' --> 'Wavefront (.obj)' should also work.

        # NOTE #1: Your mesh must exist in the 'Meshes' directory in your project folder.
        # NOTE #2: Your mesh filename can not contain a '_' (there are possibly other illegal special characters)
        dst_path = str(qtm.settings.directory.get_project_directory() + "\\Meshes")
        # If 'utah-teapot.obj' is not in the 'Meshes' (destination path) directory...
        if not os.path.isfile(dst_path + "\\utah-teapot.obj"):
            src_path = os.path.abspath(inspect.getfile(inspect.currentframe())).rsplit("\\", 2)[0] + "\\models"
            # ...then we copy and move it to 'Meshes' from 'qtm\models\other' (source directory)
            shutil.copy(src_path + "\\utah-teapot.obj", dst_path)
            print("Created the 'utah-teapot.obj' model at the following location in the project: " + dst_path)

        # Create matrix defining how the mesh should be rotated (180 degrees --> upside down)
        rotation_matrix = Mat4x4.create_rotation_matrix(math.radians(180.0), 0.0, 0.0)
        # Create matrix defining the position at which the mesh should be moved to
        translation_matrix = Mat4x4.create_translation_matrix([-2000, 0, 1500])
        # NOTE: The order of which the translation & rotation matrices are multiplied matters
        tran_rot_matrix = translation_matrix * rotation_matrix
        # Load the 'utah-teapot.obj' mesh, scaled by the given ratio
        qtm.gui._3d.draw_mesh(list(tran_rot_matrix), 1.5, "utah-teapot.obj")
    # endregion

    # - - - - - - - - - - - - - - - - - -
    # ////////   P U B L I C   ////////
    # - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def update_and_draw_advanced(self, measurement_time):
        self._draw_rainbow_arrows_field(measurement_time, 10, 10000, 800)
        self._draw_bouncing_spheres(measurement_time, 200, 2, 5000, 0.25)

    def update_and_draw_basic(self):
        # For 3D objects, the calling order here does not matter. QTM will
        # draw the objects correctly based on order-of-depth (z-buffer).
        self._draw_arrows()
        self._draw_spheres()
        self._draw_axis()
        self._draw_mesh()

    def update_and_draw_arrows_unlabeled_traj(self, measurement_time):
        self._draw_hovering_arrows(measurement_time, get_marker_positions(measurement_time, get_unlabeled_marker_ids()), 2000.0, self._red, 200.0, 3.0)

    def update_and_draw_decaying_arrows_unlabeled_traj(self, measurement_time):
        self._draw_hovering_arrows_with_decay(measurement_time, get_unlabeled_marker_ids(), 2000.0, self._white, 200.0, 3.0, 20)
# endregion
