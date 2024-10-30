# qtm.settings.export.mat

Access and modify mat export settings.

## get_export_3d

Get whether to export 3d data.
```
qtm.settings.export.mat.get_export_3d()
```

**Returns**

`bool` 

---

## set_export_3d

Set whether to export 3d data.
```
qtm.settings.export.mat.set_export_3d(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 3d data should be exported, otherwise false.



---

## get_export_6d

Get whether to export 6dof data.
```
qtm.settings.export.mat.get_export_6d()
```

**Returns**

`bool` 

---

## set_export_6d

Set whether to export 6dof data.
```
qtm.settings.export.mat.set_export_6d(enable)
```

**Parameters**

`enable` `bool`<br/>
True if 6dof data should be exported, otherwise false.



---

## get_export_analog

Get whether to export analog data.
```
qtm.settings.export.mat.get_export_analog()
```

**Returns**

`bool` 

---

## set_export_analog

Set whether to export analog data.
```
qtm.settings.export.mat.set_export_analog(enable)
```

**Parameters**

`enable` `bool`<br/>
True if analog data should be exported, otherwise false.



---

## get_export_force

Get whether to export force data.
```
qtm.settings.export.mat.get_export_force()
```

**Returns**

`bool` 

---

## set_export_force

Set whether to export force data.
```
qtm.settings.export.mat.set_export_force(enable)
```

**Parameters**

`enable` `bool`<br/>
True if force data should be exported, otherwise false.



---

## get_export_eye

Get whether to export eye data.
```
qtm.settings.export.mat.get_export_eye()
```

**Returns**

`bool` 

---

## set_export_eye

Set whether to export eye data.
```
qtm.settings.export.mat.set_export_eye(enable)
```

**Parameters**

`enable` `bool`<br/>
True if eye data should be exported, otherwise false.



---

## get_export_skeleton

Get whether to export skeleton data.
```
qtm.settings.export.mat.get_export_skeleton()
```

**Returns**

`bool` 

---

## set_export_skeleton

Set whether to export skeleton data.
```
qtm.settings.export.mat.set_export_skeleton(enable)
```

**Parameters**

`enable` `bool`<br/>
True if skeleton data should be exported, otherwise false.



---

## get_export_timecode

Get whether to export timecodes.
```
qtm.settings.export.mat.get_export_timecode()
```

**Returns**

`bool` 

---

## set_export_timecode

Set whether to export timecodes.
```
qtm.settings.export.mat.set_export_timecode(enable)
```

**Parameters**

`enable` `bool`<br/>
True if timecodes should be exported, otherwise false.



---

## get_export_event

Get whether to export events.
```
qtm.settings.export.mat.get_export_event()
```

**Returns**

`bool` 

---

## set_export_event

Set whether to export events.
```
qtm.settings.export.mat.set_export_event(enable)
```

**Parameters**

`enable` `bool`<br/>
True if events should be exported, otherwise false.



---

## get_exclude_unidentified

Get whether to exclude unidentified trajectories.
```
qtm.settings.export.mat.get_exclude_unidentified()
```

**Returns**

`bool` 

---

## set_exclude_unidentified

Set whether to exclude unidentified trajectories.
```
qtm.settings.export.mat.set_exclude_unidentified(enable)
```

**Parameters**

`enable` `bool`<br/>
True if unidentified trajectories should be excluded, otherwise false.



---

## get_skeleton_reference_frame

Get the skeleton reference frame.
```
qtm.settings.export.mat.get_skeleton_reference_frame()
```

**Returns**

`"global"|"local"` 

---

## set_skeleton_reference_frame

Set the skeleton reference frame.
```
qtm.settings.export.mat.set_skeleton_reference_frame(frame)
```

This method requires skeletons to be exported (see 'set_export_skeleton').

**Parameters**

`frame` `"global"|"local"`<br/>
The skeleton reference frame.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.mat.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

