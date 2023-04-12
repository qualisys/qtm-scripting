# qtm.settings.export.tsv

Access and modify tsv export settings.

## get_export_2d

Get whether to export 2d data.

**Returns**

`bool` 


---
## set_export_2d

Set whether to export 2d data.

**Parameters**

`enable` `bool`<br/>
True if 2d data should be exported, otherwise false.




---
## get_export_3d

Get whether to export 3d data.

**Returns**

`bool` 


---
## set_export_3d

Set whether to export 3d data.

**Parameters**

`enable` `bool`<br/>
True if 3d data should be exported, otherwise false.




---
## get_export_6d

Get whether to export 6dof data.

**Returns**

`bool` 


---
## set_export_6d

Set whether to export 6dof data.

**Parameters**

`enable` `bool`<br/>
True if 6dof data should be exported, otherwise false.




---
## get_export_analog

Get whether to export analog data.

**Returns**

`bool` 


---
## set_export_analog

Set whether to export analog data.

**Parameters**

`enable` `bool`<br/>
True if analog data should be exported, otherwise false.




---
## get_export_force

Get whether to export force data.

**Returns**

`bool` 


---
## set_export_force

Set whether to export force data.

**Parameters**

`enable` `bool`<br/>
True if force data should be exported, otherwise false.




---
## get_export_eye

Get whether to export eye data.

**Returns**

`bool` 


---
## set_export_eye

Set whether to export eye data.

**Parameters**

`enable` `bool`<br/>
True if eye data should be exported, otherwise false.




---
## get_export_skeleton

Get whether to export skeleton data.

**Returns**

`bool` 


---
## set_export_skeleton

Set whether to export skeleton data.

**Parameters**

`enable` `bool`<br/>
True if skeleton data should be exported, otherwise false.




---
## get_export_time

Get whether to export sample times.

**Returns**

`bool` 


---
## set_export_time

Set whether to export sample times.

**Parameters**

`enable` `bool`<br/>
True if sample times should be exported, otherwise false.




---
## get_export_event

Get whether to export events.

**Returns**

`bool` 


---
## set_export_event

Set whether to export events.

Events require file header to be exported (see 'set_export_file_header').

**Parameters**

`enable` `bool`<br/>
True if events should be exported, otherwise false.




---
## get_export_point_type

Get whether to export 3d point types.

**Returns**

`bool` 


---
## set_export_point_type

Set whether to export 3d point types.

**Parameters**

`enable` `bool`<br/>
True if 3d point types should be exported, otherwise false.




---
## get_export_file_header

Get whether to export a file header.

**Returns**

`bool` 


---
## set_export_file_header

Set whether to export a file header.

**Parameters**

`enable` `bool`<br/>
True if a file header should be exported, otherwise false.




---
## get_export_column_header

Get whether to export column headers.

**Returns**

`bool` 


---
## set_export_column_header

Set whether to export column headers.

Column headers require file header to be exported (see 'set_export_file_header').

**Parameters**

`enable` `bool`<br/>
True if column headers should be exported, otherwise false.




---
## get_null_string

Get the null string.

**Returns**

`string` 


---
## set_null_string

Set the null string.

**Parameters**

`string` `string`<br/>
The null string.




---
## get_exclude_unidentified

Get whether to exclude unidentified trajectories.

**Returns**

`bool` 


---
## set_exclude_unidentified

Set whether to exclude unidentified trajectories.

**Parameters**

`enable` `bool`<br/>
True if unidentified trajectories should be excluded, otherwise false.




---
## get_exclude_empty

Get whether to exclude empty trajectories.

**Returns**

`bool` 


---
## set_exclude_empty

Set whether to exclude empty trajectories.

**Parameters**

`enable` `bool`<br/>
True if empty trajectories should be excluded, otherwise false.




---
## get_exclude_partially_labeled

Get whether to exclude partially labeled frames.

**Returns**

`bool` 


---
## set_exclude_partially_labeled

Set whether to exclude partially labeled frames.

This will override the exported range.

**Parameters**

`enable` `bool`<br/>
True if partially labeled frames should be excluded, otherwise false.




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
