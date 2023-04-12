# qtm.settings.export.c3d

Access and modify c3d export settings.

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
## get_use_full_label

Get whether to use full labels.

**Returns**

`bool` 


---
## set_use_full_label

Set whether to use full labels.

**Parameters**

`enable` `bool`<br/>
True if full labels should be used, otherwise false.




---
## get_use_relative_event_time

Get whether to use relative event times.

**Returns**

`bool` 


---
## set_use_relative_event_time

Set whether to use relative event times.

If enabled, event times will be relative to the start of the exported range.

**Parameters**

`enable` `bool`<br/>
True if relative event times should be used, otherwise false.




---
## get_use_zero_force_baseline

Get whether to use zero force baseline.

**Returns**

`bool` 


---
## set_use_zero_force_baseline

Set whether to use zero force baseline.

**Parameters**

`enable` `bool`<br/>
True if zero force baseline should be used, otherwise false.




---
## get_zero_force_baseline_range

Get the zero force baseline range.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_zero_force_baseline_range

Set the zero force baseline range.

This method requires zero force baseline to be enabled (see 'set_use_zero_force_baseline').

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The zero force baseline range.




---
## get_length_units

Get the length units.

**Returns**

`"mm"|"cm"|"m"` 


---
## set_length_units

Set the length units.

**Parameters**

`units` `"mm"|"cm"|"m"`<br/>
The length units.




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
