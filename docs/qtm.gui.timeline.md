# qtm.gui.timeline

Interface to the measurement timeline.

=== "Python"
    ``` py
    import qtm
    
    measured_range = qtm.gui.timeline.get_measured_range()
    print(measured_range)
    # {'start': 0, 'end': 322}
    
    range = {"start": int(measured_range["end"]*0.10), "end": int(measured_range["end"]*0.90)}
    qtm.gui.timeline.set_selected_range(range)
    
    print(qtm.gui.timeline.get_selected_range())
    # {'start': 32, 'end': 289}
    ```
=== "Lua"
    ``` lua
    measured_range = qtm.gui.timeline.get_measured_range()
    print(measured_range)
    -- {start: 0, end: 322}
    
    range = {["start"] = math.floor(measured_range["end"]*0.10), ["end"] = math.floor(measured_range["end"]*0.90)}
    qtm.gui.timeline.set_selected_range(range)
    
    print(qtm.gui.timeline.get_selected_range())
    -- {start: 32, end: 289}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/timeline/get_measured_range/
    :: {"end":322,"start":0}
    
    set range={\"start\": 32, \"end\": 289}
    curl --json "[%range%]" http://localhost:7979/api/scripting/qtm/gui/timeline/set_selected_range/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/timeline/get_selected_range/
    :: {"end":289,"start":32}
    ```
## get_frequency

Get the frequency.
```
qtm.gui.timeline.get_frequency()
```

**Returns**

`float` 

---

## get_frame_count

Get the total number of frames.
```
qtm.gui.timeline.get_frame_count()
```

**Returns**

`integer` 

---

## get_current_time

Get the current time.
```
qtm.gui.timeline.get_current_time()
```

**Returns**

`float` The current time (in seconds).

---

## get_current_frame

Get the current frame number.
```
qtm.gui.timeline.get_current_frame()
```

**Returns**

`integer` 

---

## set_current_frame

Set the current frame number.
```
qtm.gui.timeline.set_current_frame(frame)
```

**Parameters**

`frame` `integer`<br/>
The new current frame number (must be within the current selected range).



---

## get_measured_range

Get the measured range.
```
qtm.gui.timeline.get_measured_range()
```

**Returns**

`{"start": integer, "end": integer}` 

---

## set_measured_range

Set the measured range.
```
qtm.gui.timeline.set_measured_range(range)
```

This is equivalent to doing a trim operation.

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new measured range.



---

## get_selected_range

Get the selected range.
```
qtm.gui.timeline.get_selected_range()
```

**Returns**

`{"start": integer, "end": integer}` 

---

## set_selected_range

Set the selected range.
```
qtm.gui.timeline.set_selected_range(range)
```

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new selected range (must be within the measured range).



---

## get_trace_range

Get the trace range.
```
qtm.gui.timeline.get_trace_range()
```

**Returns**

`{"start": integer, "end": integer}` 

---

## set_trace_range

Set the trace range.
```
qtm.gui.timeline.set_trace_range(range)
```

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The new trace range (must be within the current selected range).



---

## help

Get the documentation for a module or method.
```
qtm.gui.timeline.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

