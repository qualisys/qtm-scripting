# qtm.data.object.event

Access and modify events.

Events consist of a label, a time (in seconds) and an optional color (in 0xbbggrr format, see 'qtm.utilities.color' module). If the latter is null, red (0x0000ff) will be used.

## add_event

Add an event.

**Parameters**

`event` `{"label": string, "time": float, "color": integer?}`<br/>
The event to add.




---
## get_event_count

Get the total number of events.

**Returns**

`integer` 


---
## get_events

Get all events.

**Returns**

`[{"label": string, "time": float, "color": integer?}]` 


---
## clear_events

Remove all events.



---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
