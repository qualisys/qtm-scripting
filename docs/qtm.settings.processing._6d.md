# qtm.settings.processing._6d

Access and modify 6dof processing settings.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.settings.processing._6d.get_body_count("measurement"))
    # 3
    
    body_index = 2
    print(qtm.settings.processing._6d.get_body_name("measurement", body_index))
    # L_Frame
    
    print(qtm.settings.processing._6d.get_point_count("measurement", body_index))
    # 4
    
    point_index = 0
    print(qtm.settings.processing._6d.get_point_name("measurement", body_index, point_index))
    # L_Frame - 1
    
    print(qtm.settings.processing._6d.get_point_position("measurement", body_index, point_index))
    # [226.46037005049945, 0.6947789149269771, 1.19924822792081]
    
    qtm.settings.processing._6d.set_settings("project", {'identify_partial_bodies': True, 'calculate_missing_markers': False, 'bodies': [{'name': 'Body_1', 'is_enabled': True, 'color': 255, 'coordinate_system': {'type': 'global', 'relative_body_index': None, 'fixed_transform': None}, 'min_marker_count': 3, 'max_residual': 10.0, 'bone_length_tolerance': 5.0, 'filter_type': 'multi_purpose', 'mesh_settings': {'filename': 'utah-teapot.obj', 'position': [1.0, 2.0, 3.0], 'rotation': [4.0, 5.0, 6.0], 'scale': 1.0, 'opacity': 1.0}, 'points': None}, {'name': 'Body_2', 'is_enabled': True, 'color': 65280, 'coordinate_system': {'type': 'global', 'relative_body_index': None, 'fixed_transform': None}, 'min_marker_count': 3, 'max_residual': 10.0, 'bone_length_tolerance': 5.0, 'filter_type': 'none', 'mesh_settings': {'filename': '', 'position': [0.0, 0.0, 0.0], 'rotation': [0.0, 0.0, 0.0], 'scale': 1.0, 'opacity': 1.0}, 'points': [{'name': 'Body_2 - 1', 'position': [0.0, 0.0, 0.0], 'is_virtual': False, 'active_marker_id': None}]}]})
    print(qtm.settings.processing._6d.get_settings("project"))
    # {'identify_partial_bodies': True, 'calculate_missing_markers': False, 'bodies': [{'name': 'Body_1', 'is_enabled': True, 'color': 255, 'coordinate_system': {'type': 'global', 'relative_body_index': None, 'fixed_transform': None}, 'min_marker_count': 3, 'max_residual': 10.0, 'bone_length_tolerance': 5.0, 'filter_type': 'multi_purpose', 'mesh_settings': {'filename': 'utah-teapot.obj', 'position': [1.0, 2.0, 3.0], 'rotation': [4.0, 5.0, 6.0], 'scale': 1.0, 'opacity': 1.0}, 'points': []}, {'name': 'Body_2', 'is_enabled': True, 'color': 65280, 'coordinate_system': {'type': 'global', 'relative_body_index': None, 'fixed_transform': None}, 'min_marker_count': 3, 'max_residual': 10.0, 'bone_length_tolerance': 5.0, 'filter_type': 'none', 'mesh_settings': {'filename': '', 'position': [0.0, 0.0, 0.0], 'rotation': [0.0, 0.0, 0.0], 'scale': 1.0, 'opacity': 1.0}, 'points': [{'name': 'Body_2 - 1', 'position': [0.0, 0.0, 0.0], 'is_virtual': False, 'active_marker_id': None}]}]}
    ```
=== "Lua"
    ``` lua
    print(qtm.settings.processing._6d.get_body_count("measurement"))
    -- 3
    
    body_index = 2
    print(qtm.settings.processing._6d.get_body_name("measurement", body_index))
    -- L_Frame
    
    print(qtm.settings.processing._6d.get_point_count("measurement", body_index))
    -- 4
    
    point_index = 0
    print(qtm.settings.processing._6d.get_point_name("measurement", body_index, point_index))
    -- L_Frame - 1
    
    print(qtm.settings.processing._6d.get_point_position("measurement", body_index, point_index))
    -- {226.4603700505, 0.69477891492698, 1.1992482279208}
    
    qtm.settings.processing._6d.set_settings("project", {calculate_missing_markers = false, bodies = {{max_residual = 10.0, coordinate_system = {type = "global"}, mesh_settings = {filename = "utah-teapot.obj", position = {1.0, 2.0, 3.0}, opacity = 1.0, rotation = {4.0, 5.0, 6.0}, scale = 1.0}, bone_length_tolerance = 5.0, filter_type = "multi_purpose", min_marker_count = 3, color = 255, name = "Body_1", is_enabled = true}, {max_residual = 10.0, coordinate_system = {type = "global"}, mesh_settings = {filename = "", position = {0.0, 0.0, 0.0}, opacity = 1.0, rotation = {0.0, 0.0, 0.0}, scale = 1.0}, bone_length_tolerance = 5.0, points = {{position = {0.0, 0.0, 0.0}, name = "Body_2 - 1", is_virtual = false}}, filter_type = "none", min_marker_count = 3, color = 65280, name = "Body_2", is_enabled = true}}, identify_partial_bodies = true})
    print(qtm.settings.processing._6d.get_settings("project"))
    -- {calculate_missing_markers = false, bodies = {{max_residual = 10.0, coordinate_system = {type = "global"}, mesh_settings = {filename = "utah-teapot.obj", position = {1.0, 2.0, 3.0}, opacity = 1.0, rotation = {4.0, 5.0, 6.0}, scale = 1.0}, bone_length_tolerance = 5.0, points = {}, filter_type = "multi_purpose", min_marker_count = 3, color = 255, name = "Body_1", is_enabled = true}, {max_residual = 10.0, coordinate_system = {type = "global"}, mesh_settings = {filename = "", position = {0.0, 0.0, 0.0}, opacity = 1.0, rotation = {0.0, 0.0, 0.0}, scale = 1.0}, bone_length_tolerance = 5.0, points = {{position = {0.0, 0.0, 0.0}, name = "Body_2 - 1", is_virtual = false}}, filter_type = "none", min_marker_count = 3, color = 65280, name = "Body_2", is_enabled = true}}, identify_partial_bodies = true}
    ```
=== "REST"
    ``` bat
    curl --json "[\"measurement\"]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_body_count
    :: 3
    
    set body_index=2
    curl --json "[\"measurement\", %body_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_body_name
    :: "L_Frame"
    
    curl --json "[\"measurement\", %body_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_point_count
    :: 4
    
    set point_index=0
    curl --json "[\"measurement\", %body_index%, %point_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_point_name
    :: "L_Frame - 1"
    
    curl --json "[\"measurement\", %body_index%, %point_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_point_position
    :: [226.46037005049945,0.69477891492697708,1.1992482279208101]
    
    curl --json "[\"project\", {\"bodies\":[{\"bone_length_tolerance\":5,\"color\":255,\"coordinate_system\":{\"fixed_transform\":null,\"relative_body_index\":null,\"type\":\"global\"},\"filter_type\":\"multi_purpose\",\"is_enabled\":true,\"max_residual\":10,\"mesh_settings\":{\"filename\":\"utah-teapot.obj\",\"opacity\":1,\"position\":[1,2,3],\"rotation\":[4,5,6],\"scale\":1},\"min_marker_count\":3,\"name\":\"Body_1\",\"points\":null},{\"bone_length_tolerance\":5,\"color\":65280,\"coordinate_system\":{\"fixed_transform\":null,\"relative_body_index\":null,\"type\":\"global\"},\"filter_type\":\"none\",\"is_enabled\":true,\"max_residual\":10,\"mesh_settings\":{\"filename\":\"\",\"opacity\":1,\"position\":[0,0,0],\"rotation\":[0,0,0],\"scale\":1},\"min_marker_count\":3,\"name\":\"Body_2\",\"points\":[{\"active_marker_id\":null,\"is_virtual\":false,\"name\":\"Body_2 - 1\",\"position\":[0,0,0]}]}],\"calculate_missing_markers\":false,\"identify_partial_bodies\":true}]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/set_settings
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/_6d/get_settings
    :: {"bodies":[{"bone_length_tolerance":5,"color":255,"coordinate_system":{"fixed_transform":null,"relative_body_index":null,"type":"global"},"filter_type":"multi_purpose","is_enabled":true,"max_residual":10,"mesh_settings":{"filename":"utah-teapot.obj","opacity":1,"position":[1,2,3],"rotation":[4,5,6],"scale":1},"min_marker_count":3,"name":"Body_1","points":[]},{"bone_length_tolerance":5,"color":65280,"coordinate_system":{"fixed_transform":null,"relative_body_index":null,"type":"global"},"filter_type":"none","is_enabled":true,"max_residual":10,"mesh_settings":{"filename":"","opacity":1,"position":[0,0,0],"rotation":[0,0,0],"scale":1},"min_marker_count":3,"name":"Body_2","points":[{"active_marker_id":null,"is_virtual":false,"name":"Body_2 - 1","position":[0,0,0]}]}],"calculate_missing_markers":false,"identify_partial_bodies":true}
    ```
## get_identify_partial_bodies

Get whether to identify partially visible rigid bodies.
```
qtm.settings.processing._6d.get_identify_partial_bodies(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_identify_partial_bodies

Set whether to identify partially visible rigid bodies.
```
qtm.settings.processing._6d.set_identify_partial_bodies(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if partially visible rigid bodies should be identified, otherwise false.



---

## get_calculate_missing_markers

Get whether to calculate missing markers in rigid bodies.
```
qtm.settings.processing._6d.get_calculate_missing_markers(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_calculate_missing_markers

Set whether to calculate missing markers in rigid bodies.
```
qtm.settings.processing._6d.set_calculate_missing_markers(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if missing markers should be calculated, otherwise false.



---

## add_body

Add a rigid body.
```
qtm.settings.processing._6d.add_body(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The index of the added rigid body.

---

## add_point

Add a point to a rigid body.
```
qtm.settings.processing._6d.add_point(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`integer` The index of the added point.

---

## delete_body

Delete a rigid body.
```
qtm.settings.processing._6d.delete_body(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.



---

## delete_point

Delete a point in a rigid body.
```
qtm.settings.processing._6d.delete_point(source, body_index, point_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.



---

## get_body_count

Get the number of rigid bodies.
```
qtm.settings.processing._6d.get_body_count(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## get_point_count

Get the number of points in a rigid body.
```
qtm.settings.processing._6d.get_point_count(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`integer` 

---

## get_body_name

Get the name of a rigid body.
```
qtm.settings.processing._6d.get_body_name(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`string` 

---

## set_body_name

Set the name of a rigid body.
```
qtm.settings.processing._6d.set_body_name(source, body_index, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`name` `string`<br/>
The name of the rigid body.



---

## get_body_is_enabled

Get whether a rigid body is enabled.
```
qtm.settings.processing._6d.get_body_is_enabled(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`bool` 

---

## set_body_is_enabled

Set whether a rigid body is enabled.
```
qtm.settings.processing._6d.set_body_is_enabled(source, body_index, is_enabled)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`is_enabled` `bool`<br/>
True if the rigid body should be enabled, otherwise false.



---

## get_body_color

Get the color of a rigid body.
```
qtm.settings.processing._6d.get_body_color(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`integer` The color of the rigid body (in 0xbbggrr format).

---

## set_body_color

Set the color of a rigid body.
```
qtm.settings.processing._6d.set_body_color(source, body_index, color)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`color` `integer`<br/>
The color of the rigid body (in 0xbbggrr format, see 'qtm.utilities.color' module).



---

## get_body_coordinate_system

Get the coordinate system of a rigid body.
```
qtm.settings.processing._6d.get_body_coordinate_system(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`{"type": "global"|"relative"|"fixed", "relative_body_index": integer?, "fixed_transform": mat4x4f?}` 

---

## set_body_coordinate_system

Set the coordinate system of a rigid body.
```
qtm.settings.processing._6d.set_body_coordinate_system(source, body_index, coordinate_system)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`coordinate_system` `{"type": "global"|"relative"|"fixed", "relative_body_index": integer?, "fixed_transform": mat4x4f?}`<br/>
The coordinate system of the rigid body.



---

## get_body_min_marker_count

Get the minimum marker count of a rigid body.
```
qtm.settings.processing._6d.get_body_min_marker_count(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`integer` 

---

## set_body_min_marker_count

Set the minimum marker count of a rigid body.
```
qtm.settings.processing._6d.set_body_min_marker_count(source, body_index, count)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`count` `integer`<br/>
The minimum marker count of the rigid body (must be greater than or equal to 3).



---

## get_body_max_residual

Get the maximum residual of a rigid body.
```
qtm.settings.processing._6d.get_body_max_residual(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`float` The maximum residual of the rigid body (in millimeters).

---

## set_body_max_residual

Set the maximum residual of a rigid body.
```
qtm.settings.processing._6d.set_body_max_residual(source, body_index, residual)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`residual` `float`<br/>
The maximum residual of the rigid body (in millimeters). Must be within the [0.01, 100.0] range.



---

## get_body_bone_length_tolerance

Get the bone length tolerance of a rigid body.
```
qtm.settings.processing._6d.get_body_bone_length_tolerance(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`float` The bone length tolerance (in millimeters).

---

## set_body_bone_length_tolerance

Set the bone length tolerance of a rigid body.
```
qtm.settings.processing._6d.set_body_bone_length_tolerance(source, body_index, tolerance)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`tolerance` `float`<br/>
The bone length tolerance (in millimeters). Must be within the [0.01, 1000.0] range.



---

## get_body_filter_type

Get the filter type of a rigid body.
```
qtm.settings.processing._6d.get_body_filter_type(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`"none"|"multi_purpose"|"high_stability"|"static_pose"` 

---

## set_body_filter_type

Set the filter type of a rigid body.
```
qtm.settings.processing._6d.set_body_filter_type(source, body_index, filter_type)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`filter_type` `"none"|"multi_purpose"|"high_stability"|"static_pose"`<br/>
The filter type.



---

## get_body_mesh_settings

Get the mesh settings of a rigid body.
```
qtm.settings.processing._6d.get_body_mesh_settings(source, body_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.


**Returns**

`{"filename": string?, "position": vec3f?, "rotation": vec3f?, "scale": float?, "opacity": float?}` 

---

## set_body_mesh_settings

Set the mesh settings of a rigid body.
```
qtm.settings.processing._6d.set_body_mesh_settings(source, body_index, mesh_settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`mesh_settings` `{"filename": string?, "position": vec3f?, "rotation": vec3f?, "scale": float?, "opacity": float?}`<br/>
The mesh settings. Scale must be within the [0.01, 1000.0] range and opacity within the [0.01, 1.0] range.



---

## get_point_name

Get the name of a point in a rigid body.
```
qtm.settings.processing._6d.get_point_name(source, body_index, point_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.


**Returns**

`string` 

---

## set_point_name

Set the name of a point in a rigid body.
```
qtm.settings.processing._6d.set_point_name(source, body_index, point_index, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.

`name` `string`<br/>
The name of the point.



---

## get_point_position

Get the position of a point in a rigid body.
```
qtm.settings.processing._6d.get_point_position(source, body_index, point_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.


**Returns**

`vec3f` 

---

## set_point_position

Set the position of a point in a rigid body.
```
qtm.settings.processing._6d.set_point_position(source, body_index, point_index, position)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.

`position` `vec3f`<br/>
The position of the point.



---

## get_point_is_virtual

Get whether a point in a rigid body is virtual.
```
qtm.settings.processing._6d.get_point_is_virtual(source, body_index, point_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.


**Returns**

`bool` 

---

## set_point_is_virtual

Set whether a point in a rigid body is virtual.
```
qtm.settings.processing._6d.set_point_is_virtual(source, body_index, point_index, is_virtual)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.

`is_virtual` `bool`<br/>
True if the point is virtual, otherwise false.



---

## get_point_active_marker_id

Get the (sequence coded) active marker identifier of a point in a rigid body.
```
qtm.settings.processing._6d.get_point_active_marker_id(source, body_index, point_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.


**Returns**

`integer?` The active marker identifier of the point (or null, if the marker is passive).

---

## set_point_active_marker_id

Set the (sequence coded) active marker identifier of a point in a rigid body.
```
qtm.settings.processing._6d.set_point_active_marker_id(source, body_index, point_index, id?)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`body_index` `integer`<br/>
The index of the rigid body.

`point_index` `integer`<br/>
The index of the point.

`id` `integer?`<br/>
The active marker identifier of the point (if null, the marker will be regarded as passive).



---

## get_settings

Get all settings.
```
qtm.settings.processing._6d.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"identify_partial_bodies": bool?, "calculate_missing_markers": bool?, "bodies": [{"name": string?, "is_enabled": bool?, "color": integer?, "coordinate_system": {"type": "global"|"relative"|"fixed", "relative_body_index": integer?, "fixed_transform": mat4x4f?}?, "min_marker_count": integer?, "max_residual": float?, "bone_length_tolerance": float?, "filter_type": "none"|"multi_purpose"|"high_stability"|"static_pose"?, "mesh_settings": {"filename": string?, "position": vec3f?, "rotation": vec3f?, "scale": float?, "opacity": float?}?, "points": [{"name": string?, "position": vec3f?, "is_virtual": bool?, "active_marker_id": integer?}]?}]?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing._6d.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"identify_partial_bodies": bool?, "calculate_missing_markers": bool?, "bodies": [{"name": string?, "is_enabled": bool?, "color": integer?, "coordinate_system": {"type": "global"|"relative"|"fixed", "relative_body_index": integer?, "fixed_transform": mat4x4f?}?, "min_marker_count": integer?, "max_residual": float?, "bone_length_tolerance": float?, "filter_type": "none"|"multi_purpose"|"high_stability"|"static_pose"?, "mesh_settings": {"filename": string?, "position": vec3f?, "rotation": vec3f?, "scale": float?, "opacity": float?}?, "points": [{"name": string?, "position": vec3f?, "is_virtual": bool?, "active_marker_id": integer?}]?}]?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing._6d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

