# qtm.settings.processing.aim

Access and modify aim processing settings.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.settings.processing.aim.get_model_count("project"))
    # 1
    
    model_index = 0
    model_path = qtm.settings.processing.aim.get_model_path("project", model_index)
    print(model_path)
    # C:\Users\<username>\Documents\Project\AIM models\Animation.qam
    
    print(qtm.settings.processing.aim.get_model_is_applied("project", model_path))
    # True
    
    print(qtm.settings.processing.aim.get_relative_bone_length_tolerance("project"))
    # 75.0
    
    aim_1_path = r"C:\Users\<username>\Documents\SampleAims\SampleAim_1.qam"
    aim_2_path = r"C:\Users\<username>\Documents\SampleAims\SampleAim_2.qam"
    qtm.settings.processing.aim.set_settings("project", {"keep_existing_labels": True,"models": {aim_1_path: {"is_applied": True},aim_2_path: {"is_applied": False}},"randomize_bone_colors": True,"relative_bone_length_tolerance": 1})
    print(qtm.settings.processing.aim.get_settings("project"))
    # {'keep_existing_labels': True,'models': {'C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_1.qam': {'is_applied': True},'C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_2.qam': {'is_applied': False}},'randomize_bone_colors': True,'relative_bone_length_tolerance': 1}
    ```
=== "Lua"
    ``` lua
    print(qtm.settings.processing.aim.get_model_count("project"))
    -- 1
    
    model_index = 0
    model_path = qtm.settings.processing.aim.get_model_path("project", model_index)
    print(model_path)
    -- C:\Users\<username>\Documents\Project\AIM models\Animation.qam
    
    print(qtm.settings.processing.aim.get_model_is_applied("project", model_path))
    -- true
    
    print(qtm.settings.processing.aim.get_relative_bone_length_tolerance("project"))
    -- 75.0
    
    aim_1_path = "C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_1.qam"
    aim_2_path = "C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_2.qam"
    qtm.settings.processing.aim.set_settings("project", {randomize_bone_colors = true, models = {[aim_1_path] = {is_applied = false}, [aim_2_path] = {is_applied = true}}, keep_existing_labels = true, relative_bone_length_tolerance = 1.0})
    print(qtm.settings.processing.aim.get_settings("project"))
    -- {randomize_bone_colors = true, models = {C:\Users\<username>\Documents\SampleAims\SampleAim_1.qam = {is_applied = false}, C:\Users\<username>\Documents\SampleAims\SampleAim_2.qam = {is_applied = true}}, keep_existing_labels = true, relative_bone_length_tolerance = 1.0}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/get_model_count
    :: 1
    
    set model_index=0
    curl --json "[\"project\", %model_index%]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/get_model_path
    :: "C:\\Users\\<username>\\Documents\\Project\\AIM models\\Animation.qam"
    
    set model_path=\"C:\\Users\\^<username^>\\Documents\\Project\\AIM models\\Animation.qam\"
    curl --json "[\"project\", %model_path%]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/get_model_is_applied
    :: true
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/get_relative_bone_length_tolerance
    :: 75
    
    set aim_1_path=\"C:\\Users\\^<username^>\\Documents\\SampleAims\\SampleAim_1.qam\"
    set aim_2_path=\"C:\\Users\\^<username^>\\Documents\\SampleAims\\SampleAim_2.qam\"
    curl --json "[\"project\", {\"keep_existing_labels\":true,\"models\":{%aim_1_path%:{\"is_applied\":true},%aim_2_path%:{\"is_applied\":false}},\"randomize_bone_colors\":true,\"relative_bone_length_tolerance\":1}]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/set_settings
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/aim/get_settings
    :: {"keep_existing_labels":true,"models":{"C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_1.qam":{"is_applied":true},"C:\\Users\\<username>\\Documents\\SampleAims\\SampleAim_2.qam":{"is_applied":false},"randomize_bone_colors":true,"relative_bone_length_tolerance":1}
    ```
## add_model

Add an aim model.
```
qtm.settings.processing.aim.add_model(source, path)
```

The added aim model will be applied by default.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.



---

## delete_model

Delete an aim model.
```
qtm.settings.processing.aim.delete_model(source, path)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.



---

## clear_models

Remove all aim models.
```
qtm.settings.processing.aim.clear_models(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.



---

## get_model_path

Get an aim model path by index.
```
qtm.settings.processing.aim.get_model_path(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the aim model.


**Returns**

`string` 

---

## get_model_paths

Get all aim model paths.
```
qtm.settings.processing.aim.get_model_paths(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`[string]` 

---

## get_model_count

Get the number of aim models.
```
qtm.settings.processing.aim.get_model_count(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## get_model_is_applied

Get whether an aim model is applied.
```
qtm.settings.processing.aim.get_model_is_applied(source, path)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.


**Returns**

`bool` 

---

## set_model_is_applied

Set whether an aim model is applied.
```
qtm.settings.processing.aim.set_model_is_applied(source, path, is_applied)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.

`is_applied` `bool`<br/>
True if the aim model should be applied, otherwise false.



---

## get_relative_bone_length_tolerance

Get the relative bone length tolerance.
```
qtm.settings.processing.aim.get_relative_bone_length_tolerance(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` 

---

## set_relative_bone_length_tolerance

Set the relative bone length tolerance.
```
qtm.settings.processing.aim.set_relative_bone_length_tolerance(source, tolerance)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`tolerance` `float`<br/>
The relative bone length tolerance (in percent). Must be within the [1.0, 75.0] range.



---

## get_keep_existing_labels

Get whether to keep existing labels in applied aim models.
```
qtm.settings.processing.aim.get_keep_existing_labels(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_keep_existing_labels

Set whether to keep existing labels in applied aim models.
```
qtm.settings.processing.aim.set_keep_existing_labels(source, enable)
```

This setting is reset after each use.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if existing labels should be kept, otherwise false.



---

## get_randomize_bone_colors

Get whether to randomize bone colors for each applied aim model.
```
qtm.settings.processing.aim.get_randomize_bone_colors(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_randomize_bone_colors

Set whether to randomize bone colors for each applied aim model.
```
qtm.settings.processing.aim.set_randomize_bone_colors(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if bone colors should be randomized, otherwise false.



---

## get_settings

Get all settings.
```
qtm.settings.processing.aim.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"models": {string: {"is_applied": bool?}}?, "relative_bone_length_tolerance": float?, "keep_existing_labels": bool?, "randomize_bone_colors": bool?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.aim.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"models": {string: {"is_applied": bool?}}?, "relative_bone_length_tolerance": float?, "keep_existing_labels": bool?, "randomize_bone_colors": bool?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.aim.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

