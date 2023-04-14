# qtm.settings.euler

Access and modify euler angle settings.

## get_convention

Get the euler angle convention.

**Returns**

`"qualisys"|"custom"` 


---
## set_convention

Set the euler angle convention.

**Parameters**

`convention` `"qualisys"|"custom"`<br/>
The euler angle convention.




---
## get_sequence

Get the euler angle sequence.

**Returns**

`"xyx"|"xzx"|"yxy"|"yzy"|"zxz"|"zyz"|"xyz"|"xzy"|"yxz"|"yzx"|"zxy"|"zyx"` 


---
## set_sequence

Set the euler angle sequence.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`sequence` `"xyx"|"xzx"|"yxy"|"yzy"|"zxz"|"zyz"|"xyz"|"xzy"|"yxz"|"yzx"|"zxy"|"zyx"`<br/>
The euler angle sequence.




---
## get_use_extrinsic_axes

Get whether to use extrinsic (fixed) axes.

**Returns**

`bool` 


---
## set_use_extrinsic_axes

Set whether to use extrinsic (fixed) axes.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`enable` `bool`<br/>
True if extrinsic axes should be used, otherwise false.




---
## get_first_axis_name

Get the name of the first rotation axis.

**Returns**

`string` 


---
## set_first_axis_name

Set the name of the first rotation axis.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`name` `string`<br/>
The name of the first rotation axis.




---
## get_second_axis_name

Get the name of the second rotation axis.

**Returns**

`string` 


---
## set_second_axis_name

Set the name of the second rotation axis.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`name` `string`<br/>
The name of the second rotation axis.




---
## get_third_axis_name

Get the name of the third rotation axis.

**Returns**

`string` 


---
## set_third_axis_name

Set the name of the third rotation axis.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`name` `string`<br/>
The name of the third rotation axis.




---
## get_first_angle_left_handed

Get whether to use left-handed first rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis.

**Returns**

`bool` 


---
## set_first_angle_left_handed

Set whether to use left-handed first rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis. This method requires 'custom' convention (see 'set_convention').

**Parameters**

`enable` `bool`<br/>
True if left-handed first rotation angle should be used, otherwise false.




---
## get_second_angle_left_handed

Get whether to use left-handed second rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis.

**Returns**

`bool` 


---
## set_second_angle_left_handed

Set whether to use left-handed second rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis. This method requires 'custom' convention (see 'set_convention').

**Parameters**

`enable` `bool`<br/>
True if left-handed second rotation angle should be used, otherwise false.




---
## get_third_angle_left_handed

Get whether to use left-handed third rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis.

**Returns**

`bool` 


---
## set_third_angle_left_handed

Set whether to use left-handed third rotation angle.

Left-handed means counter-clockwise facing positive direction of rotation axis. This method requires 'custom' convention (see 'set_convention').

**Parameters**

`enable` `bool`<br/>
True if left-handed third rotation angle should be used, otherwise false.




---
## get_first_angle_range

Get the range of the first rotation angle.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_first_angle_range

Set the range of the first rotation angle.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The range of the first rotation angle (must be either [-180, 180] or [0, 360]).




---
## get_third_angle_range

Get the range of the third rotation angle.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_third_angle_range

Set the range of the third rotation angle.

This method requires 'custom' convention (see 'set_convention').

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The range of the third rotation angle (must be either [-180, 180] or [0, 360]).




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
