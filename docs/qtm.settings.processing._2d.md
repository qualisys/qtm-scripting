# qtm.settings.processing._2d

Access and modify 2d processing settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.processing._2d.set_use_max_marker_size("project", False)
    print(qtm.settings.processing._2d.get_use_max_marker_size("project"))
    # False
    
    print(qtm.settings.processing._2d.get_max_marker_size("measurement"))
    # 4096
    
    qtm.settings.processing._2d.set_settings("project", {'correct_center_points': False, 'use_min_marker_size': True, 'use_max_marker_size': True, 'min_marker_size': 20, 'max_marker_size': 30})
    print(qtm.settings.processing._2d.get_settings("project"))
    # {'correct_center_points': False, 'use_software_marker_masks': None, 'use_min_marker_size': True, 'use_max_marker_size': True, 'min_marker_size': 20, 'max_marker_size': 30}
    ```
=== "Lua"
    ``` lua
    qtm.settings.processing._2d.set_use_max_marker_size("project", false)
    print(qtm.settings.processing._2d.get_use_max_marker_size("project"))
    -- false
    
    print(qtm.settings.processing._2d.get_max_marker_size("measurement"))
    -- 4096
    
    qtm.settings.processing._2d.set_settings("project", {use_max_marker_size = true, max_marker_size = 500, correct_center_points = false, use_min_marker_size = true, min_marker_size = 200})
    qtm.settings.processing._2d.get_settings("project")
    -- {use_max_marker_size = true, max_marker_size = 500, correct_center_points = false, use_min_marker_size = true, min_marker_size = 200}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\", false]" http://localhost:7979/api/scripting/qtm/settings/processing/_2d/set_use_max_marker_size
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/_2d/get_use_max_marker_size
    :: false
    
    curl --json "[\"measurement\"]" http://localhost:7979/api/scripting/qtm/settings/processing/_2d/get_max_marker_size
    :: 4096
    
    curl --json "[\"project\", {\"correct_center_points\":false,\"max_marker_size\":300,\"min_marker_size\":200,\"use_max_marker_size\":true,\"use_min_marker_size\":true}]" http://localhost:7979/api/scripting/qtm/settings/processing/_2d/set_settings/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/_2d/get_settings/
    :: {"correct_center_points":false,"max_marker_size":300,"min_marker_size":200,"use_max_marker_size":true,"use_min_marker_size":true,"use_software_marker_masks":null}
    ```
## get_correct_center_points

Get whether to correct center points.
```
qtm.settings.processing._2d.get_correct_center_points(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_correct_center_points

Set whether to correct center points.
```
qtm.settings.processing._2d.set_correct_center_points(source, enable)
```

Center point correction requires circularity filtering to be enabled (see 'qtm.settings.camera.set_use_marker_circularity_filtering').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if center points should be corrected, otherwise false.



---

## get_use_software_marker_masks

Get whether to use software marker masks.
```
qtm.settings.processing._2d.get_use_software_marker_masks(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_software_marker_masks

Set whether to use software marker masks.
```
qtm.settings.processing._2d.set_use_software_marker_masks(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if software marker masks should be used, otherwise false.



---

## get_use_min_marker_size

Get whether to filter markers by minimum size.
```
qtm.settings.processing._2d.get_use_min_marker_size(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_min_marker_size

Set whether to filter markers by minimum size.
```
qtm.settings.processing._2d.set_use_min_marker_size(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if markers should be filtered by minimum size, otherwise false.



---

## get_use_max_marker_size

Get whether to filter markers by maximum size.
```
qtm.settings.processing._2d.get_use_max_marker_size(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_max_marker_size

Set whether to filter markers by maximum size.
```
qtm.settings.processing._2d.set_use_max_marker_size(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if markers should be filtered by maximum size, otherwise false.



---

## get_min_marker_size

Get the minimum marker size.
```
qtm.settings.processing._2d.get_min_marker_size(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The minimum marker size (in subpixels).

---

## set_min_marker_size

Set the minimum marker size.
```
qtm.settings.processing._2d.set_min_marker_size(source, size)
```

This method requires filtering by minimum marker size to be enabled (see 'set_use_min_marker_size').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`size` `integer`<br/>
The minimum marker size (in subpixels).



---

## get_max_marker_size

Get the maximum marker size.
```
qtm.settings.processing._2d.get_max_marker_size(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The maximum marker size (in subpixels).

---

## set_max_marker_size

Set the maximum marker size.
```
qtm.settings.processing._2d.set_max_marker_size(source, size)
```

This method requires filtering by maximum marker size to be enabled (see 'set_use_max_marker_size').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`size` `integer`<br/>
The maximum marker size (in subpixels).



---

## get_settings

Get all settings.
```
qtm.settings.processing._2d.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"correct_center_points": bool?, "use_software_marker_masks": bool?, "use_min_marker_size": bool?, "use_max_marker_size": bool?, "min_marker_size": integer?, "max_marker_size": integer?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing._2d.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"correct_center_points": bool?, "use_software_marker_masks": bool?, "use_min_marker_size": bool?, "use_max_marker_size": bool?, "min_marker_size": integer?, "max_marker_size": integer?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing._2d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

