# qtm.data.object.event

Access and modify events.

Events consist of a label, a time (in seconds) and an optional color (in 0xbbggrr format, see 'qtm.utilities.color' module). If the latter is null, red (0x0000ff) will be used.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.data.object.event.get_event_count())
    # 0
    
    event = {"label": "New Event", "time": 0.0, "color": 255}
    qtm.data.object.event.add_event(event)
    
    print(qtm.data.object.event.get_event_count())
    # 1
    
    print(qtm.data.object.event.get_events())
    # [{'label': 'New Event', 'time': 0.0, 'color': 255}]
    
    qtm.data.object.event.clear_events()
    
    print(qtm.data.object.event.get_event_count())
    # 0
    ```
=== "Lua"
    ``` lua
    print(qtm.data.object.event.get_event_count())
    -- 0
    
    event = {time = 0.0, color = 255, label = "New event"}
    qtm.data.object.event.add_event(event)
    
    print(qtm.data.object.event.get_event_count())
    -- 1
    
    print(qtm.data.object.event.get_events())
    -- [{'label': 'New Event', 'time': 0.0, 'color': 255}]
    
    qtm.data.object.event.clear_events()
    
    print(qtm.data.object.event.get_event_count())
    -- 0
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/event/get_event_count/
    :: 0
    
    set event={\"color\":255,\"label\":\"New event\",\"time\":1.2625}
    curl --json "[%event%]" http://localhost:7979/api/scripting/qtm/data/object/event/add_event/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/event/get_event_count/
    :: 1
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/event/get_events/
    :: # [{"color":255,"label":"New event","time":1.2625}]
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/event/clear_events/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/event/get_event_count/
    :: 0
    ```
## add_event

Add an event.
```
qtm.data.object.event.add_event(event)
```

**Parameters**

`event` `{"label": string, "time": float, "color": integer?}`<br/>
The event to add.



---

## get_event_count

Get the total number of events.
```
qtm.data.object.event.get_event_count()
```

**Returns**

`integer` 

---

## get_events

Get all events.
```
qtm.data.object.event.get_events()
```

**Returns**

`[{"label": string, "time": float, "color": integer?}]` 

---

## clear_events

Delete all events.
```
qtm.data.object.event.clear_events()
```


---

## help

Get the documentation for a module or method.
```
qtm.data.object.event.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

