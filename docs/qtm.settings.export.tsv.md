# qtm.settings.export.tsv

Access and modify tsv export settings.

## get_export_2d

Get whether to export 2d data.
```
qtm.settings.export.tsv.get_export_2d()
```

**Returns**

`bool` 

---

## set_export_2d

Set whether to export 2d data.
```
qtm.settings.export.tsv.set_export_2d(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 2d data should be exported, otherwise false.



---

## get_export_3d

Get whether to export 3d data.
```
qtm.settings.export.tsv.get_export_3d()
```

**Returns**

`bool` 

---

## set_export_3d

Set whether to export 3d data.
```
qtm.settings.export.tsv.set_export_3d(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 3d data should be exported, otherwise false.



---

## get_export_6d

Get whether to export 6dof data.
```
qtm.settings.export.tsv.get_export_6d()
```

**Returns**

`bool` 

---

## set_export_6d

Set whether to export 6dof data.
```
qtm.settings.export.tsv.set_export_6d(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 6dof data should be exported, otherwise false.



---

## get_export_analog

Get whether to export analog data.
```
qtm.settings.export.tsv.get_export_analog()
```

**Returns**

`bool` 

---

## set_export_analog

Set whether to export analog data.
```
qtm.settings.export.tsv.set_export_analog(enable)
```

**Parameters**

`enable` `bool`<br/>
True if analog data should be exported, otherwise false.



---

## get_export_force

Get whether to export force data.
```
qtm.settings.export.tsv.get_export_force()
```

**Returns**

`bool` 

---

## set_export_force

Set whether to export force data.
```
qtm.settings.export.tsv.set_export_force(enable)
```

**Parameters**

`enable` `bool`<br/>
True if force data should be exported, otherwise false.



---

## get_export_eye

Get whether to export eye data.
```
qtm.settings.export.tsv.get_export_eye()
```

**Returns**

`bool` 

---

## set_export_eye

Set whether to export eye data.
```
qtm.settings.export.tsv.set_export_eye(enable)
```

**Parameters**

`enable` `bool`<br/>
True if eye data should be exported, otherwise false.



---

## get_export_skeleton

Get whether to export skeleton data.
```
qtm.settings.export.tsv.get_export_skeleton()
```

**Returns**

`bool` 

---

## set_export_skeleton

Set whether to export skeleton data.
```
qtm.settings.export.tsv.set_export_skeleton(enable)
```

**Parameters**

`enable` `bool`<br/>
True if skeleton data should be exported, otherwise false.



---

## get_export_time

Get whether to export sample times.
```
qtm.settings.export.tsv.get_export_time()
```

**Returns**

`bool` 

---

## set_export_time

Set whether to export sample times.
```
qtm.settings.export.tsv.set_export_time(enable)
```

**Parameters**

`enable` `bool`<br/>
True if sample times should be exported, otherwise false.



---

## get_export_event

Get whether to export events.
```
qtm.settings.export.tsv.get_export_event()
```

**Returns**

`bool` 

---

## set_export_event

Set whether to export events.
```
qtm.settings.export.tsv.set_export_event(enable)
```

Events require file header to be exported (see 'set_export_file_header').

**Parameters**

`enable` `bool`<br/>
True if events should be exported, otherwise false.



---

## get_export_point_type

Get whether to export 3d point types.
```
qtm.settings.export.tsv.get_export_point_type()
```

**Returns**

`bool` 

---

## set_export_point_type

Set whether to export 3d point types.
```
qtm.settings.export.tsv.set_export_point_type(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 3d point types should be exported, otherwise false.



---

## get_export_file_header

Get whether to export a file header.
```
qtm.settings.export.tsv.get_export_file_header()
```

**Returns**

`bool` 

---

## set_export_file_header

Set whether to export a file header.
```
qtm.settings.export.tsv.set_export_file_header(enable)
```

**Parameters**

`enable` `bool`<br/>
True if a file header should be exported, otherwise false.



---

## get_export_column_header

Get whether to export column headers.
```
qtm.settings.export.tsv.get_export_column_header()
```

**Returns**

`bool` 

---

## set_export_column_header

Set whether to export column headers.
```
qtm.settings.export.tsv.set_export_column_header(enable)
```

Column headers require file header to be exported (see 'set_export_file_header').

**Parameters**

`enable` `bool`<br/>
True if column headers should be exported, otherwise false.



---

## get_null_string

Get the null string.
```
qtm.settings.export.tsv.get_null_string()
```

**Returns**

`string` 

---

## set_null_string

Set the null string.
```
qtm.settings.export.tsv.set_null_string(string)
```

**Parameters**

`string` `string`<br/>
The null string.



---

## get_exclude_unidentified

Get whether to exclude unidentified trajectories.
```
qtm.settings.export.tsv.get_exclude_unidentified()
```

**Returns**

`bool` 

---

## set_exclude_unidentified

Set whether to exclude unidentified trajectories.
```
qtm.settings.export.tsv.set_exclude_unidentified(enable)
```

**Parameters**

`enable` `bool`<br/>
True if unidentified trajectories should be excluded, otherwise false.



---

## get_exclude_empty

Get whether to exclude empty trajectories.
```
qtm.settings.export.tsv.get_exclude_empty()
```

**Returns**

`bool` 

---

## set_exclude_empty

Set whether to exclude empty trajectories.
```
qtm.settings.export.tsv.set_exclude_empty(enable)
```

**Parameters**

`enable` `bool`<br/>
True if empty trajectories should be excluded, otherwise false.



---

## get_exclude_partially_labeled

Get whether to exclude partially labeled frames.
```
qtm.settings.export.tsv.get_exclude_partially_labeled()
```

**Returns**

`bool` 

---

## set_exclude_partially_labeled

Set whether to exclude partially labeled frames.
```
qtm.settings.export.tsv.set_exclude_partially_labeled(enable)
```

This will override the exported range.

**Parameters**

`enable` `bool`<br/>
True if partially labeled frames should be excluded, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.tsv.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

