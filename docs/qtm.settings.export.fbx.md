# qtm.settings.export.fbx

Access and modify fbx export settings.

## get_file_format

Get the file format.
```
qtm.settings.export.fbx.get_file_format()
```

**Returns**

`"ascii"|"binary"` 

---

## set_file_format

Set the file format.
```
qtm.settings.export.fbx.set_file_format(format)
```

**Parameters**

`format` `"ascii"|"binary"`<br/>
The file format.



---

## get_export_optical

Get whether to export opticals.
```
qtm.settings.export.fbx.get_export_optical()
```

**Returns**

`bool` 

---

## set_export_optical

Set whether to export opticals.
```
qtm.settings.export.fbx.set_export_optical(enable)
```

**Parameters**

`enable` `bool`<br/>
True if opticals should be exported, otherwise false.



---

## get_export_actor

Get whether to export motionbuilder actors.
```
qtm.settings.export.fbx.get_export_actor()
```

**Returns**

`bool` 

---

## set_export_actor

Set whether to export motionbuilder actors.
```
qtm.settings.export.fbx.set_export_actor(enable)
```

Actors require opticals to be exported (see 'set_export_optical').

**Parameters**

`enable` `bool`<br/>
True if motionbuilder actors should be exported, otherwise false.



---

## get_export_skeleton

Get whether to export skeletons.
```
qtm.settings.export.fbx.get_export_skeleton()
```

**Returns**

`bool` 

---

## set_export_skeleton

Set whether to export skeletons.
```
qtm.settings.export.fbx.set_export_skeleton(enable)
```

**Parameters**

`enable` `bool`<br/>
True if skeletons should be exported, otherwise false.



---

## get_export_character

Get whether to export characters.
```
qtm.settings.export.fbx.get_export_character()
```

**Returns**

`bool` 

---

## set_export_character

Set whether to export characters.
```
qtm.settings.export.fbx.set_export_character(enable)
```

Characters require skeletons to be exported (see 'set_export_skeleton').

**Parameters**

`enable` `bool`<br/>
True if characters should be exported, otherwise false.



---

## get_export_camera

Get whether to export cameras.
```
qtm.settings.export.fbx.get_export_camera()
```

**Returns**

`bool` 

---

## set_export_camera

Set whether to export cameras.
```
qtm.settings.export.fbx.set_export_camera(enable)
```

**Parameters**

`enable` `bool`<br/>
True if cameras should be exported, otherwise false.



---

## get_export_timecode

Get whether to export timecodes.
```
qtm.settings.export.fbx.get_export_timecode()
```

**Returns**

`bool` 

---

## set_export_timecode

Set whether to export timecodes.
```
qtm.settings.export.fbx.set_export_timecode(enable)
```

**Parameters**

`enable` `bool`<br/>
True if timecodes should be exported, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.export.fbx.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

