# qtm.gui.selection

Access and modify the current selection.

Selections consists of a type, an identifier and an optional part index (only relevant for trajectory types). Different types cannot be selected simultaneously. A null part index means the entire trajectory is selected (and implicitly, all of its parts).

## clear_selections

Remove all selections.

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to remove (if null, all selection types will be removed).




---
## is_selected

Get whether an object is currently selected.

**Parameters**

`selection` `{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}`<br/>
The object.


**Returns**

`bool` 


---
## get_selection_count

Get the current number of selections.

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to count (if null, all selection types will be counted).


**Returns**

`integer` 


---
## get_selections

Get the current selections.

**Parameters**

`type` `"trajectory"|"bone"?`<br/>
The selection type to get (if null, all selection types will be returned).


**Returns**

`[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]` 


---
## set_selections

Set the current selections.

This will overwrite any existing selections.

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The selections.




---
## select

Select objects.

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The objects to select.




---
## deselect

Deselect objects.

**Parameters**

`selections` `[{"type": "trajectory"|"bone", "id": integer, "part_index": integer?}]`<br/>
The objects to deselect.




---
## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 


---
