# qtm.settings.processing.sal

Access and modify sal processing settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.processing.sal.set_claim_threshold("project", 40)
    print(qtm.settings.processing.sal.get_claim_threshold("project"))
    # 40
    
    qtm.settings.processing.sal.set_disqualification_threshold("project", 1000)
    print(qtm.settings.processing.sal.get_disqualification_threshold("project"))
    # 1000
    
    qtm.settings.processing.sal.set_settings("project", {claim_threshold = 40, disqualification_threshold = 1000})
    print(qtm.settings.processing.sal.get_settings("project"))
    # {'claim_threshold': 40, 'disqualification_threshold': 1000}
    ```
=== "Lua"
    ``` lua
    qtm.settings.processing.sal.set_claim_threshold("project", 40)
    qtm.settings.processing.sal.get_claim_threshold("project")
    -- 40
    
    qtm.settings.processing.sal.set_disqualification_threshold("project", 1000)
    qtm.settings.processing.sal.get_disqualification_threshold("project")
    -- 1000
    
    qtm.settings.processing.sal.set_settings("project", {claim_threshold = 40, disqualification_threshold = 1000})
    qtm.settings.processing.sal.get_settings("project")
    -- {claim_threshold = 40, disqualification_threshold = 1000}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\", 40]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/set_claim_threshold/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/get_claim_threshold/
    :: 40
    
    curl --json "[\"project\", 1000]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/set_disqualification_threshold/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/get_disqualification_threshold/
    :: 1000
    
    curl --json "[\"project\", {\"claim_threshold\":20,\"disqualification_threshold\":200}]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/set_settings/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/sal/get_settings/
    :: {"claim_threshold":20,"disqualification_threshold":200}
    ```
## get_claim_threshold

Get the claim threshold.
```
qtm.settings.processing.sal.get_claim_threshold(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The claim threshold (in millimeters).

---

## set_claim_threshold

Set the claim threshold.
```
qtm.settings.processing.sal.set_claim_threshold(source, threshold)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`threshold` `integer`<br/>
The claim threshold (in millimeters).



---

## get_disqualification_threshold

Get the disqualification threshold.
```
qtm.settings.processing.sal.get_disqualification_threshold(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The disqualification threshold (in millimeters).

---

## set_disqualification_threshold

Set the disqualification threshold.
```
qtm.settings.processing.sal.set_disqualification_threshold(source, threshold)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`threshold` `integer`<br/>
The disqualification threshold (in millimeters).



---

## get_settings

Get all settings.
```
qtm.settings.processing.sal.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"claim_threshold": integer?, "disqualification_threshold": integer?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.sal.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"claim_threshold": integer?, "disqualification_threshold": integer?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.sal.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

