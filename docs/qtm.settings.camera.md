# qtm.settings.camera

Access and modify camera settings.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.settings.camera.get_system_type("measurement"))
    # miqus
    
    camera_type = "miqus"
    print(qtm.settings.camera.get_camera_count("measurement", camera_type))
    # 10
    
    camera_index = 5
    print(qtm.settings.camera.get_camera_model("measurement", camera_index))
    # miqus m3
    
    print(qtm.settings.camera.get_serial_number("measurement", camera_index))
    # 20658
    
    print(qtm.settings.camera.is_calibrated("measurement", camera_index))
    # True
    ```
=== "Lua"
    ``` lua
    print(qtm.settings.camera.get_system_type("measurement"))
    -- miqus
    
    camera_type = "miqus"
    print(qtm.settings.camera.get_camera_count("measurement", camera_type))
    -- 10
    
    camera_index = 5
    print(qtm.settings.camera.get_camera_model("measurement", camera_index))
    -- miqus m3
    
    print(qtm.settings.camera.get_serial_number("measurement", camera_index))
    -- 20658
    
    print(qtm.settings.camera.is_calibrated("measurement", camera_index))
    -- true
    ```
=== "REST"
    ``` bat
    curl --json "[\"measurement\"]" http://localhost:7979/api/scripting/qtm/settings/camera/get_system_type/
    :: "miqus"
    
    set camera_type=\"miqus\"
    curl --json "[\"measurement\", %camera_type%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_camera_count/
    :: 10
    
    set camera_index=5
    curl --json "[\"measurement\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_camera_model/
    :: miqus m3
    
    curl --json "[\"measurement\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_serial_number/
    :: 20658
    
    curl --json "[\"measurement\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/is_calibrated/
    :: true
    ```
## get_system_type

Get the camera system type.
```
qtm.settings.camera.get_system_type(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"oqus"|"miqus"|"arqus"|"mixed"` 

---

## get_camera_count

Get the number of cameras.
```
qtm.settings.camera.get_camera_count(source, type?)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`type` `"oqus"|"miqus"|"arqus"?`<br/>
The camera type to count (if null, all camera types will be counted).


**Returns**

`integer` 

---

## get_use_circularity_filtering

Get whether to filter markers by circularity.
```
qtm.settings.camera.get_use_circularity_filtering(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_circularity_filtering

Set whether to filter markers by circularity.
```
qtm.settings.camera.set_use_circularity_filtering(enable)
```

**Parameters**

`enable` `bool`<br/>
True if markers should be filtered by circularity, otherwise false.



---

## get_camera_type

Get the type of a camera.
```
qtm.settings.camera.get_camera_type(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`"oqus"|"miqus"|"arqus"` 

---

## get_camera_model

Get the model of a camera.
```
qtm.settings.camera.get_camera_model(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`string` 

---

## get_serial_number

Get the serial number of a camera.
```
qtm.settings.camera.get_serial_number(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` 

---

## get_ip_address

Get the ip (internet protocol) address of a camera.
```
qtm.settings.camera.get_ip_address(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`string` 

---

## get_memory_size

Get the memory size of a camera.
```
qtm.settings.camera.get_memory_size(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` The memory size of the camera (in bytes).

---

## get_view_rotation

Get the view rotation of a camera.
```
qtm.settings.camera.get_view_rotation(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`"0"|"90"|"180"|"270"` 

---

## is_active

Get whether a camera is active (used for tracking).
```
qtm.settings.camera.is_active(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_master

Get whether a camera is master.
```
qtm.settings.camera.is_master(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_linearized

Get whether a camera is linearized.
```
qtm.settings.camera.is_linearized(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_calibrated

Get whether a camera is calibrated.
```
qtm.settings.camera.is_calibrated(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_waterproof

Get whether a camera is waterproof (for underwater usage).
```
qtm.settings.camera.is_waterproof(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_protected

Get whether a camera is dust and water protected (for outdoor usage).
```
qtm.settings.camera.is_protected(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_shielded

Get whether a camera is emi shielded (for mri usage).
```
qtm.settings.camera.is_shielded(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_wireless

Get whether a camera is wireless.
```
qtm.settings.camera.is_wireless(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_highspeed

Get whether a camera supports high-speed video.
```
qtm.settings.camera.is_highspeed(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_color

Get whether a camera has a color sensor.
```
qtm.settings.camera.is_color(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## is_twin

Get whether a camera is from a twin camera system.
```
qtm.settings.camera.is_twin(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## help

Get the documentation for a module or method.
```
qtm.settings.camera.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

