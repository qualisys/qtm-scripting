# qtm.settings.processing._2d

Access and modify 2d processing settings.

## get_correct_center_points

Get whether to correct center points.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 


---
## set_correct_center_points

Set whether to correct center points.

Center point correction requires circularity filtering to be enabled (see 'qtm.settings.camera.set_use_circularity_filtering').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if center points should be corrected, otherwise false.




---
## get_use_min_marker_size

Get whether to filter markers by minimum size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 


---
## set_use_min_marker_size

Set whether to filter markers by minimum size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if markers should be filtered by minimum size, otherwise false.




---
## get_use_max_marker_size

Get whether to filter markers by maximum size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 


---
## set_use_max_marker_size

Set whether to filter markers by maximum size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if markers should be filtered by maximum size, otherwise false.




---
## get_min_marker_size

Get the minimum marker size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The minimum marker size (in subpixels).


---
## set_min_marker_size

Set the minimum marker size.

This method requires filtering by minimum marker size to be enabled (see 'set_use_min_marker_size').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`size` `integer`<br/>
The minimum marker size (in subpixels).




---
## get_max_marker_size

Get the maximum marker size.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The maximum marker size (in subpixels).


---
## set_max_marker_size

Set the maximum marker size.

This method requires filtering by maximum marker size to be enabled (see 'set_use_max_marker_size').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`size` `integer`<br/>
The maximum marker size (in subpixels).




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
