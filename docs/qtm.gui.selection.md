# qtm.gui.selection

Access and modify the current selection.

Selections consists of a type, an identifier and an optional part index (only relevant for trajectory types). Different types cannot be selected simultaneously. A null part index means the entire trajectory is selected (and implicitly, all of its parts).

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

