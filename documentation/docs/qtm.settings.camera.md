# qtm.settings.camera

Access and modify camera settings.

## get_system_type

Get the camera system type.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"oqus"|"miqus"|"arqus"|"mixed"` 


---
## get_camera_count

Get the number of cameras.

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

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 


---
## set_use_circularity_filtering

Set whether to filter markers by circularity.

**Parameters**

`enable` `bool`<br/>
True if markers should be filtered by circularity, otherwise false.




---
## get_camera_type

Get the type of a camera.

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

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the camera.


**Returns**

`integer` 


---
## get_memory_size

Get the memory size of a camera.

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

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
