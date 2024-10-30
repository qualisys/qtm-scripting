# qtm

Interface to the qtm application.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.get_version())
    # {'major': 2023, 'minor': 1, 'build': 7928}
    ```
=== "Lua"
    ``` lua
    print(qtm.get_version()) 
    -- {build = 7928, minor = 1, major = 2023}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/get_version/
    :: {"build":7928,"major":2023,"minor":1}
    ```
## get_version

Get the version number of qtm.
```
qtm.get_version()
```

**Returns**

`{"major": integer, "minor": integer, "build": integer}` 

---

## help

Get the documentation for a module or method.
```
qtm.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

