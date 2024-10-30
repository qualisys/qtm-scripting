# qtm.gui

Control and customize the graphical user interface.

=== "Python"
    ``` py
    import qtm
    
    def my_function():
        qtm.gui.terminal.write("my_function() was called")
    
    # - List all available built-in commands
    print(qtm.gui.get_commands("builtin"))
    # ['save_file_as', 'generate_aim_model_from_multiple_files', 'swap_trajectory_current_part', ... ...
    
    # - List all available user commands
    print(qtm.gui.get_commands("user"))
    # []
    
    # - Add a user command
    my_command_name = "my_command"
    qtm.gui.add_command(my_command_name)
    
    # - List all available user commands
    print(qtm.gui.get_commands("user"))
    # ['my_command']
    
    # - Set command execute function
    qtm.gui.set_command_execute_function(my_command_name, my_function)
    
    # - Send command
    qtm.gui.send_command(my_command_name)
    # my_function() was called
    
    # - Set shortcut to a command
    shortcut = {"ctrl": True, "alt": False, "shift": True, "key": "z"}
    qtm.gui.set_accelerator(shortcut, my_command_name)
    
    # - Pressing "ctrl+shift+z":
    # my_function() was called
    
    # - Add a menu in the main menu
    menu_name = "My menu"
    my_menu_handle = qtm.gui.insert_menu_submenu(None, menu_name)
    
    # - Add a menu button in "My menu" and connect it to "my_command"
    menu_first_button_name = "User command: {}".format(my_command_name)
    qtm.gui.insert_menu_button(my_menu_handle, menu_first_button_name, my_command_name)
    
    # - Add a submenu in "My menu"
    submenu_name = "My submenu"
    my_submenu_item_handle = qtm.gui.insert_menu_submenu(my_menu_handle, submenu_name)
    
    # - Add a menu button in the submenu "My submenu" and connect it to the built-in command "add_event".
    add_event_command_name = "add_event"
    menu_second_button_name = "Built-in command: {}".format(add_event_command_name)
    qtm.gui.insert_menu_button(my_submenu_item_handle, menu_second_button_name, add_event_command_name)
    
    # - Add a separator between the button "My first button" and submenu "My submenu"
    menu_index = 1
    qtm.gui.insert_menu_separator(my_menu_handle, menu_index)
    ```
=== "Lua"
    ``` lua
    function my_function()
        qtm.gui.terminal.write("my_function() was called")
    end
    
    -- - List all available built-in commands
    print(qtm.gui.get_commands("builtin"))
    -- {"save_file_as", "generate_aim_model_from_multiple_files", "swap_trajectory_current_part", ... ...
    
    -- - List all available user commands
    print(qtm.gui.get_commands("user"))
    -- {}
    
    -- - Add a user command
    my_command_name = "my_command"
    qtm.gui.add_command(my_command_name)
    
    -- - List all available user commands
    print(qtm.gui.get_commands("user"))
    -- {"my_command"}
    
    -- - Set command execute function
    qtm.gui.set_command_execute_function(my_command_name, my_function)
    
    -- - Send command
    qtm.gui.send_command(my_command_name)
    -- my_function() was called
    
    -- - Set shortcut to a command
    shortcut = {ctrl = true, alt = false, shift = true, key = "z"}
    qtm.gui.set_accelerator(shortcut, my_command_name)
    
    -- - Pressing "ctrl+shift+z":
    -- my_function() was called
    
    -- - Add a menu in the main menu
    menu_name = "My menu"
    my_menu_handle = qtm.gui.insert_menu_submenu(nil, menu_name)
    
    -- - Add a menu button in "My menu" and connect it to "my_command"
    menu_first_button_name = string.format("User command: %s", my_command_name)
    qtm.gui.insert_menu_button(my_menu_handle, menu_first_button_name, my_command_name)
    
    -- - Add a submenu in "My menu"
    submenu_name = "My submenu"
    my_submenu_item_handle = qtm.gui.insert_menu_submenu(my_menu_handle, submenu_name)
    
    -- - Add a menu button in the submenu "My submenu" and connect it to the built-in command "add_event".
    add_event_command_name = "add_event"
    menu_second_button_name = string.format("Built-in command: %s", add_event_command_name)
    
    qtm.gui.insert_menu_button(my_submenu_item_handle, menu_second_button_name, add_event_command_name)
    
    -- - Add a separator between the button "My first button" and submenu "My submenu"
    menu_index = 1
    qtm.gui.insert_menu_separator(my_menu_handle, menu_index)
    ```
## add_command

Add a command.
```
qtm.gui.add_command(command)
```

The command will be added as a user command. Use 'set_command_execute_function' and 'set_command_update_function' to set the behavior of the command (by default, it will be enabled and do nothing).

**Parameters**

`command` `string`<br/>
The command.



---

## get_commands

Get the available commands.
```
qtm.gui.get_commands(type?)
```

**Parameters**

`type` `"builtin"|"user"?`<br/>
The command type to get (if null, all command types will be returned).


**Returns**

`[string]` 

---

## send_command

Send a command.
```
qtm.gui.send_command(command)
```

This is equivalent to clicking a button. Note that if the update function of the command returns false (equivalent to a button being grey/disabled) the command will not be executed.

**Parameters**

`command` `string`<br/>
The command to send (for a list of available commands, see 'get_commands').



---

## set_accelerator

Set an accelerator (hotkey/shortcut) for a command.
```
qtm.gui.set_accelerator(accelerator, command)
```

If the accelerator already exists for a different command, it will be overwritten.

**Parameters**

`accelerator` `{"ctrl": bool, "alt": bool, "shift": bool, "key": "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"a"|"b"|"c"|"d"|"e"|"f"|"g"|"h"|"i"|"j"|"k"|"l"|"m"|"n"|"o"|"p"|"q"|"r"|"s"|"t"|"u"|"v"|"w"|"x"|"y"|"z"|"f1"|"f2"|"f3"|"f4"|"f5"|"f6"|"f7"|"f8"|"f9"|"f10"|"f11"|"f12"|"f13"|"f14"|"f15"|"f16"|"f17"|"f18"|"f19"|"f20"|"f21"|"f22"|"f23"|"f24"|"numpad_0"|"numpad_1"|"numpad_2"|"numpad_3"|"numpad_4"|"numpad_5"|"numpad_6"|"numpad_7"|"numpad_8"|"numpad_9"|"escape"|"backspace"|"tab"|"clear"|"enter"|"pause"|"insert"|"delete"|"home"|"end"|"page_up"|"page_down"|"left"|"right"|"up"|"down"|"select"|"print"|"execute"|"help"|"add"|"subtract"|"multiply"|"divide"|"decimal"|"separator"|"plus"|"minus"|"comma"|"period"|"num_lock"|"caps_lock"|"scroll_lock"|"oem_1"|"oem_2"|"oem_3"|"oem_4"|"oem_5"|"oem_6"|"oem_7"|"oem_8"|"oem_102"}`<br/>
The accelerator.

`command` `string`<br/>
The command to send when the accelerator is invoked (for a list of available commands, see 'get_commands').



---

## get_menu_item

Get an item from a menu or submenu.
```
qtm.gui.get_menu_item(menu?, index)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).

`index` `integer`<br/>
The index of the item in the menu.


**Returns**

`{"text": string, "command": string, "submenu": integer}` 

---

## get_menu_items

Get all items from a menu or submenu.
```
qtm.gui.get_menu_items(menu?)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).


**Returns**

`[{"text": string, "command": string, "submenu": integer}]` 

---

## get_menu_item_count

Get the number of items in a menu or submenu.
```
qtm.gui.get_menu_item_count(menu?)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).


**Returns**

`integer` 

---

## insert_menu_button

Insert a button into a menu or submenu.
```
qtm.gui.insert_menu_button(menu?, text, command, index?)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).

`text` `string`<br/>
The button text.

`command` `string`<br/>
The command to execute when button is pressed (for a list of available commands, see 'get_commands').

`index` `integer?`<br/>
The index where the button will be inserted (if null, the button will be inserted at the end).



---

## insert_menu_separator

Insert a separator into a menu or submenu.
```
qtm.gui.insert_menu_separator(menu?, index?)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).

`index` `integer?`<br/>
The index where the separator will be inserted (if null, the separator will be inserted at the end).



---

## insert_menu_submenu

Insert a submenu into a menu or submenu.
```
qtm.gui.insert_menu_submenu(menu?, text, index?)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).

`text` `string`<br/>
The submenu text.

`index` `integer?`<br/>
The index where the submenu will be inserted (if null, the submenu will inserted at the end).


**Returns**

`integer` The handle to the inserted submenu.

---

## delete_menu_item

Delete an item in a menu or submenu.
```
qtm.gui.delete_menu_item(menu?, index)
```

**Parameters**

`menu` `integer?`<br/>
The handle to the menu (if null, the main menu will be used).

`index` `integer`<br/>
The index of the item to delete.



---

## set_command_execute_function

Set an execute callback function for a command.
```
qtm.gui.set_command_execute_function(command, function?)
```

The command must've been added by a previous call to 'add_command'. This method cannot be used to overwrite built-in commands or user commands added by other instances of this module.

**Parameters**

`command` `string`<br/>
The command.

`function` `function?`<br/>
The function to invoke when the command is executed (if null, execution of the command will be disabled).



---

## set_command_update_function

Set an update callback function for a command.
```
qtm.gui.set_command_update_function(command, function?)
```

This can be used to conditionally disable commands and grey out buttons. The command must've been added by a previous call to 'add_command'. This method cannot be used to overwrite built-in commands or user commands added by other instances of this module.

**Parameters**

`command` `string`<br/>
The command.

`function` `function?`<br/>
The function to invoke when the command is updated (if null, the command will be enabled by default). Must return a boolean indicating if the command should be enabled.



---

## help

Get the documentation for a module or method.
```
qtm.gui.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

