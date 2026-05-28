# qtm.file

Various methods related to measurement files.

=== "Python"
    ``` py
    import qtm
    
    qtm.file.open(r"C:\Users\<username>\Documents\Project\Data\File1.qtm")
    qtm.file.is_open()
    # True
    qtm.file.is_dirty()
    # False
    qtm.file.get_path()
    # 'C:\\Users\\<username>\\Documents\\Project\\Data\\File1.qtm'
    qtm.file.get_capture_time()
    # {'year': 2019, 'month': 2, 'day': 13, 'hour': 18, 'minute': 3, 'second': 6, 'millisecond': 585}
    qtm.file.get_capture_version()
    # '2019.1 (build 4400)'
    qtm.file.get_capture_license()
    # 'Qualisys Internal'
    
    qtm.file.export_tsv(r"C:\temp\exported_file.tsv")
    qtm.file.export_c3d(r"C:\temp\exported_file.c3d")
    qtm.file.export_fbx(r"C:\temp\exported_file.fbx")
    
    qtm.data.object.trajectory.add_trajectory()
    qtm.file.is_dirty()
    # True
    
    qtm.file.save()
    qtm.file.is_dirty()
    # False
    
    qtm.file.save_as(r"C:\Users\<username>\Documents\Project\Data\File2.qtm")
    qtm.file.get_path()
    # 'C:\\Users\\<username>\\Documents\\Project\\Data\\File2.qtm'
    
    qtm.file.close()
    qtm.file.is_open()
    # False
    ```
=== "Lua"
    ``` lua
    qtm.file.open([[C:\Users\<username>\Documents\Project\Data\File1.qtm]])
    qtm.file.is_open()
    -- true
    qtm.file.is_dirty()
    -- false
    qtm.file.get_path()
    -- C:\Users\<username>\Documents\Project\Data\File1.qtm
    qtm.file.get_capture_time()
    -- {hour = 18, month = 2, year = 2019, minute = 3, second = 6, millisecond = 585, day = 13}
    qtm.file.get_capture_version()
    -- 2019.1 (build 4400)
    qtm.file.get_capture_license()
    -- Qualisys Internal
    
    qtm.file.export_tsv([[C:\temp\exported_file.tsv]])
    qtm.file.export_c3d([[C:\temp\exported_file.c3d]])
    qtm.file.export_fbx([[C:\temp\exported_file.fbx]])
    
    qtm.data.object.trajectory.add_trajectory()
    qtm.file.is_dirty()
    -- true
    
    qtm.file.save()
    qtm.file.is_dirty()
    -- false
    
    qtm.file.save_as([[C:\Users\<username>\Documents\Project\Data\File2.qtm]])
    qtm.file.get_path()
    -- C:\Users\<username>\Documents\Project\Data\File2.qtm
    
    qtm.file.close()
    qtm.file.is_open()
    -- false
    ```
=== "REST"
    ``` bat
    set path_1=\"C:\\Users\\^<username^>\\Documents\\Project\\Data\\File1.qtm\"
    curl --json "[%path_1%]" http://localhost:7979/api/scripting/qtm/file/open/
    curl --json "" http://localhost:7979/api/scripting/qtm/file/is_open/
    :: true
    curl --json "" http://localhost:7979/api/scripting/qtm/file/is_dirty/
    :: false
    curl --json "" http://localhost:7979/api/scripting/qtm/file/get_path/
    :: "C:\\Users\\<username>\\Documents\\Project\\Data\\File1.qtm"
    curl --json "" http://localhost:7979/api/scripting/qtm/file/get_capture_time/
    :: {"day":13,"hour":18,"millisecond":585,"minute":3,"month":2,"second":6,"year":2019}
    curl --json "" http://localhost:7979/api/scripting/qtm/file/get_capture_version/
    :: "2019.1 (build 4400)"
    curl --json "" http://localhost:7979/api/scripting/qtm/file/get_capture_license/
    :: "Qualisys Internal"
    
    set out_tsv=\"C:\\temp\\exported_file.tsv\"
    curl --json "[%out_tsv%]" http://localhost:7979/api/scripting/qtm/file/export_tsv/
    set out_c3d=\"C:\\temp\\exported_file.c3d\"
    curl --json "[%out_c3d%]" http://localhost:7979/api/scripting/qtm/file/export_c3d/
    set out_fbx=\"C:\\temp\\exported_file.fbx\"
    curl --json "[%out_fbx%]" http://localhost:7979/api/scripting/qtm/file/export_fbx/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/trajectory/add_trajectory/
    curl --json "" http://localhost:7979/api/scripting/qtm/file/is_dirty/
    :: true
    
    curl --json "" http://localhost:7979/api/scripting/qtm/file/save/
    curl --json "" http://localhost:7979/api/scripting/qtm/file/is_dirty/
    :: false
    
    set path_2=\"C:\\Users\\^<username^>\\Documents\\Project\\Data\\File2.qtm\"
    curl --json "[%path_2%]" http://localhost:7979/api/scripting/qtm/file/save_as/
    curl --json "" http://localhost:7979/api/scripting/qtm/file/get_path/
    :: "C:\\Users\\<username>\\Documents\\Project\\Data\\File2.qtm"
    
    curl --json "" http://localhost:7979/api/scripting/qtm/file/close/
    curl --json "" http://localhost:7979/api/scripting/qtm/file/is_open/
    :: false
    
    ```
## open

Open a measurement file.
```
qtm.file.open(path)
```

**Parameters**

`path` `string`<br/>
The file path.



---

## save

Save the current measurement file.
```
qtm.file.save()
```

This method requires that the file is persisted.


---

## save_as

Save the current measurement file to a given path.
```
qtm.file.save_as(path)
```

**Parameters**

`path` `string`<br/>
The file path.



---

## close

Close the current measurement file (or preview).
```
qtm.file.close()
```

Ongoing capture/processing will be canceled and any unsaved changes will be lost.


---

## is_open

Get whether a measurement file (or preview) is open.
```
qtm.file.is_open()
```

**Returns**

`bool` 

---

## is_dirty

Get whether the current measurement file is dirty (has unsaved changes).
```
qtm.file.is_dirty()
```

**Returns**

`bool` 

---

## is_persisted

Get whether the current measurement file is persisted (has ever been written to disk).
```
qtm.file.is_persisted()
```

**Returns**

`bool` 

---

## get_path

Get the path of the current measurement file.
```
qtm.file.get_path()
```

**Returns**

`string?` The path (or null, if the file is not persisted).

---

## get_capture_time

Get the start time of the capture of the current measurement file.
```
qtm.file.get_capture_time()
```

**Returns**

`{"year": integer, "month": integer, "day": integer, "hour": integer, "minute": integer, "second": integer, "millisecond": integer}` 

---

## get_capture_version

Get the qtm version used to capture the current measurement file.
```
qtm.file.get_capture_version()
```

**Returns**

`string?` The version (or null, if the file does not contain this info).

---

## get_capture_license

Get the license used to capture the current measurement file.
```
qtm.file.get_capture_license()
```

**Returns**

`string?` The license (or null, if the file does not contain this info).

---

## export_tsv

Export the current measurement as a tsv file.
```
qtm.file.export_tsv(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.tsv).



---

## export_c3d

Export the current measurement as a c3d file.
```
qtm.file.export_c3d(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.c3d).



---

## export_mat

Export the current measurement as a mat file.
```
qtm.file.export_mat(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.mat).



---

## export_json

Export the current measurement as a json file.
```
qtm.file.export_json(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.json).



---

## export_fbx

Export the current measurement as an fbx file.
```
qtm.file.export_fbx(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.fbx).



---

## export_trc

Export the current measurement as a trc file.
```
qtm.file.export_trc(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.trc).



---

## export_sto

Export the current measurement as an sto file.
```
qtm.file.export_sto(path)
```

**Parameters**

`path` `string`<br/>
The output file path (.sto).



---

## help

Get the documentation for a module or method.
```
qtm.file.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

