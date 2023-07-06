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
    
    set auto_save_directory=\"C:\\Users\\<username>\\Documents\\Project\\AutoSave\\\"
    curl --json "[%auto_save_directory%]" http://localhost:7979/api/scripting/qtm/settings/camera/set_auto_save_directory/
    curl --json "" http://localhost:7979/api/scripting/qtm/settings/directory/get_auto_save_directory/
    :: "C:\\Users\\<username>\\Documents\\Project\\AutoSave\\"
    ```
## get_project_directory

Get the project directory path.

**Returns**

`string` 

---

## get_calibration_directory

Get the calibration directory path.

**Returns**

`string` 

---

## set_calibration_directory

Set the calibration directory path.

**Parameters**

`directory` `string`<br/>
The calibration directory path.



---

## get_aim_directory

Get the aim model directory path.

**Returns**

`string` 

---

## set_aim_directory

Set the aim model directory path.

**Parameters**

`directory` `string`<br/>
The aim model directory path.



---

## get_default_project_directory

Get the default project directory path.

**Returns**

`string` 

---

## set_default_project_directory

Set the default project directory path.

**Parameters**

`directory` `string`<br/>
The default project directory path.



---

## get_temp_video_directory

Get the temporary video directory path.

**Returns**

`string` 

---

## set_temp_video_directory

Set the temporary video directory path.

**Parameters**

`directory` `string`<br/>
The temporary video directory path.



---

## get_auto_save_directory

Get the auto save directory path.

**Returns**

`string` 

---

## set_auto_save_directory

Set the auto save directory path.

**Parameters**

`directory` `string`<br/>
The auto save directory path.



---

## get_linearization_directory

Get the linearization directory path.

**Returns**

`string` 

---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

