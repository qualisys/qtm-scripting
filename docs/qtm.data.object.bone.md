# qtm.data.object.bone

Access and modify bones.

=== "Python"
    ``` py
    import qtm
    
    # - Create two dummy trajectories
    trajectory_id_1 = qtm.data.object.trajectory.add_trajectory("trajectory 1")
    trajectory_id_2 = qtm.data.object.trajectory.add_trajectory("trajectory 2")
    
    qtm.data.object.trajectory.fill_trajectory(trajectory_id_1, "static", None, {"offset": [1000.0, 0000.0, 0000.0]})
    qtm.data.object.trajectory.fill_trajectory(trajectory_id_2, "static", None, {"offset": [0000.0, 1000.0, 0000.0]})
    
    # - Create a bone between the trajectories
    bone_id = qtm.data.object.bone.add_bone(trajectory_id_1, trajectory_id_2)
    print(qtm.data.object.bone.get_bone_count())
    # 1
    
    # - Change the color of the bone
    color = qtm.utilities.color.rgb(1.0, 0.0, 1.0)
    qtm.data.object.bone.set_bone_color(bone_id, color)
    
    # - Delete the bone
    qtm.data.object.bone.delete_bone(bone_id)
    print(qtm.data.object.bone.get_bone_count())
    # 0
    ```
=== "Lua"
    ``` lua
    -- - Create two dummy trajectories
    trajectory_id_1 = qtm.data.object.trajectory.add_trajectory("trajectory 1")
    trajectory_id_2 = qtm.data.object.trajectory.add_trajectory("trajectory 2")
    
    qtm.data.object.trajectory.fill_trajectory(trajectory_id_1, "static", nil, {offset={1000.0, 0000.0, 0000.0}})
    qtm.data.object.trajectory.fill_trajectory(trajectory_id_2, "static", nil, {offset={0000.0, 1000.0, 0000.0}})
    
    -- - Create a bone between the trajectories
    bone_id = qtm.data.object.bone.add_bone(trajectory_id_1, trajectory_id_2)
    print(qtm.data.object.bone.get_bone_count())
    -- 1
    
    -- - Change the color of the bone
    color = qtm.utilities.color.rgb(1.0, 0.0, 1.0)
    qtm.data.object.bone.set_bone_color(bone_id, color)
    
    -- - Delete the bone
    qtm.data.object.bone.delete_bone(bone_id)
    print(qtm.data.object.bone.get_bone_count())
    -- 0
    ```
=== "REST"
    ``` bat
    :: - Create two dummy trajectories
    for /f "usebackq delims=" %%i in (`curl -s --json "[\"trajectory 1\"]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/add_trajectory/`) do ( 
      set "trajectory_id_1=%%i"
    )
    
    for /f "usebackq delims=" %%i in (`curl -s --json "[\"trajectory 2\"]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/add_trajectory/`) do (
      set "trajectory_id_2=%%i"
    )
    
    curl --json "[%trajectory_id_1%, \"static\", null, {\"offset\": [1000.0, 0, 0]}]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/fill_trajectory/
    curl --json "[%trajectory_id_2%, \"static\", null, {\"offset\": [0, 1000.0, 0]}]" http://localhost:7979/api/scripting/qtm/data/object/trajectory/fill_trajectory/
    
    :: - Create a bone between the trajectories
    for /f "usebackq delims=" %%i in (`curl -s --json "[%trajectory_id_1%, %trajectory_id_2%]" http://localhost:7979/api/scripting/qtm/data/object/bone/add_bone/`) do ( 
      set "bone_id=%%i"
    )
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/bone/get_bone_count/
    :: 1
    
    :: - Change the color of the bone
    for /f "usebackq delims=" %%i in (`curl -s --json "[1.0, 0.0, 1.0]" http://localhost:7979/api/scripting/qtm/utilities/color/rgb/`) do ( 
      set "color=%%i"
    )
    
    curl --json "[%bone_id%, %color%]" http://localhost:7979/api/scripting/qtm/data/object/bone/set_bone_color/
    
    :: - Delete the bone
    curl --json "[%bone_id%]" http://localhost:7979/api/scripting/qtm/data/object/bone/delete_bone/
    
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/bone/get_bone_count/
    :: 0
    ```
## add_bone

Add a bone.
```
qtm.data.object.bone.add_bone(trajectory_id_1, trajectory_id_2, color?)
```

**Parameters**

`trajectory_id_1` `integer`<br/>
The identifier of the first trajectory.

`trajectory_id_2` `integer`<br/>
The identifier of the second trajectory.

`color` `integer?`<br/>
The color of the bone (in 0xbbggrr format, see 'qtm.utilities.color' module).


**Returns**

`integer` The identifier of the added bone.

---

## delete_bone

Delete a bone.
```
qtm.data.object.bone.delete_bone(bone_id)
```

**Parameters**

`bone_id` `integer`<br/>
The identifier of the bone.



---

## find_bone

Find a bone by trajectory ids.
```
qtm.data.object.bone.find_bone(trajectory_id_1, trajectory_id_2)
```

**Parameters**

`trajectory_id_1` `integer`<br/>
The identifier of the first trajectory.

`trajectory_id_2` `integer`<br/>
The identifier of the second trajectory.


**Returns**

`integer?` The identifier of the found bone (or null, if no bone was found).

---

## clear_bones

Delete all bones.
```
qtm.data.object.bone.clear_bones()
```


---

## get_bone_id

Get a bone identifier by index.
```
qtm.data.object.bone.get_bone_id(index)
```

**Parameters**

`index` `integer`<br/>
The index of the bone.


**Returns**

`integer` 

---

## get_bone_ids

Get all bone identifiers.
```
qtm.data.object.bone.get_bone_ids()
```

**Returns**

`[integer]` 

---

## get_bone_count

Get the number of bones.
```
qtm.data.object.bone.get_bone_count()
```

**Returns**

`integer` 

---

## get_bone_trajectory_ids

Get the trajectory identifiers of a bone.
```
qtm.data.object.bone.get_bone_trajectory_ids(bone_id)
```

**Parameters**

`bone_id` `integer`<br/>
The identifier of the bone.


**Returns**

`integer, integer` The trajectory identifiers of the bone.

---

## get_bone_color

Get the color of a bone.
```
qtm.data.object.bone.get_bone_color(bone_id)
```

**Parameters**

`bone_id` `integer`<br/>
The identifier of the bone.


**Returns**

`integer` The color of the bone (in 0xbbggrr format).

---

## set_bone_color

Set the color of a bone.
```
qtm.data.object.bone.set_bone_color(bone_id, color)
```

**Parameters**

`bone_id` `integer`<br/>
The identifier of the bone.

`color` `integer`<br/>
The color of the bone (in 0xbbggrr format, see 'qtm.utilities.color' module).



---

## help

Get the documentation for a module or method.
```
qtm.data.object.bone.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

