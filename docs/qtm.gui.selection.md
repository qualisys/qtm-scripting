# qtm.gui.selection

Access and modify the current selection.

Selections consists of a type, an identifier and an optional part index (only relevant for trajectory types). Different types cannot be selected simultaneously. A null part index means the entire trajectory is selected (and implicitly, all of its parts).

=== "Python"
    ``` py
    import qtm
    
    id_f_headtop = qtm.data.object.trajectory.find_trajectory("F_HeadTop")
    id_f_headfront = qtm.data.object.trajectory.find_trajectory("F_HeadFront")
    
    select = [{"type": "trajectory", "id": id_f_headtop, "part_index": None},
              {"type": "trajectory", "id": id_f_headfront, "part_index": None}]
    
    qtm.gui.selection.clear_selections()
    print(qtm.gui.selection.get_selection_count())
    # 0
    
    qtm.gui.selection.select(select)
    
    print(qtm.gui.selection.get_selection_count())
    # 2
    
    print(qtm.gui.selection.get_selections())
    # [{'type': 'trajectory', 'id': 106051, 'part_index': None}, {'type': 'trajectory', 'id': 106053, 'part_index': None}]
    ```
=== "Lua"
    ``` lua
    id_f_headtop = qtm.data.object.trajectory.find_trajectory("F_HeadTop")
    id_f_headfront = qtm.data.object.trajectory.find_trajectory("F_HeadFront")
    
    select = {{type = "trajectory", id = id_f_headtop, part_index = nil},
              {type = "trajectory", id = id_f_headfront, part_index = nil}}
    
    qtm.gui.selection.clear_selections()
    print(qtm.gui.selection.get_selection_count())
    -- 0
    
    qtm.gui.selection.select(select)
    
    print(qtm.gui.selection.get_selection_count())
    -- 2
    
    print(qtm.gui.selection.get_selections())
    -- {{id = 106051, type = "trajectory"}, {id = 106053, type = "trajectory"}}
    ```
=== "REST"
    ``` bat
    for /f "usebackq delims=" %%i in (`curl -s --json "[\"F_HeadTop\"]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/find_trajectory/`) do (
      set "id_f_headtop=%%i"
    )
    for /f "usebackq delims=" %%i in (`curl -s --json "[\"F_HeadFront\"]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/find_trajectory/`) do (
      set "id_f_headfront=%%i"
    )
    
    set select=[{\"type\": \"trajectory\", \"id\": %id_f_headtop%, \"part_index\": null}, {\"type\": \"trajectory\", \"id\": %id_f_headfront%, \"part_index\": null}]
    
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/selection/clear_selections/
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/selection/get_selection_count/
    :: 0
    
    curl --json "[%select%]" http://localhost:7979/api/scripting/qtm/gui/selection/select/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/selection/get_selection_count/
    :: 2
    
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/selection/get_selections/
    :: [{"id":106051,"part_index":null,"type":"trajectory"},{"id":106053,"part_index":null,"type":"trajectory"}]
    ```
## clear_selections

Remove all selections.
```
qtm.gui.selection.clear_selections(type?)
```

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to remove (if null, all selection types will be removed).



---

## is_selected

Get whether an object is currently selected.
```
qtm.gui.selection.is_selected(selection)
```

**Parameters**

`selection` `{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}`<br/>
The object.


**Returns**

`bool` 

---

## get_selection_count

Get the current number of selections.
```
qtm.gui.selection.get_selection_count(type?)
```

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to count (if null, all selection types will be counted).


**Returns**

`integer` 

---

## get_selections

Get the current selections.
```
qtm.gui.selection.get_selections(type?)
```

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to get (if null, all selection types will be returned).


**Returns**

`[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]` 

---

## set_selections

Set the current selections.
```
qtm.gui.selection.set_selections(selections)
```

This will overwrite any existing selections.

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The selections.



---

## select

Select objects.
```
qtm.gui.selection.select(selections)
```

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The objects to select.



---

## deselect

Deselect objects.
```
qtm.gui.selection.deselect(selections)
```

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The objects to deselect.



---

## help

Get the documentation for a module or method.
```
qtm.gui.selection.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

