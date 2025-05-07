# qtm.settings.export.trc

Access and modify trc export settings.

=== "Python"
    ``` py
    import qtm
    
    # Output in QTM coordinate system.
    qtm.settings.export.trc.set_output_x_axis("+x")
    print(qtm.settings.export.trc.get_output_x_axis())
    # +x
    
    qtm.settings.export.trc.set_output_y_axis("+y")
    print(qtm.settings.export.trc.get_output_y_axis())
    # +y
    
    qtm.settings.export.trc.set_output_z_axis("+z")
    print(qtm.settings.export.trc.get_output_z_axis())
    # +z
    
    # Output in OpenSim coordinate system.
    qtm.settings.export.trc.set_output_x_axis("+x")
    print(qtm.settings.export.trc.get_output_x_axis())
    # +x
    
    qtm.settings.export.trc.set_output_y_axis("+z")
    print(qtm.settings.export.trc.get_output_y_axis())
    # +z
    
    qtm.settings.export.trc.set_output_z_axis("-y")
    print(qtm.settings.export.trc.get_output_z_axis())
    # -y
    ```
=== "Lua"
    ``` lua
    -- - Output in QTM coordinate system.
    qtm.settings.export.trc.set_output_x_axis("+x")
    print(qtm.settings.export.trc.get_output_x_axis())
    -- +x
    
    qtm.settings.export.trc.set_output_y_axis("+y")
    print(qtm.settings.export.trc.get_output_y_axis())
    -- +y
    
    qtm.settings.export.trc.set_output_z_axis("+z")
    print(qtm.settings.export.trc.get_output_z_axis())
    -- +z
    
    -- - Output in OpenSim coordinate system.
    qtm.settings.export.trc.set_output_x_axis("+x")
    print(qtm.settings.export.trc.get_output_x_axis())
    -- +x
    
    qtm.settings.export.trc.set_output_y_axis("+z")
    print(qtm.settings.export.trc.get_output_y_axis())
    -- +z
    
    qtm.settings.export.trc.set_output_z_axis("-y")
    print(qtm.settings.export.trc.get_output_z_axis())
    -- -y
    ```
=== "REST"
    ``` bat
    :: Output in QTM coordinate system.
    curl --json "[\"+x\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_x_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_x_axis/
    :: "+x"
    
    curl --json "[\"+y\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_y_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_y_axis/
    :: "+y"
    
    curl --json "[\"+z\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_z_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_z_axis/
    :: "+z"
    
    :: Output in OpenSim coordinate system.
    curl --json "[\"+x\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_x_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_x_axis/
    :: "+x"
    
    curl --json "[\"+z\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_y_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_y_axis/
    :: "+z"
    
    curl --json "[\"-y\"]" http://localhost:7979/api/scripting/qtm/settings/export/trc/set_output_z_axis/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/trc/get_output_z_axis/
    :: "-y"
    ```
## get_output_x_axis

Get the axis to use as the output x axis.
```
qtm.settings.export.trc.get_output_x_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_x_axis

Set the axis to use as the output x axis.
```
qtm.settings.export.trc.set_output_x_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output x axis.



---

## get_output_y_axis

Get the axis to use as the output y axis.
```
qtm.settings.export.trc.get_output_y_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_y_axis

Set the axis to use as the output y axis.
```
qtm.settings.export.trc.set_output_y_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output y axis.



---

## get_output_z_axis

Get the axis to use as the output z axis.
```
qtm.settings.export.trc.get_output_z_axis()
```

**Returns**

`"+x"|"-x"|"+y"|"-y"|"+z"|"-z"` 

---

## set_output_z_axis

Set the axis to use as the output z axis.
```
qtm.settings.export.trc.set_output_z_axis(input_axis)
```

**Parameters**

`input_axis` `"+x"|"-x"|"+y"|"-y"|"+z"|"-z"`<br/>
The axis to use as the output z axis.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.trc.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

