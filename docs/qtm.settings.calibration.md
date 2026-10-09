# qtm.settings.calibration

Access and modify calibration settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.calibration.get_calibration_type("project")
    # 'wand'
    
    qtm.settings.calibration.get_wand_kit("project")
    # 'carbon_600mm'
    qtm.settings.calibration.get_wand_length("project")
    # 300.5
    
    qtm.settings.calibration.set_wand_kit("project", "custom")
    qtm.settings.calibration.set_reference_object("project", {"short_end": 150.0, "long_end": 200.0, "long_middle": 75.0})
    
    qtm.settings.calibration.get_coordinate_axes("project")
    # {'up': '-x', 'long': '+y'}
    qtm.settings.calibration.get_max_frame_count("project")
    # 3000
    
    qtm.settings.calibration.set_calibration_type("project", "fixed")
    qtm.settings.calibration.set_reference_markers("project", [[1000.0, 2000.0, 3000.0], [4000.0, 5000.0, 6000.0], [7000.0, 8000.0, 9000.0]])
    
    qtm.settings.calibration.get_camera_count("project")
    # 0
    
    qtm.settings.calibration.add_camera("project")
    # 0
    qtm.settings.calibration.set_camera_position("project", 0, [1000.0, 1000.0, 1000.0])
    qtm.settings.calibration.set_camera_cylinder_length("project", 0, 75.0)
    qtm.settings.calibration.set_camera_reference_markers("project", 0, [0, 2])
    
    qtm.settings.calibration.get_camera_count("project")
    # 1
    
    qtm.settings.calibration.get_apply_transform("project")
    # True
    qtm.settings.calibration.get_apply_translation("project")
    # True
    qtm.settings.calibration.get_translation("project")
    # [1500.0, 0.0, 3000.0]
    
    qtm.settings.calibration.get_settings("project")
    # {'calibration_type': 'fixed', 'wand_kit': None, 'wand_length': None, 'reference_object': None, 'coordinate_axes': None, ...}
    ```
=== "Lua"
    ``` lua
    qtm.settings.calibration.get_calibration_type("project")
    -- wand
    
    qtm.settings.calibration.get_wand_kit("project")
    -- carbon_600mm
    qtm.settings.calibration.get_wand_length("project")
    -- 300.5
    
    qtm.settings.calibration.set_wand_kit("project", "custom")
    qtm.settings.calibration.set_reference_object("project", {short_end = 150.0, long_end = 200.0, long_middle = 75.0})
    
    qtm.settings.calibration.get_coordinate_axes("project")
    -- {up = "-x", long = "+y"}
    qtm.settings.calibration.get_max_frame_count("project")
    --3000
    
    qtm.settings.calibration.set_calibration_type("project", "fixed")
    qtm.settings.calibration.set_reference_markers("project", {{1000.0, 2000.0, 3000.0}, {4000.0, 5000.0, 6000.0}, {7000.0, 8000.0, 9000.0}})
    
    qtm.settings.calibration.get_camera_count("project")
    -- 0
    
    qtm.settings.calibration.add_camera("project")
    -- 0
    qtm.settings.calibration.set_camera_position("project", 0, {1000.0, 1000.0, 1000.0})
    qtm.settings.calibration.set_camera_cylinder_length("project", 0, 75.0)
    qtm.settings.calibration.set_camera_reference_markers("project", 0, {0, 2})
    
    qtm.settings.calibration.get_camera_count("project")
    -- 1
    
    qtm.settings.calibration.get_apply_transform("project")
    -- true
    qtm.settings.calibration.get_apply_translation("project")
    -- true
    qtm.settings.calibration.get_translation("project")
    -- {1500.0, 0.0, 3000.0}
    
    qtm.settings.calibration.get_settings("project")
    -- {apply_transform = true, rotation = {{1.0, 0.0, 0.0}, {0.0, 1.0, 0.0}, {0.0, 0.0, 1.0}}, apply_rotation = true, translation = {1500.0, 0.0, 3000.0}, ...}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_calibration_type
    :: "wand"
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_wand_kit
    :: "carbon_600mm"
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_wand_length
    :: 300.5
    
    curl --json "[\"project\", \"custom\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_wand_kit
    curl --json "[\"project\", {\"short_end\":150.0,\"long_end\":200.0,\"long_middle\":75.0}]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_reference_object
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_coordinate_axes
    :: {"long":"+y","up":"-x"}
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_max_frame_count
    :: 3000
    
    curl --json "[\"project\", \"fixed\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_calibration_type
    curl --json "[\"project\", [[1000.0,2000.0,3000.0], [4000.0,5000.0,6000.0], [7000.0,8000.0,9000.0]]]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_reference_markers
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_camera_count
    :: 0
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/add_camera
    :: 0
    curl --json "[\"project\", 0, [1000.0,1000.0,1000.0]]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_camera_position
    curl --json "[\"project\", 0, 75.0]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_camera_cylinder_length
    curl --json "[\"project\", 0, [0,2]]" http://localhost:7979/api/scripting/qtm/settings/calibration/set_camera_reference_markers
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_camera_count
    :: 1
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_apply_transform
    :: true
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_apply_translation
    :: true
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_translation
    :: [1500,0,3000]
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/calibration/get_settings
    :: {"apply_rotation":true,"apply_transform":true,"apply_translation":true,"calibration_type":"fixed",...}
    ```
## get_calibration_type

Get the calibration type.
```
qtm.settings.calibration.get_calibration_type(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"wand"|"fixed"` 

---

## set_calibration_type

Set the calibration type.
```
qtm.settings.calibration.set_calibration_type(source, type)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`type` `"wand"|"fixed"`<br/>
The calibration type.



---

## get_wand_kit

Get the wand kit.
```
qtm.settings.calibration.get_wand_kit(source)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"none"|"110mm"|"120mm"|"300mm"|"750mm"|"carbon_300mm"|"carbon_600mm"|"active_500mm"|"active_1011mm"|"custom"` 

---

## set_wand_kit

Set the wand kit.
```
qtm.settings.calibration.set_wand_kit(source, kit)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`kit` `"none"|"110mm"|"120mm"|"300mm"|"750mm"|"carbon_300mm"|"carbon_600mm"|"active_500mm"|"active_1011mm"|"custom"`<br/>
The wand kit.



---

## get_wand_length

Get the wand length.
```
qtm.settings.calibration.get_wand_length(source)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` The wand length (in millimeters).

---

## set_wand_length

Set the wand length.
```
qtm.settings.calibration.set_wand_length(source, length)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `float`<br/>
The wand length (in millimeters). Must be within the [0.0, 2000.0] range.



---

## get_reference_object

Get the reference object definition.
```
qtm.settings.calibration.get_reference_object(source)
```

This method requires 'wand' calibration type (see 'set_calibration_type') and 'custom' wand kit (see 'set_wand_kit').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"short_end": float, "long_end": float, "long_middle": float}` The reference object definition (in millimeters).

---

## set_reference_object

Set the reference object definition.
```
qtm.settings.calibration.set_reference_object(source, object)
```

This method requires 'wand' calibration type (see 'set_calibration_type') and 'custom' wand kit (see 'set_wand_kit').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`object` `{"short_end": float, "long_end": float, "long_middle": float}`<br/>
The reference object definition (in millimeters). Short end must be within the [-10000.0, 10000.0] range, and long end/middle within [0.0, 10000.0]. Additionally, the long end must be greater than the short end, and long middle must be less than half the long end.



---

## get_coordinate_axes

Get the coordinate axes.
```
qtm.settings.calibration.get_coordinate_axes(source)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"up": "+x"|"-x"|"+y"|"-y"|"+z"|"-z", "long": "+x"|"-x"|"+y"|"-y"|"+z"|"-z"}` 

---

## set_coordinate_axes

Set the coordinate axes.
```
qtm.settings.calibration.set_coordinate_axes(source, axes)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`axes` `{"up": "+x"|"-x"|"+y"|"-y"|"+z"|"-z", "long": "+x"|"-x"|"+y"|"-y"|"+z"|"-z"}`<br/>
The coordinate axes.



---

## get_max_frame_count

Get the maximum number of frames.
```
qtm.settings.calibration.get_max_frame_count(source)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## set_max_frame_count

Set the maximum number of frames.
```
qtm.settings.calibration.set_max_frame_count(source, count)
```

This method requires 'wand' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`count` `integer`<br/>
The maximum number of frames. Must be within the [1000, 30000] range.



---

## get_reference_markers

Get the reference marker positions.
```
qtm.settings.calibration.get_reference_markers(source)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`[vec3f]` The reference marker positions (in millimeters).

---

## set_reference_markers

Set the reference marker positions.
```
qtm.settings.calibration.set_reference_markers(source, markers)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`markers` `[vec3f]`<br/>
The reference marker positions (in millimeters).



---

## add_camera

Add a camera.
```
qtm.settings.calibration.add_camera(source)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The index of the added camera.

---

## delete_camera

Delete a camera.
```
qtm.settings.calibration.delete_camera(source, index)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.



---

## get_camera_count

Get the number of cameras.
```
qtm.settings.calibration.get_camera_count(source)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## get_camera_position

Get the position of a camera.
```
qtm.settings.calibration.get_camera_position(source, index)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`vec3f` The camera position (in millimeters).

---

## set_camera_position

Set the position of a camera.
```
qtm.settings.calibration.set_camera_position(source, index, position)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`position` `vec3f`<br/>
The camera position (in millimeters).



---

## get_camera_cylinder_length

Get the cylinder length of a camera.
```
qtm.settings.calibration.get_camera_cylinder_length(source, index)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`float` The cylinder length (in millimeters).

---

## set_camera_cylinder_length

Set the cylinder length of a camera.
```
qtm.settings.calibration.set_camera_cylinder_length(source, index, length)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`length` `float`<br/>
The cylinder length (in millimeters).



---

## get_camera_reference_markers

Get the indices of the visible reference markers in a camera.
```
qtm.settings.calibration.get_camera_reference_markers(source, index)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`[integer]` The indices of the visible reference markers (in left-to-right order).

---

## set_camera_reference_markers

Set the indices of the visible reference markers in a camera.
```
qtm.settings.calibration.set_camera_reference_markers(source, index, markers)
```

This method requires 'fixed' calibration type (see 'set_calibration_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`markers` `[integer]`<br/>
The indices of the visible reference markers (in left-to-right order).



---

## get_apply_transform

Get whether to apply a transform after calibration.
```
qtm.settings.calibration.get_apply_transform(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_apply_transform

Set whether to apply a transform after calibration.
```
qtm.settings.calibration.set_apply_transform(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if a transform should be applied, otherwise false.



---

## get_apply_translation

Get whether to apply a translation after calibration.
```
qtm.settings.calibration.get_apply_translation(source)
```

This method requires a transform to be applied (see 'set_apply_transform').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_apply_translation

Get whether to apply a translation after calibration.
```
qtm.settings.calibration.set_apply_translation(source, enable)
```

This method requires a transform to be applied (see 'set_apply_transform').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if a translation should be applied, otherwise false.



---

## get_apply_rotation

Get whether to apply a rotation after calibration.
```
qtm.settings.calibration.get_apply_rotation(source)
```

This method requires a transform to be applied (see 'set_apply_transform').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_apply_rotation

Get whether to apply a rotation after calibration.
```
qtm.settings.calibration.set_apply_rotation(source, enable)
```

This method requires a transform to be applied (see 'set_apply_transform').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if a rotation should be applied, otherwise false.



---

## get_translation

Get the translation to apply after calibration.
```
qtm.settings.calibration.get_translation(source)
```

This method requires a translation to be applied (see 'set_apply_translation').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`vec3f` The translation to apply (in millimeters).

---

## set_translation

Set the translation to apply after calibration.
```
qtm.settings.calibration.set_translation(source, translation)
```

This method requires a translation to be applied (see 'set_apply_translation').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`translation` `vec3f`<br/>
The translation to apply (in millimeters).



---

## get_rotation

Get the rotation to apply after calibration.
```
qtm.settings.calibration.get_rotation(source)
```

This method requires a rotation to be applied (see 'set_apply_rotation').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`mat3x3f` The rotation matrix to apply.

---

## set_rotation

Set the rotation to apply after calibration.
```
qtm.settings.calibration.set_rotation(source, rotation)
```

This method requires a rotation to be applied (see 'set_apply_rotation').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`rotation` `mat3x3f`<br/>
The rotation matrix to apply.



---

## get_settings

Get all settings.
```
qtm.settings.calibration.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"calibration_type": "wand"|"fixed"?, "wand_kit": "none"|"110mm"|"120mm"|"300mm"|"750mm"|"carbon_300mm"|"carbon_600mm"|"active_500mm"|"active_1011mm"|"custom"?, "wand_length": float?, "reference_object": {"short_end": float, "long_end": float, "long_middle": float}?, "coordinate_axes": {"up": "+x"|"-x"|"+y"|"-y"|"+z"|"-z", "long": "+x"|"-x"|"+y"|"-y"|"+z"|"-z"}?, "max_frame_count": integer?, "reference_markers": [vec3f]?, "cameras": [{"position": vec3f?, "cylinder_length": float?, "reference_markers": [integer]?}]?, "apply_transform": bool?, "apply_translation": bool?, "apply_rotation": bool?, "translation": vec3f?, "rotation": mat3x3f?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.calibration.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"calibration_type": "wand"|"fixed"?, "wand_kit": "none"|"110mm"|"120mm"|"300mm"|"750mm"|"carbon_300mm"|"carbon_600mm"|"active_500mm"|"active_1011mm"|"custom"?, "wand_length": float?, "reference_object": {"short_end": float, "long_end": float, "long_middle": float}?, "coordinate_axes": {"up": "+x"|"-x"|"+y"|"-y"|"+z"|"-z", "long": "+x"|"-x"|"+y"|"-y"|"+z"|"-z"}?, "max_frame_count": integer?, "reference_markers": [vec3f]?, "cameras": [{"position": vec3f?, "cylinder_length": float?, "reference_markers": [integer]?}]?, "apply_transform": bool?, "apply_translation": bool?, "apply_rotation": bool?, "translation": vec3f?, "rotation": mat3x3f?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.calibration.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

