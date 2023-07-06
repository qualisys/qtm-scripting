# qtm.settings.export.fbx

Access and modify fbx export settings.

=== "Python"
    ``` py
    import qtm
    
    file_format = "binary"
    qtm.settings.export.fbx.set_file_format(file_format)
    print(qtm.settings.export.fbx.get_file_format())
    # binary
    
    qtm.settings.export.fbx.set_export_camera(True)
    print(qtm.settings.export.fbx.get_export_camera())
    # True
    ```
=== "Lua"
    ``` lua
    file_format = "binary"
    qtm.settings.export.fbx.set_file_format(file_format)
    print(qtm.settings.export.fbx.get_file_format())
    -- binary
    
    qtm.settings.export.fbx.set_export_camera(true)
    print(qtm.settings.export.fbx.get_export_camera())
    -- true
    ```
=== "REST"
    ``` bat
    curl --json "[\"binary\"]" http://localhost:7979/api/scripting/qtm/settings/export/fbx/set_file_format/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/fbx/get_file_format/
    :: "binary"
    
    curl --json "[true]" http://localhost:7979/api/scripting/qtm/settings/export/fbx/set_export_camera/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/export/fbx/get_export_camera/
    :: true
    ```
## get_file_format

Get the file format.

**Returns**

`"ascii"|"binary"` 

---

## set_file_format

Set the file format.

**Parameters**

`format` `"ascii"|"binary"`<br/>
The file format.



---

## get_export_optical

Get whether to export opticals.

**Returns**

`bool` 

---

## set_export_optical

Set whether to export opticals.

**Parameters**

`enable` `bool`<br/>
True if opticals should be exported, otherwise false.



---

## get_export_actor

Get whether to export motionbuilder actors.

**Returns**

`bool` 

---

## set_export_actor

Set whether to export motionbuilder actors.

Actors require opticals to be exported (see 'set_export_optical').

**Parameters**

`enable` `bool`<br/>
True if motionbuilder actors should be exported, otherwise false.



---

## get_export_skeleton

Get whether to export skeletons.

**Returns**

`bool` 

---

## set_export_skeleton

Set whether to export skeletons.

**Parameters**

`enable` `bool`<br/>
True if skeletons should be exported, otherwise false.



---

## get_export_character

Get whether to export characters.

**Returns**

`bool` 

---

## set_export_character

Set whether to export characters.

Characters require skeletons to be exported (see 'set_export_skeleton').

**Parameters**

`enable` `bool`<br/>
True if characters should be exported, otherwise false.



---

## get_export_camera

Get whether to export cameras.

**Returns**

`bool` 

---

## set_export_camera

Set whether to export cameras.

**Parameters**

`enable` `bool`<br/>
True if cameras should be exported, otherwise false.



---

## get_export_timecode

Get whether to export timecodes.

**Returns**

`bool` 

---

## set_export_timecode

Set whether to export timecodes.

**Parameters**

`enable` `bool`<br/>
True if timecodes should be exported, otherwise false.



---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

