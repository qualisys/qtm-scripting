# qtm.gui.message

Interface to the messages window.

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

