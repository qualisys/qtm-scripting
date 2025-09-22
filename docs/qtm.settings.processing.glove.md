# qtm.settings.processing.glove

Access and modify glove processing settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.processing.glove.set_settings("project", {'gloves': [{'enabled': True, 'glove_name': 'left', 'skeleton_name': 'Ben', 'use_translations': False}, {'enabled': True, 'glove_name': 'right', 'skeleton_name': 'Ben', 'use_translations': False}]})
    qtm.settings.processing.glove.get_settings("project")
    # {'gloves': [{'enabled': True, 'glove_name': 'left', 'skeleton_name': 'Ben', 'use_translations': False}, {'enabled': True, 'glove_name': 'right', 'skeleton_name': 'Ben', 'use_translations': False}]}
    
    glove_index = 0
    qtm.settings.processing.glove.get_glove_count("project")
    # 2
    
    qtm.settings.processing.glove.get_glove_is_enabled("project", glove_index)
    # True
    
    qtm.settings.processing.glove.get_glove_name("project", glove_index)
    # 'left'
    
    qtm.settings.processing.glove.get_glove_skeleton_name("project", glove_index)
    # 'Ben'
    
    qtm.settings.processing.glove.get_glove_use_translations("project", glove_index)
    # False
    
    qtm.settings.processing.glove.clear_gloves("project")
    ```
=== "Lua"
    ``` lua
    qtm.settings.processing.glove.set_settings("project", {gloves = {{enabled = true, skeleton_name = "Ben", glove_name = "left", use_translations = false}, {enabled = true, skeleton_name = "Ben", glove_name = "right", use_translations = false}}})
    qtm.settings.processing.glove.get_settings("project")
    -- {gloves = {{enabled = true, skeleton_name = "Ben", glove_name = "left", use_translations = false}, {enabled = true, skeleton_name = "Ben", glove_name = "right", use_translations = false}}}
    
    qtm.settings.processing.glove.get_glove_count("project")
    -- 2
    
    glove_index = 0
    qtm.settings.processing.glove.get_glove_is_enabled("project", glove_index)
    -- true
    
    qtm.settings.processing.glove.get_glove_name("project", glove_index)
    -- left
    
    qtm.settings.processing.glove.get_glove_skeleton_name("project", glove_index)
    -- Ben
    
    qtm.settings.processing.glove.get_glove_use_translations("project", glove_index)
    -- false
    
    qtm.settings.processing.glove.clear_gloves("project") 
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\", {\"gloves\":[{\"enabled\":true,\"glove_name\":\"left\",\"skeleton_name\":\"Ben\",\"use_translations\":false},{\"enabled\":true,\"glove_name\":\"right\",\"skeleton_name\":\"Ben\",\"use_translations\":false}]}]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/set_settings/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_settings/
    :: {"gloves":[{"enabled":true,"glove_name":"left","skeleton_name":"Ben","use_translations":false},{"enabled":true,"glove_name":"right","skeleton_name":"Ben","use_translations":false}]}
    
    set glove_index=0
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_glove_count
    :: 2
    
    curl --json "[\"project\", %glove_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_glove_is_enabled
    :: true
    
    curl --json "[\"project\", %glove_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_glove_name
    :: "left"
    
    curl --json "[\"project\", %glove_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_glove_skeleton_name
    :: "Ben"
    
    curl --json "[\"project\", %glove_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/get_glove_use_translations
    :: false
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/glove/clear_gloves
    ```
## add_glove

Add a glove.
```
qtm.settings.processing.glove.add_glove(source)
```

The added glove will be disabled, have no name, have no associated skeleton and won't use translations.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The index of the added glove.

---

## delete_glove

Delete a glove.
```
qtm.settings.processing.glove.delete_glove(source, glove_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.



---

## clear_gloves

Delete all gloves.
```
qtm.settings.processing.glove.clear_gloves(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.



---

## get_glove_count

Get the number of gloves.
```
qtm.settings.processing.glove.get_glove_count(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## get_glove_name

Get the name of a glove.
```
qtm.settings.processing.glove.get_glove_name(source, glove_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.


**Returns**

`string` 

---

## set_glove_name

Set the name of a glove.
```
qtm.settings.processing.glove.set_glove_name(source, glove_index, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.

`name` `string`<br/>
The name of the glove.



---

## get_glove_is_enabled

Get whether a glove is enabled.
```
qtm.settings.processing.glove.get_glove_is_enabled(source, glove_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.


**Returns**

`bool` 

---

## set_glove_is_enabled

Set whether a glove is enabled.
```
qtm.settings.processing.glove.set_glove_is_enabled(source, glove_index, is_enabled)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.

`is_enabled` `bool`<br/>
True if the glove should be enabled, otherwise false.



---

## get_glove_skeleton_name

Get the name of the skeleton associated with a glove.
```
qtm.settings.processing.glove.get_glove_skeleton_name(source, glove_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.


**Returns**

`string` 

---

## set_glove_skeleton_name

Set the name of the skeleton associated with a glove.
```
qtm.settings.processing.glove.set_glove_skeleton_name(source, glove_index, skeleton_name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.

`skeleton_name` `string`<br/>
The name of the skeleton.



---

## get_glove_use_translations

Get whether a glove should use translations.
```
qtm.settings.processing.glove.get_glove_use_translations(source, glove_index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.


**Returns**

`bool` 

---

## set_glove_use_translations

Set whether a glove uses translations.
```
qtm.settings.processing.glove.set_glove_use_translations(source, glove_index, use_translations)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`glove_index` `integer`<br/>
The index of the glove.

`use_translations` `bool`<br/>
True if the glove should use translations, otherwise false.



---

## get_settings

Get all settings.
```
qtm.settings.processing.glove.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"gloves": [{"glove_name": string?, "is_enabled": bool?, "skeleton_name": string?, "use_translations": bool?}]?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.glove.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"gloves": [{"glove_name": string?, "is_enabled": bool?, "skeleton_name": string?, "use_translations": bool?}]?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.glove.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

