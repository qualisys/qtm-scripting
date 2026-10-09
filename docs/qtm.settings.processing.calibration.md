# qtm.settings.processing.calibration

Access and modify calibration processing settings.

=== "Python"
    ``` py
    import qtm
    
    qtm.settings.processing.calibration.get_calibration_file("project")
    # '20230413_093052.qca'
    
    qtm.settings.processing.calibration.set_calibration_file("project", "C:\\Users\\<username>\\Documents\\Project\\Calibrations\\20230413_093551.qca")
    
    qtm.settings.processing.calibration.get_calibration_time("project")
    # {'year': 2023, 'month': 4, 'day': 13, 'hour': 9, 'minute': 35, 'second': 51, 'millisecond': 0}
    
    qtm.settings.processing.calibration.get_calibration_results("project")
    # {'cameras': [{'transform': [[0.9336454326674574, 0.06239040051233219, -0.3527231832232, 1582.4917584007865], ...], 'point_count': 1758, 'average_residual': 1.9353868571146682, ...}, ...], ...}
    
    qtm.settings.processing.calibration.get_settings("project")
    # {'calibration_file': '20230413_093551.qca', 'calibration_time': {'year': 2023, 'month': 4, 'day': 13, 'hour': 9, 'minute': 35, 'second': 51, 'millisecond': 0}, 'calibration_results': ...}
    
    qtm.settings.processing.calibration.set_settings("project", {'calibration_file': "C:\\Users\\<username>\\Documents\\Project\\Calibrations\\20230413_093936.qca"})
    ```
=== "Lua"
    ``` lua
    qtm.settings.processing.calibration.get_calibration_file("project")
    -- 20230413_093052.qca
    
    qtm.settings.processing.calibration.set_calibration_file("project", "C:\\Users\\<username>\\Documents\\Project\\Calibrations\\20230413_093551.qca")
    
    qtm.settings.processing.calibration.get_calibration_time("project")
    -- {hour = 9, year = 2023, millisecond = 0, second = 51, minute = 35, day = 13, month = 4}
    
    qtm.settings.processing.calibration.get_calibration_results("project")
    -- {cameras = {{point_count = 1758, average_residual = 1.9353868571147, transform = {{0.93364543266746, 0.062390400512332, -0.3527231832232, 1582.4917584008}, ...}, ...}, ...}, ...}
    
    qtm.settings.processing.calibration.get_settings("project")
    -- {calibration_time = {hour = 9, year = 2023, millisecond = 0, second = 51, minute = 35, day = 13, month = 4}, calibration_results = {cameras = {{point_count = 1758, ...}, ...}, ...}, ...}
    
    qtm.settings.processing.calibration.set_settings("project", {calibration_file = "C:\\Users\\<username>\\Documents\\Project\\Calibrations\\20230413_093936.qca"})
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/get_calibration_file
    :: "20230413_093052.qca"
    
    set calibration_file=\"C:\\Users\\^<username^>\\Documents\\Project\\Calibrations\\20230413_093551.qca\"
    curl --json "[\"project\", %calibration_file%]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/set_calibration_file
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/get_calibration_time
    :: {"day":13,"hour":9,"millisecond":0,"minute":35,"month":4,"second":51,"year":2023}
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/get_calibration_results
    :: {"cameras":[{"average_residual":1.9353868571146682,"message":null,"point_count":1758,"transform":[[0.93364543266745736,0.062390400512332189,...],...]},...],...}
    
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/get_settings
    :: {"calibration_file":"20230413_093551.qca","calibration_results":{"cameras":[{"average_residual":1.9353868571146682,"message":null,"point_count":1758,"transform":[[0.93364543266745736,0.062390400512332189,-0.35272318322320001,1582.4917584007865],...]},...],...},...}
    
    curl --json "[\"project\", {\"calibration_file\":\"C:\\Users\\<username>\\Documents\\Project\\Calibrations\\20230413_093936.qca\"}]" http://localhost:7979/api/scripting/qtm/settings/processing/calibration/set_settings
    ```
## get_calibration_file

Get the current calibration file.
```
qtm.settings.processing.calibration.get_calibration_file(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`string` 

---

## set_calibration_file

Set the current calibration file.
```
qtm.settings.processing.calibration.set_calibration_file(source, path)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`path` `string`<br/>
The calibration file path.



---

## get_calibration_time

Get the start time of the current calibration.
```
qtm.settings.processing.calibration.get_calibration_time(source)
```

This method requires a calibration file (see 'set_calibration_file').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"year": integer, "month": integer, "day": integer, "hour": integer, "minute": integer, "second": integer, "millisecond": integer}` 

---

## get_calibration_results

Get the current calibration results.
```
qtm.settings.processing.calibration.get_calibration_results(source)
```

This method requires a calibration file (see 'set_calibration_file').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"cameras": [{"transform": mat4x4f?, "point_count": integer?, "average_residual": float?, "message": string?}], "wand": {"standard_deviation": float}?, "passed": bool}` 

---

## get_settings

Get all settings.
```
qtm.settings.processing.calibration.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"calibration_file": string?, "calibration_time": {"year": integer, "month": integer, "day": integer, "hour": integer, "minute": integer, "second": integer, "millisecond": integer}?, "calibration_results": {"cameras": [{"transform": mat4x4f?, "point_count": integer?, "average_residual": float?, "message": string?}], "wand": {"standard_deviation": float}?, "passed": bool}?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.calibration.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"calibration_file": string?, "calibration_time": {"year": integer, "month": integer, "day": integer, "hour": integer, "minute": integer, "second": integer, "millisecond": integer}?, "calibration_results": {"cameras": [{"transform": mat4x4f?, "point_count": integer?, "average_residual": float?, "message": string?}], "wand": {"standard_deviation": float}?, "passed": bool}?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.calibration.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

