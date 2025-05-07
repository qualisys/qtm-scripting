# qtm.data.object.analog

Access and modify analog boards and channels.

=== "Python"
    ``` py
    import qtm
    
    qtm.data.object.analog.get_board_count()
    # 1
    
    qtm.data.object.analog.get_board_ids()
    # [10020]
    
    qtm.data.object.analog.get_board_id(0)
    # 10020
    
    qtm.data.object.analog.get_board_name(10020)
    # 'EMG System'
    
    qtm.data.object.analog.get_board_channel_count(10020)
    # 4
    
    qtm.data.object.analog.get_board_channel_ids(10020)
    # [706, 707, 708, 709]
    
    qtm.data.object.analog.get_board_channel_id(10020, 0)
    # 706
    
    qtm.data.object.analog.get_board_channel_id(10020, 3)
    # 709
    
    qtm.data.object.analog.get_channel_count()
    # 4
    
    qtm.data.object.analog.get_channel_ids()
    # [706, 707, 708, 709]
    
    qtm.data.object.analog.get_channel_id(0)
    # 706
    
    qtm.data.object.analog.get_channel_id(3)
    # 709
    
    qtm.data.object.analog.get_channel_board_id(706)
    # 10020
    
    qtm.data.object.analog.get_channel_board_id(709)
    # 10020
    
    qtm.data.object.analog.get_channel_name(706)
    # 'EMG Sensor 1'
    
    qtm.data.object.analog.set_channel_name(706, "My Channel")
    
    qtm.data.object.analog.get_channel_name(706)
    # 'My Channel'
    
    qtm.data.object.analog.find_board("EMG System")
    # 10020
    
    qtm.data.object.analog.find_channel(10020, "My Channel")
    # 706
    
    qtm.data.object.analog.find_channels("My Channel")
    # [706]
    ```
=== "Lua"
    ``` lua
    print(qtm.data.object.analog.get_board_count())
    -- 1
    
    print(qtm.data.object.analog.get_board_ids())
    -- {10020}
    
    print(qtm.data.object.analog.get_board_id(0))
    -- 10020
    
    print(qtm.data.object.analog.get_board_name(10020))
    -- EMG System
    
    print(qtm.data.object.analog.get_board_channel_count(10020))
    -- 4
    
    print(qtm.data.object.analog.get_board_channel_ids(10020))
    -- {706, 707, 708, 709}
    
    print(qtm.data.object.analog.get_board_channel_id(10020, 0))
    -- 706
    
    print(qtm.data.object.analog.get_board_channel_id(10020, 3))
    -- 709
    
    print(qtm.data.object.analog.get_channel_count())
    -- 4
    
    print(qtm.data.object.analog.get_channel_ids())
    -- {706, 707, 708, 709}
    
    print(qtm.data.object.analog.get_channel_id(0))
    -- 706
    
    print(qtm.data.object.analog.get_channel_id(3))
    -- 709
    
    print(qtm.data.object.analog.get_channel_board_id(706))
    -- 10020
    
    print(qtm.data.object.analog.get_channel_board_id(709))
    -- 10020
    
    print(qtm.data.object.analog.get_channel_name(706))
    -- EMG Sensor 1
    
    print(qtm.data.object.analog.set_channel_name(706, "My Channel"))
    
    print(qtm.data.object.analog.get_channel_name(706))
    -- My Channel
    
    print(qtm.data.object.analog.find_board("EMG System"))
    -- 10020
    
    print(qtm.data.object.analog.find_channel(10020, "My Channel"))
    -- 706
    
    print(qtm.data.object.analog.find_channels("My Channel"))
    -- {706}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_count/
    :: 1
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_ids/
    :: [10020]
    
    curl --json "[0]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_id/
    :: 10020
    
    curl --json "[10020]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_name/
    :: "EMG System"
    
    curl --json "[10020]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_channel_count/
    :: 4
    
    curl --json "[10020]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_channel_ids/
    :: [706,707,708,709]
    
    curl --json "[10020, 0]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_channel_id/
    :: 706
    
    curl --json "[10020, 3]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_board_channel_id/
    :: 709
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_count/
    :: 4
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_ids/
    :: [706,707,708,709]
    
    curl --json "[0]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_id/
    :: 706
    
    curl --json "[3]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_id/
    :: 709
    
    curl --json "[706]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_board_id/
    :: 10020
    
    curl --json "[709]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_board_id/
    :: 10020
    
    curl --json "[706]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_name/
    :: "EMG Sensor 1"
    
    curl --json "[706, \"My Channel\"]" http://localhost:7979/api/scripting/qtm/data/object/analog/set_channel_name/
    
    curl --json "[706]" http://localhost:7979/api/scripting/qtm/data/object/analog/get_channel_name/
    :: "My Channel"
    
    curl --json "[\"EMG System\"]" http://localhost:7979/api/scripting/qtm/data/object/analog/find_board/
    :: 10020
    
    curl --json "[10020, \"My Channel\"]" http://localhost:7979/api/scripting/qtm/data/object/analog/find_channel/
    :: 706
    
    curl --json "[\"My Channel\"]" http://localhost:7979/api/scripting/qtm/data/object/analog/find_channels/
    :: [706]
    ```
## get_board_id

Get an analog board identifier by index.
```
qtm.data.object.analog.get_board_id(board_index)
```

**Parameters**

`board_index` `integer`<br/>
The index of the analog board.


**Returns**

`integer` 

---

## get_board_ids

Get all analog board identifiers.
```
qtm.data.object.analog.get_board_ids()
```

**Returns**

`[integer]` 

---

## get_board_count

Get the number of analog boards.
```
qtm.data.object.analog.get_board_count()
```

**Returns**

`integer` 

---

## get_board_name

Get the name of an analog board.
```
qtm.data.object.analog.get_board_name(board_id)
```

**Parameters**

`board_id` `integer`<br/>
The identifier of the analog board.


**Returns**

`string` 

---

## get_board_channel_id

Get an analog channel identifier on an analog board by index.
```
qtm.data.object.analog.get_board_channel_id(board_id, channel_index)
```

**Parameters**

`board_id` `integer`<br/>
The identifier of the analog board.

`channel_index` `integer`<br/>
The index of the analog channel.


**Returns**

`integer` 

---

## get_board_channel_ids

Get all analog channel identifiers on an analog board.
```
qtm.data.object.analog.get_board_channel_ids(board_id)
```

**Parameters**

`board_id` `integer`<br/>
The identifier of the analog board.


**Returns**

`[integer]` 

---

## get_board_channel_count

Get the number of analog channels on an analog board.
```
qtm.data.object.analog.get_board_channel_count(board_id)
```

**Parameters**

`board_id` `integer`<br/>
The identifier of the analog board.


**Returns**

`integer` 

---

## get_channel_id

Get an analog channel identifier by index.
```
qtm.data.object.analog.get_channel_id(channel_index)
```

This is equivalent to calling qtm.data.series.analog.get_series_id.

**Parameters**

`channel_index` `integer`<br/>
The index of the analog channel.


**Returns**

`integer` 

---

## get_channel_ids

Get all analog channel identifiers.
```
qtm.data.object.analog.get_channel_ids()
```

This is equivalent to calling qtm.data.series.analog.get_series_ids.

**Returns**

`[integer]` 

---

## get_channel_count

Get the number of analog channels.
```
qtm.data.object.analog.get_channel_count()
```

This is equivalent to calling qtm.data.series.analog.get_series_count.

**Returns**

`integer` 

---

## get_channel_name

Get the name of an analog channel.
```
qtm.data.object.analog.get_channel_name(channel_id)
```

**Parameters**

`channel_id` `integer`<br/>
The identifier of the analog channel.


**Returns**

`string` 

---

## set_channel_name

Set the name of an analog channel.
```
qtm.data.object.analog.set_channel_name(channel_id, channel_name)
```

**Parameters**

`channel_id` `integer`<br/>
The identifier of the analog channel.

`channel_name` `string`<br/>
The name of the analog channel.



---

## get_channel_board_id

Get the analog board identifier of an analog channel.
```
qtm.data.object.analog.get_channel_board_id(channel_id)
```

**Parameters**

`channel_id` `integer`<br/>
The identifier of the analog channel.


**Returns**

`integer` 

---

## find_board

Find an analog board by name.
```
qtm.data.object.analog.find_board(board_name)
```

**Parameters**

`board_name` `string`<br/>
The name of the analog board.


**Returns**

`integer?` The identifier of the found analog board (or null, if no analog board was found).

---

## find_channel

Find an analog channel on an analog board by name.
```
qtm.data.object.analog.find_channel(board_id, channel_name)
```

**Parameters**

`board_id` `integer`<br/>
The identifier of the analog board.

`channel_name` `string`<br/>
The name of the analog channel.


**Returns**

`integer?` The identifier of the found analog channel (or null, if no analog channel was found).

---

## find_channels

Find analog channels by name.
```
qtm.data.object.analog.find_channels(channel_name)
```

Analog channels may have the same name as long as they are on separate analog boards.

**Parameters**

`channel_name` `string`<br/>
The name of the analog channels.


**Returns**

`[integer]` The identifiers of the found analog channels.

---

## help

Get the documentation for a module or method.
```
qtm.data.object.analog.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

