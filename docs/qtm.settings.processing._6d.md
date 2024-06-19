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

## load_bodies

Load rigid bodies from an xml file.
```
qtm.settings.processing._6d.load_bodies(source, filename)
```

This will overwrite any existing rigid bodies.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`filename` `string`<br/>
The xml filename to load.



---

## save_bodies

Save rigid bodies to an xml file.
```
qtm.settings.processing._6d.save_bodies(source, filename)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`filename` `string`<br/>
The xml filename to save.



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

