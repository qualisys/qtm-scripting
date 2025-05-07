# qtm.gui.dialog

Functions for showing various dialogs.

=== "Python"
    ``` py
    import qtm
    
    title = "Message Box Example"
    message = "Click a button!"
    buttons = ["Yes", "No", "Maybe"]
    icon = "information"
    print(qtm.gui.dialog.show_message_box(title, message, buttons, icon))
    # Maybe
    
    title = "Open File Dialog Example"
    filters = ["Text files (*.txt)", "All files (*.*)"]
    multiselect = True
    directory = "C:\\"
    print(qtm.gui.dialog.show_open_file_dialog(title, filters, multiselect, directory))
    # ['C:\\Directory\\File1.txt', 'C:\\Directory\\File2.txt']
    
    title = "Save File Dialog Example"
    filters = ["QTM files (*.qtm)"]
    filename = "MyFile"
    directory = "C:\\"
    print(qtm.gui.dialog.show_save_file_dialog(title, filters, filename, directory))
    # C:\Directory\MyFile.qtm
    
    title = "String Input Dialog Example"
    message = "Write something!"
    input = "Lorem ipsum"
    print(qtm.gui.dialog.show_string_input_dialog(title, message, input))
    # Lorem ipsum dolor sit amet
    ```
=== "Lua"
    ``` lua
    title = "Message Box Example"
    message = "Click a button!"
    buttons = {"Yes", "No", "Maybe"}
    icon = "information"
    print(qtm.gui.dialog.show_message_box(title, message, buttons, icon))
    -- Maybe
    
    title = "Open File Dialog Example"
    filters = {"Text files (*.txt)", "All files (*.*)"}
    multiselect = true
    directory = "C:\\"
    print(qtm.gui.dialog.show_open_file_dialog(title, filters, multiselect, directory))
    -- {"C:\Directory\File1.txt", "C:\Directory\File2.txt"}
    
    title = "Save File Dialog Example"
    filters = {"QTM files (*.qtm)"}
    filename = "MyFile"
    directory = "C:\\"
    print(qtm.gui.dialog.show_save_file_dialog(title, filters, filename, directory))
    -- C:\Directory\MyFile.qtm
    
    title = "String Input Dialog Example"
    message = "Write something!"
    input = "Lorem ipsum"
    print(qtm.gui.dialog.show_string_input_dialog(title, message, input))
    -- Lorem ipsum dolor sit amet
    ```
=== "REST"
    ``` bat
    curl --json "[\"Message Box Example\", \"Click a button!\", [\"Yes\", \"No\", \"Maybe\"], \"information\"]" http://localhost:7979/api/scripting/qtm/gui/dialog/show_message_box/
    :: "Maybe"
    
    curl --json "[\"Open File Dialog Example\", [\"Text files (*.txt)\", \"All files (*.*)\"], true, \"C:\\\\\"]" http://localhost:7979/api/scripting/qtm/gui/dialog/show_open_file_dialog/
    :: ["C:\\Directory\\File1.txt","C:\\Directory\\File2.txt"]
    
    curl --json "[\"Save File Dialog Example\", [\"QTM files (*.qtm)\"], \"MyFile\", \"C:\\\\\"]" http://localhost:7979/api/scripting/qtm/gui/dialog/show_save_file_dialog/
    :: "C:\\Directory\\MyFile.qtm"
    
    curl --json "[\"String Input Dialog Example\", \"Write something!\", \"Lorem ipsum\"]" http://localhost:7979/api/scripting/qtm/gui/dialog/show_string_input_dialog/
    :: "Lorem ipsum dolor sit amet"
    ```
## show_message_box

Show a message box.
```
qtm.gui.dialog.show_message_box(title, message, buttons, icon?)
```

**Parameters**

`title` `string`<br/>
The title of the message box.

`message` `string`<br/>
The message shown in the message box.

`buttons` `[string]`<br/>
The button texts.

`icon` `"information"|"question"|"warning"|"error"?`<br/>
The icon shown in the message box (if null, the information icon will be used).


**Returns**

`string` The text of the clicked button.

---

## show_open_file_dialog

Show an open file dialog.
```
qtm.gui.dialog.show_open_file_dialog(title?, filters?, multiselect?, directory?)
```

**Parameters**

`title` `string?`<br/>
The title of the dialog (if null, 'Open' will be used).

`filters` `[string]?`<br/>
The file type filters, e.g. 'Bitmap files (*.bmp;*.dib)' (if null, 'All files (*.*)' will be used).

`multiselect` `bool?`<br/>
True if multiple files can be selected, otherwise false (if null, multiselect will be disabled).

`directory` `string?`<br/>
The default directory (if null, the default directory will be the most recently used).


**Returns**

`[string]?` The selected file paths (or null, if the dialog was canceled).

---

## show_save_file_dialog

Show a save file dialog.
```
qtm.gui.dialog.show_save_file_dialog(title?, filters?, filename?, directory?)
```

**Parameters**

`title` `string?`<br/>
The title of the dialog (if null, 'Save As' will be used).

`filters` `[string]?`<br/>
The file type filters, e.g. 'Bitmap files (*.bmp;*.dib)' (if null, 'All files (*.*)' will be used).

`filename` `string?`<br/>
The default filename (if null, the default filename will be empty).

`directory` `string?`<br/>
The default directory (if null, the default directory will be the most recently used).


**Returns**

`string?` The selected file path (or null, if the dialog was canceled).

---

## show_string_input_dialog

Display a string input dialog.
```
qtm.gui.dialog.show_string_input_dialog(title, message, input?)
```

**Parameters**

`title` `string`<br/>
The title of the dialog.

`message` `string`<br/>
The message shown in the dialog.

`input` `string?`<br/>
The default input (if null, the default input will be empty).


**Returns**

`string?` The string entered into the dialog (or null, if the dialog was canceled).

---

## help

Get the documentation for a module or method.
```
qtm.gui.dialog.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

