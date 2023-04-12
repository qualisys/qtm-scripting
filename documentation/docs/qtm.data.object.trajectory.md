# qtm.data.object.trajectory

Access and modify trajectories.

## add_trajectory

Add a trajectory.

**Parameters**

`label` `string?`<br/>
The label of the trajectory (if null, the trajectory will be unidentified).


**Returns**

`integer` The identifier of the added trajectory.


---
## delete_trajectory

Delete a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.




---
## smooth_trajectory

Smooth a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`algorithm` `"moving_average"|"butterworth"?`<br/>
The smooth algorithm to use (if null, moving average will be used).

`range` `{"start": integer, "end": integer}?`<br/>
The sample index range to smooth (if null, entire trajectory will be smoothed).

`settings` `{"window_size": integer?, "filter_order": integer?, "cutoff_frequency": float?}?`<br/>
The smooth settings to use (if null, or if any individual setting is null, the following default values will be used: {window_size: 5, filter_order: 4, cutoff_frequency: 10.0}).




---
## fill_trajectory

Fill a trajectory.

All samples within the given range will be overwritten. To fill gaps only, use the ranges returned by 'qtm.data.series._3d.get_gap_ranges'.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`algorithm` `"static"|"linear"|"polynomial"|"relational"|"virtual"|"kinematic"?`<br/>
The fill algorithm to use (if null, polynomial will be used).

`range` `{"start": integer, "end": integer}?`<br/>
The sample index range to fill (if null, the entire measurement range will be filled).

`settings` `{"origin": integer?, "line": integer?, "plane": integer?, "offset": vec3f?, "is_rigid_body": bool?, "is_relative_offset": bool?}?`<br/>
The fill settings to use (if null, or if any individual setting is null, the following default values will be used: {offset: [0.0, 0.0, 0.0], is_rigid_body: false, is_relative_offset: false}).




---
## find_trajectory

Find a trajectory by label.

**Parameters**

`label` `string`<br/>
The label of the trajectory.


**Returns**

`integer?` The identifier of the found trajectory (or null, if no trajectory was found).


---
## clear_trajectories

Remove all trajectories.



---
## get_part

Get a part of a trajectory by index.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`index` `integer`<br/>
The index of the part.


**Returns**

`{"range": {"start": integer, "end": integer}, "type": string}` 


---
## get_parts

Get all parts of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`[{"range": {"start": integer, "end": integer}, "type": string}]` 


---
## get_part_count

Get the number of parts of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer` 


---
## delete_parts

Delete parts of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`part_indices` `[integer]?`<br/>
The indices of the parts to delete (if null, all parts will be deleted).




---
## move_parts

Move parts from one trajectory to another.

**Parameters**

`id_from` `integer`<br/>
The identifier of the trajectory to move from.

`id_to` `integer`<br/>
The identifier of the trajectory to move to.

`part_indices` `[integer]?`<br/>
The indices of the parts to move (if null, all parts will be moved).




---
## swap_parts

Swap parts between two trajectories.

**Parameters**

`id_1` `integer`<br/>
The identifier of the first trajectory.

`id_2` `integer`<br/>
The identifier of the second trajectory.

`part_indices_1` `[integer]?`<br/>
The indices of the parts to swap from the first trajectory (if null, all parts will be swapped).

`part_indices_2` `[integer]?`<br/>
The indices of the parts to swap from the second trajectory (if null, all parts will be swapped).




---
## split_part

Split a part of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`sample_index` `integer`<br/>
The index of the last sample before the split.




---
## get_label

Get the label of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`string?` The label (or null, if the trajectory is unidentified).


---
## set_label

Set the label of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`label` `string?`<br/>
The label (if null, the trajectory will become unidentified).




---
## get_active_marker_id

Get the (sequence coded) active marker identifier of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The active marker identifier (or null, if the marker is passive or actively unidentified).


---
## get_rigid_body_id

Get the rigid body identifier of a trajectory.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The identifier of the rigid body (or null, if the trajectory isn't part of a rigid body).


---
## get_skeleton_segment_id

Get the skeleton segment identifier of a trajectory.

If the trajectory is attached to multiple segments, only the identifier of the first found will be returned.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The identifier of the skeleton segment (or null, if the trajectory isn't part of a skeleton).


---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
