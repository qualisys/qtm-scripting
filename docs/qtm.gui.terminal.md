# qtm.gui.terminal

Interface to the terminal window.

=== "Python"
    ``` py
    import qtm
    
    qtm.gui.terminal.clear()
    
    qtm.gui.terminal.write("message in terminal")
    ```
=== "Lua"
    ``` lua
    qtm.gui.terminal.clear()
    
    qtm.gui.terminal.write("message in terminal")
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/gui/terminal/clear/
    
    curl --json "[\"message in terminal\"]" http://localhost:7979/api/scripting/qtm/gui/terminal/write/
    ```
## clear

Clear the terminal.
```
qtm.gui.terminal.clear()
```

This method is used internally by the global 'clear' function.


---

## write

Write text in the terminal.
```
qtm.gui.terminal.write(text)
```

This method is used internally by the global 'print' function.

**Parameters**

`text` `string`<br/>
The text to write.



---

## help

Get the documentation for a module or method.
```
qtm.gui.terminal.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

