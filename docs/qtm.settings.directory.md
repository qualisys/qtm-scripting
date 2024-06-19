# qtm.settings.directory

Access and modify directory settings.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.settings.directory.get_project_directory())
    # C:\Users\<username>\Documents\Project\
    
    print(qtm.settings.directory.get_calibration_directory())
    # C:\Users\<username>\Documents\Project\Calibrations\
    
    print(qtm.settings.directory.get_auto_save_directory())
    # C:\Users\<username>\AppData\Local\Temp\
    
    auto_save_directory = "C:/Users/<username>/Documents/Project/AutoSave/"
    qtm.settings.directory.set_auto_save_directory(auto_save_directory)
    print(qtm.settings.directory.get_auto_save_directory())
    # C:\Users\<username>\Documents\Project\AutoSave\
    ```
=== "Lua"
    ``` lua
    print(qtm.settings.directory.get_project_directory())
    -- C:\Users\<username>\Documents\Project\
    
    print(qtm.settings.directory.get_calibration_directory())
    -- C:\Users\<username>\Documents\Project\Calibrations\
    
    print(qtm.settings.directory.get_auto_save_directory())
    -- C:\Users\<username>\AppData\Local\Temp\
    
    auto_save_directory = "C:/Users/<username>/Documents/Project/AutoSave/"
    qtm.settings.directory.set_auto_save_directory(auto_save_directory)
    print(qtm.settings.directory.get_auto_save_directory())
    -- C:\Users\<username>\Documents\Project\AutoSave\
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/directory/get_project_directory/
    :: "C:\\Users\\<username>\\Documents\\Project\\"
    
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/directory/get_calibration_directory/
    :: "C:\\Users\\<username>\\Documents\\Project\\Calibrations\\"
    
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/directory/get_auto_save_directory/
    :: "C:\\Users\\<username>\\AppData\\Local\\Temp\\"
    
    set auto_save_directory=\"C:\\Users\\^<username^>\\Documents\\Project\\AutoSave\\\\\"
    curl --json "[%auto_save_directory%]" http://localhost:7979/api/scripting/qtm/settings/directory/set_auto_save_directory/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/directory/get_auto_save_directory/
    :: "C:\\Users\\<username>\\Documents\\Project\\AutoSave\\"
    ```
## get_project_directory

Get the project directory path.
```
qtm.settings.directory.get_project_directory()
```

**Returns**

`string` 

---

## get_calibration_directory

Get the calibration directory path.
```
qtm.settings.directory.get_calibration_directory()
```

**Returns**

`string` 

---

## set_calibration_directory

Set the calibration directory path.
```
qtm.settings.directory.set_calibration_directory(directory)
```

**Parameters**

`directory` `string`<br/>
The calibration directory path.



---

## get_aim_directory

Get the aim model directory path.
```
qtm.settings.directory.get_aim_directory()
```

**Returns**

`string` 

---

## set_aim_directory

Set the aim model directory path.
```
qtm.settings.directory.set_aim_directory(directory)
```

**Parameters**

`directory` `string`<br/>
The aim model directory path.



---

## get_default_project_directory

Get the default project directory path.
```
qtm.settings.directory.get_default_project_directory()
```

**Returns**

`string` 

---

## set_default_project_directory

Set the default project directory path.
```
qtm.settings.directory.set_default_project_directory(directory)
```

**Parameters**

`directory` `string`<br/>
The default project directory path.



---

## get_temp_video_directory

Get the temporary video directory path.
```
qtm.settings.directory.get_temp_video_directory()
```

**Returns**

`string` 

---

## set_temp_video_directory

Set the temporary video directory path.
```
qtm.settings.directory.set_temp_video_directory(directory)
```

**Parameters**

`directory` `string`<br/>
The temporary video directory path.



---

## get_auto_save_directory

Get the auto save directory path.
```
qtm.settings.directory.get_auto_save_directory()
```

**Returns**

`string` 

---

## set_auto_save_directory

Set the auto save directory path.
```
qtm.settings.directory.set_auto_save_directory(directory)
```

**Parameters**

`directory` `string`<br/>
The auto save directory path.



---

## get_linearization_directory

Get the linearization directory path.
```
qtm.settings.directory.get_linearization_directory()
```

**Returns**

`string` 

---

## help

Get the documentation for a module or method.
```
qtm.settings.directory.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

