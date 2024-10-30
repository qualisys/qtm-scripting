# qtm.gui.terminal

Interface to the terminal window.

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

