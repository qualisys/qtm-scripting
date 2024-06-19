# qtm.data.object.trajectory

Access and modify trajectories.

=== "Python"
    ``` py
    import qtm
    
    # - Create an empty labeled trajectory
    trajectory_label = "trajectory"
    trajectory_id = qtm.data.object.trajectory.add_trajectory(trajectory_label)
    
    # - Get measurement range
    measured_range = qtm.gui.timeline.get_measured_range()
    print(measured_range)
    # {'start': 0, 'end': 2999}
    
    # - Generate dummy 3d data
    dummy_3d_data = []
    for x_value in range(measured_range["start"], measured_range["end"]+1):
            dummy_3d_data.append({"position": [x_value, 1000.0, 1000.0], "residual": 0.0})
    
    # - Add generated 3d data to the trajectory
    qtm.data.series._3d.set_samples(trajectory_id, measured_range, dummy_3d_data)
    
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    # [{'range': {'start': 0, 'end': 2999}, 'type': 'virtual'}]
    
    # - Split the trajectory in 3 parts
    split_index_1 = 1200
    split_index_2 = 1300
    qtm.data.object.trajectory.split_part(trajectory_id, split_index_1)
    qtm.data.object.trajectory.split_part(trajectory_id, split_index_2)
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    # 3
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    # [{'range': {'start': 0, 'end': 1200}, 'type': 'virtual'}, {'range': ... ...
    
    # - Remove the middle part of the trajectory
    parts_to_remove_indices = [1]
    qtm.data.object.trajectory.delete_parts(trajectory_id, parts_to_remove_indices)
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    # 2
    
    # - Get the range of created gap
    gap_ranges = qtm.data.series._3d.get_gap_ranges(trajectory_id)
    print(gap_ranges)
    # [{'start': 1201, 'end': 1300}]
    
    # - Use fill_trajectory to fill the created gap
    fill_algorithm = "polynomial"
    qtm.data.object.trajectory.fill_trajectory(trajectory_id, fill_algorithm, gap_ranges[0])
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    # 3
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    # [ ... ... {'range': {'start': 1201, 'end': 1300}, 'type': 'filled'}, ... ... ]
    ```
=== "Lua"
    ``` lua
    -- - Create an empty labeled trajectory
    trajectory_label = "trajectory"
    trajectory_id = qtm.data.object.trajectory.add_trajectory(trajectory_label)
    
    -- - Get measurement range
    measured_range = qtm.gui.timeline.get_measured_range()
    print(measured_range)
    -- {start = 0, end = 2999}
    
    -- - Generate dummy 3d data
    dummy_3d_data = {}
    for x_value = measured_range["start"], measured_range["end"] do
        table.insert(dummy_3d_data, {position = {x_value, 1000.0, 1000.0}, residual = 0.0})
    end
    
    -- - Add generated 3d data to the trajectory
    qtm.data.series._3d.set_samples(trajectory_id, measured_range, dummy_3d_data)
    
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    -- {{range = {start = 0, end = 2999}, type = "virtual"}}
    
    -- - Split the trajectory in 3 parts
    split_index_1 = 1200
    split_index_2 = 1300
    qtm.data.object.trajectory.split_part(trajectory_id, split_index_1)
    qtm.data.object.trajectory.split_part(trajectory_id, split_index_2)
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    -- 3
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    -- {{range = {start = 0, end = 1200}, type = "virtual"}, {range = ... ...
    
    -- - Remove the middle part of the trajectory
    parts_to_remove_indices = {1}
    qtm.data.object.trajectory.delete_parts(trajectory_id, parts_to_remove_indices)
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    -- 2
    
    -- - Get the range of created gap
    gap_ranges = qtm.data.series._3d.get_gap_ranges(trajectory_id)
    print(gap_ranges)
    -- {{end = 1300, start = 1201}}
    
    -- - Use fill_trajectory to fill the created gap
    fill_algorithm = "polynomial"
    qtm.data.object.trajectory.fill_trajectory(trajectory_id, fill_algorithm, gap_ranges[1])
    
    print(qtm.data.object.trajectory.get_part_count(trajectory_id))
    -- 3
    print(qtm.data.object.trajectory.get_parts(trajectory_id))
    -- { ... ... {range = {start = 1201, end = 1300}, type = "filled"}, ... ...}
    ```
=== "REST"
    ``` bat
    :: - Create an empty labeled trajectory
    for /f "usebackq delims=" %%i in (`curl -s --json "[\"trajectory\"]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/add_trajectory/`) do (
      set "trajectory_id=%%i"
    )
    
    :: - Get measurement range
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/timeline/get_measured_range/
    :: {"end":24,"start":0}
    
    set measured_range={\"start\": 0, \"end\": 24}
    
    :: - Generate dummy 3d data
    set dummy_3d_data=[{\"position\": [0, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [1, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [2, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [3, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [4, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [5, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [6, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [7, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [8, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [9, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [10, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [11, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [12, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [13, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [14, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [15, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [16, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [17, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [18, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [19, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [20, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [21, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [22, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [23, 1000.0, 1000.0], \"residual\": 0.0}, {\"position\": [24, 1000.0, 1000.0], \"residual\": 0.0}]
    
    :: - Add generated 3d data to the trajectory
    curl --json "[%trajectory_id%, %measured_range%, %dummy_3d_data%]" http://localhost:7979/api/scripting/qtm/data/series/_3d/set_samples/
    
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_parts/
    :: [{"range":{"end":24,"start":0},"type":"virtual"}]
    
    :: - Split the trajectory in 3 parts
    set split_index_1=10
    set split_index_2=15
    curl --json "[%trajectory_id%, %split_index_1%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/split_part/
    curl --json "[%trajectory_id%, %split_index_2%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/split_part/
    
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_part_count/
    :: 3
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_parts/
    :: [{"range":{"end":10,"start":0},"type":"virtual"},{"range":{"end":15,"start":11},"type":"virtual"},{"range":{"end":24,"start":16},"type":"virtual"}]
    
    :: - Remove the middle part of the trajectory
    set parts_to_remove_indices=1
    curl --json "[%trajectory_id%, [%parts_to_remove_indices%]]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/delete_parts/
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_part_count/
    :: 2
    
    :: - Get the range of created gap
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/series/_3d/get_gap_ranges/
    :: [{"end":15,"start":11}]
    
    set gap_range={\"end\":15,\"start\":11}
    
    :: - Use fill_trajectory to fill the created gap
    set fill_algorithm=\"polynomial\"
    curl --json "[%trajectory_id%, %fill_algorithm%, %gap_range%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/fill_trajectory/
    
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_part_count/
    :: 3
    curl --json "[%trajectory_id%]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/get_parts/
    :: [ ... ... ,{"range":{"end":15,"start":11},"type":"filled"}, ... ...]
    ```
## add_trajectory

Add a trajectory.
```
qtm.data.object.trajectory.add_trajectory(label?)
```

**Parameters**

`label` `string?`<br/>
The label of the trajectory (if null, the trajectory will be unidentified).


**Returns**

`integer` The identifier of the added trajectory.

---

## delete_trajectory

Delete a trajectory.
```
qtm.data.object.trajectory.delete_trajectory(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.



---

## smooth_trajectory

Smooth a trajectory.
```
qtm.data.object.trajectory.smooth_trajectory(id, algorithm?, range?, settings?)
```

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
```
qtm.data.object.trajectory.fill_trajectory(id, algorithm?, range?, settings?)
```

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
```
qtm.data.object.trajectory.find_trajectory(label)
```

**Parameters**

`label` `string`<br/>
The label of the trajectory.


**Returns**

`integer?` The identifier of the found trajectory (or null, if no trajectory was found).

---

## clear_trajectories

Delete all trajectories.
```
qtm.data.object.trajectory.clear_trajectories()
```


---

## get_trajectory_id

Get a trajectory identifier by index.
```
qtm.data.object.trajectory.get_trajectory_id(index)
```

This is equivalent to calling qtm.data.series._3d.get_series_id.

**Parameters**

`index` `integer`<br/>
The index of the trajectory.


**Returns**

`integer` 

---

## get_trajectory_ids

Get all trajectory identifiers.
```
qtm.data.object.trajectory.get_trajectory_ids()
```

This is equivalent to calling qtm.data.series._3d.get_series_ids.

**Returns**

`[integer]` 

---

## get_trajectory_count

Get the number of trajectories.
```
qtm.data.object.trajectory.get_trajectory_count()
```

This is equivalent to calling qtm.data.series._3d.get_series_count.

**Returns**

`integer` 

---

## get_part

Get a part of a trajectory by index.
```
qtm.data.object.trajectory.get_part(id, index)
```

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
```
qtm.data.object.trajectory.get_parts(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`[{"range": {"start": integer, "end": integer}, "type": string}]` 

---

## get_part_count

Get the number of parts of a trajectory.
```
qtm.data.object.trajectory.get_part_count(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer` 

---

## delete_parts

Delete parts of a trajectory.
```
qtm.data.object.trajectory.delete_parts(id, part_indices?)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`part_indices` `[integer]?`<br/>
The indices of the parts to delete (if null, all parts will be deleted).



---

## move_parts

Move parts from one trajectory to another.
```
qtm.data.object.trajectory.move_parts(id_from, id_to, part_indices?)
```

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
```
qtm.data.object.trajectory.swap_parts(id_1, id_2, part_indices_1?, part_indices_2?)
```

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
```
qtm.data.object.trajectory.split_part(id, sample_index)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`sample_index` `integer`<br/>
The index of the last sample before the split.



---

## get_label

Get the label of a trajectory.
```
qtm.data.object.trajectory.get_label(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`string?` The label of the trajectory (or null, if the trajectory is unidentified).

---

## set_label

Set the label of a trajectory.
```
qtm.data.object.trajectory.set_label(id, label?)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`label` `string?`<br/>
The label of the trajectory (if null, the trajectory will become unidentified).



---

## get_color

Get the color of a trajectory.
```
qtm.data.object.trajectory.get_color(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer` The color of the trajectory (in 0xbbggrr format).

---

## set_color

Set the color of a trajectory.
```
qtm.data.object.trajectory.set_color(id, color)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`color` `integer`<br/>
The color of the trajectory (in 0xbbggrr format, see 'qtm.utilities.color' module).



---

## get_is_discarded

Get whether a trajectory is discarded.
```
qtm.data.object.trajectory.get_is_discarded(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`bool` 

---

## set_is_discarded

Set whether a trajectory is discarded.
```
qtm.data.object.trajectory.set_is_discarded(id, is_discarded)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.

`is_discarded` `bool`<br/>
True if the trajectory is discarded, otherwise false.



---

## get_active_marker_id

Get the (sequence coded) active marker identifier of a trajectory.
```
qtm.data.object.trajectory.get_active_marker_id(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The active marker identifier (or null, if the marker is passive or actively unidentified).

---

## get_rigid_body_id

Get the rigid body identifier of a trajectory.
```
qtm.data.object.trajectory.get_rigid_body_id(id)
```

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The identifier of the rigid body (or null, if the trajectory isn't part of a rigid body).

---

## get_skeleton_segment_id

Get the skeleton segment identifier of a trajectory.
```
qtm.data.object.trajectory.get_skeleton_segment_id(id)
```

If the trajectory is attached to multiple segments, only the identifier of the first found will be returned.

**Parameters**

`id` `integer`<br/>
The identifier of the trajectory.


**Returns**

`integer?` The identifier of the skeleton segment (or null, if the trajectory isn't part of a skeleton).

---

## help

Get the documentation for a module or method.
```
qtm.data.object.trajectory.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

