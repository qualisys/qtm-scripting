# qtm.data.object.bone

Access and modify bones.

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

