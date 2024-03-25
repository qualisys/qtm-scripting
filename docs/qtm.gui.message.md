# qtm.gui.message

Interface to the messages window.

=== "Python"
    ``` py
    import qtm
    
    qtm.gui.message.add_message("information message", "detailed information", "info")
    
    qtm.gui.message.add_message("warning message", "detailed information", "warning")
    
    qtm.gui.message.add_message("error message", "detailed information", "error")
    ```
=== "Lua"
    ``` lua
    qtm.gui.message.add_message("information message", "detailed information", "info")
    
    qtm.gui.message.add_message("warning message", "detailed information", "warning")
    
    qtm.gui.message.add_message("error message", "detailed information", "error")
    ```
=== "REST"
    ``` bat
    curl --json "[\"information message\", \"detailed information\", \"info\"]" http://localhost:7979/api/scripting/qtm/gui/message/add_message/
    
    curl --json "[\"warning message\", \"detailed information\", \"warning\"]" http://localhost:7979/api/scripting/qtm/gui/message/add_message/
    
    curl --json "[\"error message\", \"detailed information\", \"error\"]" http://localhost:7979/api/scripting/qtm/gui/message/add_message/
    ```
## add_message

Add a message.
```
qtm.gui.message.add_message(message, details, type)
```

**Parameters**

`message` `string`<br/>
The message (shown in the message log).

`details` `string`<br/>
Detailed information (shown when double-clicking the message).

`type` `"info"|"warning"|"error"`<br/>
The type of message.



---

## help

Get the documentation for a module or method.
```
qtm.gui.message.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

