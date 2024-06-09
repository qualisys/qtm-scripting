# qtm.settings.processing.aim

Access and modify aim processing settings.

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

## get_model_application_count

Get the number of applications of an aim model.
```
qtm.settings.processing.aim.get_model_application_count(source, path)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.


**Returns**

`integer` 

---

## set_model_application_count

Set the number of applications of an aim model.
```
qtm.settings.processing.aim.set_model_application_count(source, path, count)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The path of the aim model.

`count` `integer`<br/>
The number of applications of the aim model.



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

