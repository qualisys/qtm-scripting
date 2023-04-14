# qtm.gui.timeline

Interface to the measurement timeline.

## get_frequency

Get the frequency.

**Returns**

`float` 


---
## get_frame_count

Get the total number of frames.

**Returns**

`integer` 


---
## get_current_time

Get the current time.

**Returns**

`float` The current time (in seconds).


---
## get_current_frame

Get the current frame number.

**Returns**

`integer` 


---
## set_current_frame

Set the current frame number.

**Parameters**

`frame` `integer`<br/>
The new current frame number (must be within the current selected range).




---
## get_measured_range

Get the measured range.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_measured_range

Set the measured range.

This is equivalent to doing a trim operation.

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new measured range.




---
## get_selected_range

Get the selected range.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_selected_range

Set the selected range.

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new selected range (must be within the measured range).




---
## get_trace_range

Get the trace range.

**Returns**

`{"start": integer, "end": integer}` 


---
## set_trace_range

Set the trace range.

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new trace range (must be within the current selected range).




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
