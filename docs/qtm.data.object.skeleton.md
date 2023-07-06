# qtm.data.object.skeleton

Access skeletons.

=== "Python"
    ``` py
    import qtm
    
    skeleton_ids = qtm.data.object.skeleton.get_skeleton_ids()
    print(skeleton_ids)
    # [8495, 8651]
    
    skeleton_name = qtm.data.object.skeleton.get_skeleton_name(skeleton_ids[0])
    print(skeleton_name)
    # Eli
    
    print(qtm.data.object.skeleton.find_skeleton(skeleton_name))
    # 8495
    
    segment_ids = qtm.data.object.skeleton.get_segment_ids(skeleton_ids[0])
    print(segment_ids)
    # [8496, 8507, 8515, 8522, 8528, 8534, 8540, 8547, 8555, 8561, 8567, 8574, ... ...
    
    print(qtm.data.object.skeleton.get_segment_name(segment_ids[0]))
    # Hips
    
    print(qtm.data.object.skeleton.get_segment_markers(segment_ids[0]))
    # [{'name': 'WaistRFront', 'position': [120.28204047346821, 202.23087588521537, ... ...
    
    print(qtm.data.object.skeleton.get_segment_degrees_of_freedom(segment_ids[0]))
    # {'rotation_x': {'constraint': None, 'couplings': [], 'goal': None}, 'rotation_y': ... ...
    
    segment_child_ids = qtm.data.object.skeleton.get_segment_child_ids(segment_ids[0])
    print(segment_child_ids)
    # [8507, 8597, 8624]
    
    print(qtm.data.object.skeleton.get_segment_name(segment_child_ids[0]))
    # Spine
    ```
=== "Lua"
    ``` lua
    skeleton_ids = qtm.data.object.skeleton.get_skeleton_ids()
    print(skeleton_ids)
    -- {8495, 8651}
    
    skeleton_name = qtm.data.object.skeleton.get_skeleton_name(skeleton_ids[1])
    print(skeleton_name)
    -- Eli
    
    print(qtm.data.object.skeleton.find_skeleton(skeleton_name))
    -- 8495
    
    segment_ids = qtm.data.object.skeleton.get_segment_ids(skeleton_ids[1])
    print(segment_ids)
    -- {8496, 8507, 8515, 8522, 8528, 8534, 8540, 8547, 8555, 8561, 8567, 8574, ... ...
    
    print(qtm.data.object.skeleton.get_segment_name(segment_ids[1]))
    -- Hips
    
    print(qtm.data.object.skeleton.get_segment_markers(segment_ids[1]))
    -- {{weight = 1.0, name = "WaistRFront", position = {120.28204047347, 202.23087588522, ... ...
    
    print(qtm.data.object.skeleton.get_segment_degrees_of_freedom(segment_ids[1]))
    -- {translation_x = {couplings = {}}, rotation_z = {couplings = {}}, rotation_x = ... ...
    
    segment_child_ids = qtm.data.object.skeleton.get_segment_child_ids(segment_ids[1])
    print(segment_child_ids)
    -- {8507, 8597, 8624}
    
    print(qtm.data.object.skeleton.get_segment_name(segment_child_ids[1]))
    -- Spine
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_skeleton_ids/
    :: [8495,8651]
    
    set skeleton_id=8495
    curl --json "[%skeleton_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_skeleton_name/
    :: "Eli"
    
    set skeleton_name=\"Eli\"
    curl --json "[%skeleton_name%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/find_skeleton/
    :: 8495
    
    curl --json "[%skeleton_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_ids/
    :: [8496,8507,8515,8522,8528,8534,8540,8547,8555,8561,8567,8574,8582,8589,8597,8603,8610,8617, ... ...
    
    set segment_id=8496
    curl --json "[%segment_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_name/
    :: "Hips"
    
    curl --json "[%segment_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_markers/
    :: [{"name":"WaistRFront","position":[120.28204047346821,202.23087588521537,61.546423666081523], ... ...
    
    curl --json "[%segment_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_degrees_of_freedom/
    :: {"rotation_x":{"constraint":null,"couplings":[],"goal":null},"rotation_y":{"constraint":null, ... ...
    
    curl --json "[%segment_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_child_ids/
    :: [8507,8597,8624]
    
    set segment_child_id=8507
    curl --json "[%segment_child_id%]" http://localhost:7979/api/scripting/qtm/data/object/skeleton/get_segment_name/
    :: "Spine"
    ```
## get_skeleton_id

Get a skeleton identifier by index.

**Parameters**

`index` `integer`<br/>
The index of the skeleton.


**Returns**

`integer` 

---

## get_skeleton_ids

Get all skeleton identifiers.

**Returns**

`[integer]` 

---

## get_skeleton_count

Get the number of skeletons.

**Returns**

`integer` 

---

## get_skeleton_name

Get the name of a skeleton.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`string` 

---

## get_skeleton_scale

Get the scale of a skeleton.

The scale represents the size of the skeleton relative to e.g. an avatar. It is used when exporting and streaming such that the scale of the output is always 1.0.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`float` 

---

## get_skeleton_root_id

Get the root segment identifier in a skeleton.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`integer` 

---

## get_segment_id

Get a segment identifier in a skeleton by index.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.

`index` `integer`<br/>
The segment index.


**Returns**

`integer` 

---

## get_segment_ids

Get all segment identifiers in a skeleton.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`[integer]` 

---

## get_segment_count

Get the number of segments in a skeleton.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`integer` 

---

## get_segment_name

Get the name of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`string` 

---

## get_segment_solver

Get the solver of a segment in a skeleton.

A skeleton can have multiple solvers (e.g. the hands may be solved separately from the rest of the body). In this case, the solving will be done in a hierarchical manner, starting with the root (which must have a solver). Descendant body parts are then solved locally in the coordinate systems of their parent segments.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`"none"|"global_optimization"?` The segment solver (or null, if the segment is solved together with its ancestors).

---

## get_segment_transform

Get the transform of a segment in a skeleton.

The transform represents the calibrated pose of the skeleton, and is used as the initial solution when solving.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`mat4x4f` The segment transform (in local coordinates with translation in millimeters).

---

## get_segment_default_transform

Get the default transform of a segment in a skeleton.

The default transform brings skeletons with different zero poses (the pose where all segment rotations are zero) to the same default pose (e.g. a t-pose). This is mainly used for retargeting.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`mat4x4f` The segment default transform (in local coordinates with translation in millimeters).

---

## get_segment_degrees_of_freedom

Get the degrees of freedom of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`{"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}` 

---

## get_segment_endpoint

Get the endpoint of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`vec3f?` The segment endpoint (in local coordinates and millimeters). Or null, if the segment has children.

---

## get_segment_markers

Get the markers of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[{"name": string, "position": vec3f, "weight": float}]` The segment markers (with positions in local coordinates and millimeters).

---

## get_segment_rigid_bodies

Get the rigid bodies of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[{"name": string, "transform": mat4x4f, "weight": float}]` The segment rigid bodies (with transforms in local coordinates and translations in millimeters).

---

## get_segment_skeleton_id

Get the skeleton identifier of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer` 

---

## get_segment_parent_id

Get the parent segment identifier of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer?` The parent segment identifier (or null, if the segment is the root).

---

## get_segment_child_id

Get a child segment identifier of a segment in a skeleton by index.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.

`index` `integer`<br/>
The child index.


**Returns**

`integer` 

---

## get_segment_child_ids

Get all child segment identifiers of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[integer]` 

---

## get_segment_child_count

Get the number of child segments of a segment in a skeleton.

**Parameters**

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer` 

---

## find_skeleton

Find a skeleton by name.

**Parameters**

`name` `string`<br/>
The name of the skeleton.


**Returns**

`integer?` The identifier of the found skeleton (or null, if no skeleton was found).

---

## find_segment

Find a segment in a skeleton by name.

**Parameters**

`skeleton_id` `integer`<br/>
The skeleton identifier.

`name` `string`<br/>
The name of the segment.


**Returns**

`integer?` The identifier of the found segment (or null, if no segment was found).

---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

