# qtm.settings.processing.gap_fill

Access and modify gap fill processing settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.processing.gap_fill.set_max_gap_length("project", 4)
    print(qtm.settings.processing.gap_fill.get_max_gap_length("project"))
    # 4
    
    qtm.settings.processing.gap_fill.set_fill_type("project", "linear")
    print(qtm.settings.processing.gap_fill.get_fill_type("project"))
    # linear
    
    qtm.settings.processing.gap_fill.set_settings("project", {'max_gap_length': 10, 'fill_type': 'polynomial'})
    print(qtm.settings.processing.gap_fill.get_settings("project"))
    # {'max_gap_length': 10, 'fill_type': 'polynomial'}
    ```
=== "Lua"
    ``` lua
    qtm.settings.processing.gap_fill.set_max_gap_length("project", 4)
    print(qtm.settings.processing.gap_fill.get_max_gap_length("project"))
    -- 4
    
    qtm.settings.processing.gap_fill.set_fill_type("project", "linear")
    print(qtm.settings.processing.gap_fill.get_fill_type("project"))
    -- linear
    
    qtm.settings.processing.gap_fill.set_settings("project", {max_gap_length = 10, fill_type = "polynomial"})
    print(qtm.settings.processing.gap_fill.get_settings("project"))
    -- {max_gap_length = 10, fill_type = "polynomial"}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\", 4]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/set_max_gap_length
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/get_max_gap_length
    :: 4
    
    curl --json "[\"project\", \"linear\"]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/set_fill_type
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/get_fill_type
    :: "linear"
    
    curl --json "[\"project\", {\"fill_type\":\"polynomial\",\"max_gap_length\":10}]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/set_settings/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/gap_fill/get_settings/
    :: {"fill_type":"polynomial","max_gap_length":10}
    ```
## get_max_gap_length

Get the max gap length.
```
qtm.settings.processing.gap_fill.get_max_gap_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The max gap length (in frames).

---

## set_max_gap_length

Set the max gap length.
```
qtm.settings.processing.gap_fill.set_max_gap_length(source, length)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `integer`<br/>
The max gap length (in frames).



---

## get_fill_type

Get the fill type.
```
qtm.settings.processing.gap_fill.get_fill_type(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`"linear"|"polynomial"` 

---

## set_fill_type

Set the fill type.
```
qtm.settings.processing.gap_fill.set_fill_type(source, type)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`type` `"linear"|"polynomial"`<br/>
The fill type.



---

## get_settings

Get all settings.
```
qtm.settings.processing.gap_fill.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"max_gap_length": integer?, "fill_type": "linear"|"polynomial"?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.gap_fill.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"max_gap_length": integer?, "fill_type": "linear"|"polynomial"?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.gap_fill.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

