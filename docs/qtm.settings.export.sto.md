# qtm.settings.export.sto

Access and modify sto export settings.

=== "Python"
    ``` py
    import qtm
    
    # Output in QTM coordinate system.
    qtm.settings.export.sto.set_output_x_axis("+x")
    print(qtm.settings.export.sto.get_output_x_axis())
    # +x
    
    qtm.settings.export.sto.set_output_y_axis("+y")
    print(qtm.settings.export.sto.get_output_y_axis())
    # +y
    
    qtm.settings.export.sto.set_output_z_axis("+z")
    print(qtm.settings.export.sto.get_output_z_axis())
    # +z
    
    # Output in OpenSim coordinate system.
    qtm.settings.export.sto.set_output_x_axis("+x")
    print(qtm.settings.export.sto.get_output_x_axis())
    # +x
    
    qtm.settings.export.sto.set_output_y_axis("+z")
    print(qtm.settings.export.sto.get_output_y_axis())
    # +z
    
    qtm.settings.export.sto.set_output_z_axis("-y")
    print(qtm.settings.export.sto.get_output_z_axis())
    # -y
    
    qtm.settings.export.sto.set_export_ground_reaction_forces(True)
    print(qtm.settings.export.sto.get_export_ground_reaction_forces())
    # True
    ```
=== "Lua"
    ``` lua
    -- - Output in QTM coordinate system.
    qtm.settings.export.sto.set_output_x_axis("+x")
    print(qtm.settings.export.sto.get_output_x_axis())
    -- +x
    
    qtm.settings.export.sto.set_output_y_axis("+y")
    print(qtm.settings.export.sto.get_output_y_axis())
    -- +y
    
    qtm.settings.export.sto.set_output_z_axis("+z")
    print(qtm.settings.export.sto.get_output_z_axis())
    -- +z
    
    -- - Output in OpenSim coordinate system.
    qtm.settings.export.sto.set_output_x_axis("+x")
    print(qtm.settings.export.sto.get_output_x_axis())
    -- +x
    
    qtm.settings.export.sto.set_output_y_axis("+z")
    print(qtm.settings.export.sto.get_output_y_axis())
    -- +z
    
    qtm.settings.export.sto.set_output_z_axis("-y")
    print(qtm.settings.export.sto.get_output_z_axis())
    -- -y
    
    qtm.settings.export.sto.set_export_ground_reaction_forces(true)
    print(qtm.settings.export.sto.get_export_ground_reaction_forces())
    -- true
    	
    ```
=== "REST"
    ``` bat
    :: Output in QTM coordinate system.
    curl --json "[\"+x\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_x_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_x_axis/
    :: "+x"
    
    curl --json "[\"+y\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_y_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_y_axis/
    :: "+y"
    
    curl --json "[\"+z\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_z_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_z_axis/
    :: "+z"
    
    :: Output in OpenSim coordinate system.
    curl --json "[\"+x\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_x_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_x_axis/
    :: "+x"
    
    curl --json "[\"+z\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_y_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_y_axis/
    :: "+z"
    
    curl --json "[\"-y\"]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_output_z_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_output_z_axis/
    :: "-y"
    
    curl --json "[true]" http://localhost:7979/api/scripting/qtm/settings/export/sto/set_export_ground_reaction_forces/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/sto/get_export_ground_reaction_forces/
    :: true
    ```
## get_output_x_axis

Get the axis to use as the output x axis.
```
qtm.settings.export.sto.get_output_x_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_x_axis

Set the axis to use as the output x axis.
```
qtm.settings.export.sto.set_output_x_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output x axis.



---

## get_output_y_axis

Get the axis to use as the output y axis.
```
qtm.settings.export.sto.get_output_y_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_y_axis

Set the axis to use as the output y axis.
```
qtm.settings.export.sto.set_output_y_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output y axis.



---

## get_output_z_axis

Get the axis to use as the output z axis.
```
qtm.settings.export.sto.get_output_z_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_z_axis

Set the axis to use as the output z axis.
```
qtm.settings.export.sto.set_output_z_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output z axis.



---

## get_export_ground_reaction_forces

Get whether to export ground reaction forces.
```
qtm.settings.export.sto.get_export_ground_reaction_forces()
```

**Returns**

`bool` 

---

## set_export_ground_reaction_forces

Set whether to export ground reaction forces.
```
qtm.settings.export.sto.set_export_ground_reaction_forces(enable)
```

**Parameters**

`enable` `bool`<br/>
True if ground reaction forces should be exported, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.sto.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

