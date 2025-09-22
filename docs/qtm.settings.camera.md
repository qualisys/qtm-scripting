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
    
    print(qtm.settings.camera.get_use_marker_limits("project", camera_index))
    # False
    
    qtm.settings.camera.set_use_marker_limits("project", camera_index, True)
    
    print(qtm.settings.camera.get_min_marker_size("project", camera_index))
    # 128
    
    print(qtm.settings.camera.get_max_marker_size("project", camera_index))
    # 60000
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
    
    print(qtm.settings.camera.get_use_marker_limits("project", camera_index))
    -- false
    
    qtm.settings.camera.set_use_marker_limits("project", camera_index, true)
    
    print(qtm.settings.camera.get_min_marker_size("project", camera_index))
    -- 128
    
    print(qtm.settings.camera.get_max_marker_size("project", camera_index))
    -- 60000
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
    
    curl --json "[\"project\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_use_marker_limits/
    :: false
    
    curl --json "[\"project\", %camera_index%, true]" http://localhost:7979/api/scripting/qtm/settings/camera/set_use_marker_limits/
    
    curl --json "[\"project\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_min_marker_size/
    :: 128
    
    curl --json "[\"project\", %camera_index%]" http://localhost:7979/api/scripting/qtm/settings/camera/get_max_marker_size/
    :: 60000
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

## get_camera_mode

Get the camera mode of a camera.
```
qtm.settings.camera.get_camera_mode(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`"marker"|"intensity"|"video"` 

---

## set_camera_mode

Set the camera mode of a camera.
```
qtm.settings.camera.set_camera_mode(source, index, mode)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`mode` `"marker"|"intensity"|"video"`<br/>
The camera mode.



---

## get_marker_frequency

Get the marker frequency of the system.
```
qtm.settings.camera.get_marker_frequency(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The frequency (in hertz).

---

## set_marker_frequency

Set the marker frequency of the system.
```
qtm.settings.camera.set_marker_frequency(source, frequency)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`frequency` `integer`<br/>
The frequency (in hertz).



---

## get_marker_exposure_time

Get the marker exposure time of a camera.
```
qtm.settings.camera.get_marker_exposure_time(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` The exposure time (in microseconds).

---

## set_marker_exposure_time

Set the marker exposure time of a camera.
```
qtm.settings.camera.set_marker_exposure_time(source, index, time)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`time` `integer`<br/>
The exposure time (in microseconds).



---

## get_marker_threshold

Get the marker threshold of a camera.
```
qtm.settings.camera.get_marker_threshold(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` The threshold (in percent).

---

## set_marker_threshold

Set the marker threshold of a camera.
```
qtm.settings.camera.set_marker_threshold(source, index, threshold)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`threshold` `integer`<br/>
The marker threshold (in percent).



---

## get_marker_image_size

Get the marker image size of a camera.
```
qtm.settings.camera.get_marker_image_size(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`{"left": integer, "top": integer, "right": integer, "bottom": integer}` 

---

## set_marker_image_size

Set the marker image size of a camera.
```
qtm.settings.camera.set_marker_image_size(source, index, size)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`size` `{"left": integer, "top": integer, "right": integer, "bottom": integer}`<br/>
The image size.



---

## get_use_marker_masks

Get whether a camera should use marker masks.
```
qtm.settings.camera.get_use_marker_masks(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## set_use_marker_masks

Set whether a camera should use marker masks.
```
qtm.settings.camera.set_use_marker_masks(source, index, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`enable` `bool`<br/>
True if marker masks should be used, otherwise false.



---

## get_marker_masks

Get the marker masks of a camera.
```
qtm.settings.camera.get_marker_masks(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`[{"left": integer, "top": integer, "right": integer, "bottom": integer}]` 

---

## set_marker_masks

Set the marker masks of a camera.
```
qtm.settings.camera.set_marker_masks(source, index, masks)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`masks` `[{"left": integer, "top": integer, "right": integer, "bottom": integer}]`<br/>
The marker masks.



---

## get_use_marker_circularity_filtering

Get whether to filter markers by circularity.
```
qtm.settings.camera.get_use_marker_circularity_filtering(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_marker_circularity_filtering

Set whether to filter markers by circularity.
```
qtm.settings.camera.set_use_marker_circularity_filtering(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if markers should be filtered by circularity, otherwise false.



---

## get_marker_circularity_threshold

Get the marker circularity threshold.
```
qtm.settings.camera.get_marker_circularity_threshold(source)
```

This method requires marker circularity filtering to be enabled (see 'set_use_marker_circularity_filtering').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"none"|"low"|"medium"|"high"|"very_high"` 

---

## set_marker_circularity_threshold

Set the marker circularity threshold.
```
qtm.settings.camera.set_marker_circularity_threshold(source, threshold)
```

This method requires marker circularity filtering to be enabled (see 'set_use_marker_circularity_filtering').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`threshold` `"none"|"low"|"medium"|"high"|"very_high"`<br/>
The marker circularity threshold.



---

## get_use_marker_limits

Get whether a camera should use marker limits.
```
qtm.settings.camera.get_use_marker_limits(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`bool` 

---

## set_use_marker_limits

Set whether a camera should use marker limits.
```
qtm.settings.camera.set_use_marker_limits(source, index, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`enable` `bool`<br/>
True if marker limits should be used, otherwise false.



---

## get_min_marker_size

Get the minimum marker size of a camera.
```
qtm.settings.camera.get_min_marker_size(source, index)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` The minimum marker size (in subpixels).

---

## set_min_marker_size

Set the minimum marker size of a camera.
```
qtm.settings.camera.set_min_marker_size(source, index, size)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`size` `integer`<br/>
The minimum marker size (in subpixels).



---

## get_max_marker_size

Get the maximum marker size of a camera.
```
qtm.settings.camera.get_max_marker_size(source, index)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` The maximum marker size (in subpixels).

---

## set_max_marker_size

Set the maximum marker size of a camera.
```
qtm.settings.camera.set_max_marker_size(source, index, size)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`size` `integer`<br/>
The maximum marker size (in subpixels).



---

## get_max_marker_count

Get the maximum marker count of a camera.
```
qtm.settings.camera.get_max_marker_count(source, index)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` 

---

## set_max_marker_count

Set the maximum marker count of a camera.
```
qtm.settings.camera.set_max_marker_count(source, index, count)
```

This method requires marker limits to be enabled (see 'set_use_marker_limits').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`count` `integer`<br/>
The maximum marker count.



---

## get_marker_exposure_delay_mode

Get the marker exposure delay mode of the system.
```
qtm.settings.camera.get_marker_exposure_delay_mode(source)
```

This method requires 'passive' marker type (see 'set_marker_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"none"|"group"|"custom"` 

---

## set_marker_exposure_delay_mode

Set the marker exposure delay mode of the system.
```
qtm.settings.camera.set_marker_exposure_delay_mode(source, mode)
```

This method requires 'passive' marker type (see 'set_marker_type').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"none"|"group"|"custom"`<br/>
The exposure delay mode.



---

## get_marker_exposure_group

Get the marker exposure group of a camera.
```
qtm.settings.camera.get_marker_exposure_group(source, index)
```

This method requires 'passive' marker type (see 'set_marker_type') and 'group' marker exposure delay mode (see 'set_marker_exposure_delay_mode').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` 

---

## set_marker_exposure_group

Set the marker exposure group of a camera.
```
qtm.settings.camera.set_marker_exposure_group(source, index, group)
```

This method requires 'passive' marker type (see 'set_marker_type') and 'group' marker exposure delay mode (see 'set_marker_exposure_delay_mode').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`group` `integer`<br/>
The exposure group. Must be within the [0, 4] range.



---

## get_marker_exposure_delay

Get the marker exposure delay of a camera.
```
qtm.settings.camera.get_marker_exposure_delay(source, index)
```

This method requires 'passive' marker type (see 'set_marker_type') and 'custom' marker exposure delay mode (see 'set_marker_exposure_delay_mode').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` 

---

## set_marker_exposure_delay

Set the marker exposure delay of a camera.
```
qtm.settings.camera.set_marker_exposure_delay(source, index, delay)
```

This method requires 'passive' marker type (see 'set_marker_type') and 'custom' marker exposure delay mode (see 'set_marker_exposure_delay_mode').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`delay` `integer`<br/>
The exposure delay (in microseconds).



---

## get_marker_sensor_mode

Get the marker sensor mode of a camera.
```
qtm.settings.camera.get_marker_sensor_mode(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`"1x"|"4x"|"16x"|"64x"` 

---

## set_marker_sensor_mode

Set the marker sensor mode of a camera.
```
qtm.settings.camera.set_marker_sensor_mode(source, index, mode)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`mode` `"1x"|"4x"|"16x"|"64x"`<br/>
The sensor mode.



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

## set_view_rotation

Set the view rotation of a camera.
```
qtm.settings.camera.set_view_rotation(source, index, rotation)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.

`rotation` `"0"|"90"|"180"|"270"`<br/>
The view rotation.



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

