# qtm.processing

Methods for processing measurement files.

=== "Python"
    ``` py
    import qtm
    
    qtm.processing.process_2d({})
    
    qtm.processing.track_3d({})
    
    qtm.processing.fill_gaps({})
    
    qtm.processing.apply_aim({})
    
    qtm.processing.calculate_6d({})
    
    qtm.processing.solve_skeletons({})
    
    qtm.processing.apply_gloves({})
    
    qtm.processing.apply_sal({})
    ```
=== "Lua"
    ``` lua
    qtm.processing.process_2d({})
    
    qtm.processing.track_3d({})
    
    qtm.processing.fill_gaps({})
    
    qtm.processing.apply_aim({})
    
    qtm.processing.calculate_6d({})
    
    qtm.processing.solve_skeletons({})
    
    qtm.processing.apply_gloves({})
    
    qtm.processing.apply_sal({})
    ```
=== "REST"
    ``` bat
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/process_2d/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/track_3d/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/fill_gaps/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/apply_aim/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/calculate_6d/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/solve_skeletons/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/apply_gloves/
    
    curl --json "[{}]" http://localhost:7979/api/scripting/qtm/processing/apply_sal/
    ```
## process_2d

Run the 'process 2d' processing step on the current measurement file.
```
qtm.processing.process_2d(settings)
```

**Parameters**

`settings` `{"correct_center_points": bool?, "use_software_marker_masks": bool?, "use_min_marker_size": bool?, "use_max_marker_size": bool?, "min_marker_size": integer?, "max_marker_size": integer?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## track_3d

Run the 'track 3d' processing step on the current measurement file.
```
qtm.processing.track_3d(settings)
```

**Parameters**

`settings` `{"prediction_error": float?, "max_residual": float?, "min_trajectory_length": integer?, "min_ray_count": integer?, "auto_limit_ray_length": bool?, "min_ray_length": float?, "max_ray_length": float?, "store_rays": bool?, "auto_join": bool?, "max_auto_join_gap_length": integer?, "use_bounding_box": bool?, "bounding_box": {"min_x": float, "max_x": float, "min_y": float, "max_y": float, "min_z": float, "max_z": float}?, "auto_select_range": bool?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## fill_gaps

Run the 'fill gaps' processing step on the current measurement file.
```
qtm.processing.fill_gaps(settings)
```

**Parameters**

`settings` `{"max_gap_length": integer?, "fill_type": "linear"|"polynomial"?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## apply_aim

Run the 'apply aim' processing step on the current measurement file.
```
qtm.processing.apply_aim(settings)
```

**Parameters**

`settings` `{"models": {string: {"is_applied": bool?}}?, "relative_bone_length_tolerance": float?, "keep_existing_labels": bool?, "randomize_bone_colors": bool?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## calculate_6d

Run the 'calculate 6d' processing step on the current measurement file.
```
qtm.processing.calculate_6d(settings)
```

**Parameters**

`settings` `{"identify_partial_bodies": bool?, "calculate_missing_markers": bool?, "bodies": [{"name": string?, "is_enabled": bool?, "color": integer?, "coordinate_system": {"type": "global"|"relative"|"fixed", "relative_body_index": integer?, "fixed_transform": mat4x4f?}?, "min_marker_count": integer?, "max_residual": float?, "bone_length_tolerance": float?, "filter_type": "none"|"multi_purpose"|"high_stability"|"static_pose"?, "mesh_settings": {"filename": string?, "position": vec3f?, "rotation": vec3f?, "scale": float?, "opacity": float?}?, "points": [{"name": string?, "position": vec3f?, "is_virtual": bool?, "active_marker_id": integer?}]?}]?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## solve_skeletons

Run the 'solve skeletons' processing step on the current measurement file.
```
qtm.processing.solve_skeletons(settings)
```

**Parameters**

`settings` `{"skeletons": [{"name": string, "scale": float?, "root": {"name": string, "markers": [{"name": string, "position": vec3f, "weight": float}]?, "rigid_bodies": [{"name": string, "transform": mat4x4f, "weight": float}]?, "transform": mat4x4f?, "default_transform": mat4x4f?, "degrees_of_freedom": {"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}?, "solver": "none"|"global_optimization"?, "endpoint": vec3f?, "children": [...]?}?}]?, "marker_count_threshold": integer?, "realtime": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?, "post": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## apply_gloves

Run the 'apply gloves' processing step on the current measurement file.
```
qtm.processing.apply_gloves(settings)
```

**Parameters**

`settings` `{"gloves": [{"glove_name": string?, "is_enabled": bool?, "skeleton_name": string?, "use_translations": bool?}]?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## apply_sal

Run the 'apply sal' processing step on the current measurement file.
```
qtm.processing.apply_sal(settings)
```

**Parameters**

`settings` `{"claim_threshold": integer?, "disqualification_threshold": integer?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.processing.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

