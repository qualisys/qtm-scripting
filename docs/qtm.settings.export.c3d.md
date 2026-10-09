# qtm.settings.export.c3d

Access and modify c3d export settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.export.c3d.set_exclude_empty(True)
    print(qtm.settings.export.c3d.get_exclude_empty())
    # True
    
    qtm.settings.export.c3d.set_exclude_partially_labeled(False)
    print(qtm.settings.export.c3d.get_exclude_partially_labeled())
    # False
    
    zero_baseline_range = {"start": 0, "end": 9}
    qtm.settings.export.c3d.set_use_zero_force_baseline(True)
    qtm.settings.export.c3d.set_zero_force_baseline_range(zero_baseline_range)
    print(qtm.settings.export.c3d.get_zero_force_baseline_range())
    # {'start': 0, 'end': 9}
    
    # Set a Y-up axis mapping (output X from input X, Y from Z, Z from -Y).
    qtm.settings.export.c3d.set_output_x_axis("+x")
    qtm.settings.export.c3d.set_output_y_axis("+z")
    qtm.settings.export.c3d.set_output_z_axis("-y")
    print(qtm.settings.export.c3d.get_output_x_axis())
    # +x
    print(qtm.settings.export.c3d.get_output_y_axis())
    # +z
    print(qtm.settings.export.c3d.get_output_z_axis())
    # -y
    
    qtm.settings.export.c3d.set_export_subjects(True)
    print(qtm.settings.export.c3d.get_export_subjects())
    # True
    ```
=== "Lua"
    ``` lua
    qtm.settings.export.c3d.set_exclude_empty(true)
    print(qtm.settings.export.c3d.get_exclude_empty())
    -- true
    
    qtm.settings.export.c3d.set_exclude_partially_labeled(false)
    print(qtm.settings.export.c3d.get_exclude_partially_labeled())
    -- false
    
    zero_baseline_range = {["start"] = 0, ["end"] = 9}
    qtm.settings.export.c3d.set_use_zero_force_baseline(true)
    qtm.settings.export.c3d.set_zero_force_baseline_range(zero_baseline_range)
    print(qtm.settings.export.c3d.get_zero_force_baseline_range())
    -- {start = 0, end = 9}
    
    -- Set a Y-up axis mapping (output X from input X, Y from Z, Z from -Y).
    qtm.settings.export.c3d.set_output_x_axis("+x")
    qtm.settings.export.c3d.set_output_y_axis("+z")
    qtm.settings.export.c3d.set_output_z_axis("-y")
    print(qtm.settings.export.c3d.get_output_x_axis())
    -- +x
    print(qtm.settings.export.c3d.get_output_y_axis())
    -- +z
    print(qtm.settings.export.c3d.get_output_z_axis())
    -- -y
    
    qtm.settings.export.c3d.set_export_subjects(true)
    print(qtm.settings.export.c3d.get_export_subjects())
    -- true
    ```
=== "REST"
    ``` bat
    curl --json "[true]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_exclude_empty/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_exclude_empty/
    :: true
    
    curl --json "[false]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_exclude_partially_labeled/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_exclude_partially_labeled/
    :: false
    
    set zero_baseline_range={\"start\": 0, \"end\": 9}
    curl --json "[true]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_use_zero_force_baseline/
    curl --json "[%zero_baseline_range%]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_zero_force_baseline_range/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_zero_force_baseline_range/
    :: {"end":9,"start":0}
    
    :: Set a Y-up axis mapping (output X from input X, Y from Z, Z from -Y).
    curl --json "[\"+x\"]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_output_x_axis/
    curl --json "[\"+z\"]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_output_y_axis/
    curl --json "[\"-y\"]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_output_z_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_output_x_axis/
    :: "+x"
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_output_y_axis/
    :: "+z"
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_output_z_axis/
    :: "-y"
    
    curl --json "[true]" http://localhost:7979/api/scripting/qtm/settings/export/c3d/set_export_subjects/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/c3d/get_export_subjects/
    :: true
    ```
## get_exclude_unidentified

Get whether to exclude unidentified trajectories.
```
qtm.settings.export.c3d.get_exclude_unidentified()
```

**Returns**

`bool` 

---

## set_exclude_unidentified

Set whether to exclude unidentified trajectories.
```
qtm.settings.export.c3d.set_exclude_unidentified(enable)
```

**Parameters**

`enable` `bool`<br/>
True if unidentified trajectories should be excluded, otherwise false.



---

## get_exclude_empty

Get whether to exclude empty trajectories.
```
qtm.settings.export.c3d.get_exclude_empty()
```

**Returns**

`bool` 

---

## set_exclude_empty

Set whether to exclude empty trajectories.
```
qtm.settings.export.c3d.set_exclude_empty(enable)
```

**Parameters**

`enable` `bool`<br/>
True if empty trajectories should be excluded, otherwise false.



---

## get_exclude_partially_labeled

Get whether to exclude partially labeled frames.
```
qtm.settings.export.c3d.get_exclude_partially_labeled()
```

**Returns**

`bool` 

---

## set_exclude_partially_labeled

Set whether to exclude partially labeled frames.
```
qtm.settings.export.c3d.set_exclude_partially_labeled(enable)
```

This will override the exported range.

**Parameters**

`enable` `bool`<br/>
True if partially labeled frames should be excluded, otherwise false.



---

## get_use_full_label

Get whether to use full labels.
```
qtm.settings.export.c3d.get_use_full_label()
```

**Returns**

`bool` 

---

## set_use_full_label

Set whether to use full labels.
```
qtm.settings.export.c3d.set_use_full_label(enable)
```

**Parameters**

`enable` `bool`<br/>
True if full labels should be used, otherwise false.



---

## get_use_relative_event_time

Get whether to use relative event times.
```
qtm.settings.export.c3d.get_use_relative_event_time()
```

**Returns**

`bool` 

---

## set_use_relative_event_time

Set whether to use relative event times.
```
qtm.settings.export.c3d.set_use_relative_event_time(enable)
```

If enabled, event times will be relative to the start of the exported range.

**Parameters**

`enable` `bool`<br/>
True if relative event times should be used, otherwise false.



---

## get_use_zero_force_baseline

Get whether to use zero force baseline.
```
qtm.settings.export.c3d.get_use_zero_force_baseline()
```

**Returns**

`bool` 

---

## set_use_zero_force_baseline

Set whether to use zero force baseline.
```
qtm.settings.export.c3d.set_use_zero_force_baseline(enable)
```

**Parameters**

`enable` `bool`<br/>
True if zero force baseline should be used, otherwise false.



---

## get_zero_force_baseline_range

Get the zero force baseline range.
```
qtm.settings.export.c3d.get_zero_force_baseline_range()
```

**Returns**

`{"start": integer, "end": integer}` 

---

## set_zero_force_baseline_range

Set the zero force baseline range.
```
qtm.settings.export.c3d.set_zero_force_baseline_range(range)
```

This method requires zero force baseline to be enabled (see 'set_use_zero_force_baseline').

**Parameters**

`range` `{"start": integer, "end": integer}`<br/>
The zero force baseline range.



---

## get_length_units

Get the length units.
```
qtm.settings.export.c3d.get_length_units()
```

**Returns**

`"mm"|"cm"|"m"` 

---

## set_length_units

Set the length units.
```
qtm.settings.export.c3d.set_length_units(units)
```

**Parameters**

`units` `"mm"|"cm"|"m"`<br/>
The length units.



---

## get_output_x_axis

Get the axis to use as the output x axis.
```
qtm.settings.export.c3d.get_output_x_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_x_axis

Set the axis to use as the output x axis.
```
qtm.settings.export.c3d.set_output_x_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output x axis.



---

## get_output_y_axis

Get the axis to use as the output y axis.
```
qtm.settings.export.c3d.get_output_y_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_y_axis

Set the axis to use as the output y axis.
```
qtm.settings.export.c3d.set_output_y_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output y axis.



---

## get_output_z_axis

Get the axis to use as the output z axis.
```
qtm.settings.export.c3d.get_output_z_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_z_axis

Set the axis to use as the output z axis.
```
qtm.settings.export.c3d.set_output_z_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output z axis.



---

## get_export_subjects

Get whether to export the subjects parameter group.
```
qtm.settings.export.c3d.get_export_subjects()
```

**Returns**

`bool` 

---

## set_export_subjects

Set whether to export the subjects parameter group.
```
qtm.settings.export.c3d.set_export_subjects(enable)
```

**Parameters**

`enable` `bool`<br/>
True if the subjects parameter group should be exported, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.c3d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

