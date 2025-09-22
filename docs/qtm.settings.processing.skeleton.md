# qtm.settings.processing.skeleton

Access and modify skeleton processing settings.

=== "Python"
    ``` py
    import qtm
    
    skeleton_ids = qtm.settings.processing.skeleton.get_skeleton_ids("project")
    print(skeleton_ids)
    # [17, 173, 329]
    
    print(qtm.settings.processing.skeleton.get_skeleton_name("project", skeleton_ids[0]))
    # Eli
    
    skeleton_name = "Eliott"
    qtm.settings.processing.skeleton.set_skeleton_name("project", skeleton_ids[0], skeleton_name)
    print(qtm.settings.processing.skeleton.get_skeleton_name("project", skeleton_ids[0]))
    # Eliott
    
    print(qtm.settings.processing.skeleton.find_skeleton("project", skeleton_name))
    # 17
    
    segment_ids = qtm.settings.processing.skeleton.get_segment_ids("project", skeleton_ids[0])
    print(segment_ids)
    # [18, 29, 37, 44, 50, 56, 62, 69, 77, 83, 89, 96, 104, 111, 119, 125, 132, 139, 146, 152, 159, 166]
    
    print(qtm.settings.processing.skeleton.get_segment_name("project", segment_ids[0]))
    # Hips
    
    segment_child_ids = qtm.settings.processing.skeleton.get_segment_child_ids("project", segment_ids[0])
    print(segment_child_ids)
    # [29, 119, 146]
    
    print(qtm.settings.processing.skeleton.get_segment_name("project", segment_child_ids[0]))
    # Spine
    
    segment_name = "Head"
    segment_id = qtm.settings.processing.skeleton.find_segment("project", skeleton_ids[0], segment_name)
    print(segment_id)
    # 111
    
    qtm.settings.processing.skeleton.get_max_iterations("project", "post")
    # 3000
    qtm.settings.processing.skeleton.set_max_iterations("project", "post", 1)
    qtm.settings.processing.skeleton.get_max_iterations("project", "post")
    # 1
    
    qtm.settings.processing.skeleton.get_factor("project", "realtime")
    # 10000000.0
    qtm.settings.processing.skeleton.set_factor("project", "realtime", 1000)
    qtm.settings.processing.skeleton.get_factor("project", "realtime")
    # 1000.0
    
    qtm.settings.processing.skeleton.set_settings("project", {'skeletons': [{'name': 'ABC', 'scale_factor': 1.0, 'root': {'name': 'Root', 'markers': [{'name': 'RootMarker1', 'position': [108.3, 141.4, 36.9], 'weight': 4.0}, {'name': 'RootMarker2', 'position': [-108.3, 140.2, 29.7], 'weight': 4.0}], 'transform': [[-0.98, -0.043, 0.007, 3852.7], [0.044, -0.98, 0.049, -1187.9], [0.005, 0.05, 0.99, 927.7], [0.0, 0.0, 0.0, 1.0]], 'default_transform': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'solver': 'global_optimization', 'endpoint': [2.68, 1.0, 2.68], 'children': [{'name': 'ChildSegment', 'markers': [{'name': 'ChildMarker', 'position': [-1.032, 125.1, 139.6], 'weight': 1.0}], 'transform': [[0.97, 0.23, -0.014, 3.66], [-0.23, 0.96, 0.056, 22.8], [0.028, -0.05, 0.99, 64.3], [0.0, 0.0, 0.0, 1.0]], 'default_transform': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'solver': 'none', 'endpoint': [-0.0, 0.0, 186.1], 'children': None}]}}], 'marker_count_threshold': 1, 'realtime': {'max_iterations': 22, 'factor': 10.0, 'accuracy': 0.1}, 'post': {'max_iterations': 11, 'factor': 10.0, 'accuracy': 0.1}})
    qtm.settings.processing.skeleton.get_settings("project")
    # {'skeletons': [{'name': 'ABC', 'scale': 1.0, 'root': {'name': 'Root', 'markers': [{'name': 'RootMarker1', 'position': [108.3, 141.4, 36.9], 'weight': 4.0}, {'name': 'RootMarker2', 'position': [-108.3, 140.2, 29.7], 'weight': 4.0}], 'rigid_bodies': [], 'transform': [[-0.9762406329113924, -0.04334962025316456, 0.007090253164556962, 3852.7], [0.04365037974683544, -0.9750182278481014, 0.04936784810126583, -1187.9], [0.004909746835443038, 0.04963215189873418, 0.9987411392405063, 927.7], [0.0, 0.0, 0.0, 1.0]], 'default_transform': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'degrees_of_freedom': {}, 'solver': 'global_optimization', 'endpoint': [2.68, 1.0, 2.68], 'children': [{'name': 'ChildSegment', 'markers': [{'name': 'ChildMarker', 'position': [-1.032, 125.1, 139.6], 'weight': 1.0}], 'rigid_bodies': [], 'transform': [[0.9727852040816327, 0.23056785714285713, -0.014780612244897958, 3.66], [-0.22943214285714283, 0.9715770408163266, 0.05546428571428571, 22.8], [0.027219387755102038, -0.05053571428571429, 0.9983418367346939, 64.3], [0.0, 0.0, 0.0, 1.0]], 'default_transform': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'degrees_of_freedom': {}, 'solver': 'none', 'endpoint': [-0.0, 0.0, 186.1], 'children': []}]}}], 'marker_count_threshold': 1, 'realtime': {'max_iterations': 22, 'factor': 10.0, 'accuracy': 0.1}, 'post': {'max_iterations': 11, 'factor': 10.0, 'accuracy': 0.1}}
    ```
=== "Lua"
    ``` lua
    skeleton_ids = qtm.settings.processing.skeleton.get_skeleton_ids("project")
    print(skeleton_ids)
    -- {17, 173, 329}
    
    print(qtm.settings.processing.skeleton.get_skeleton_name("project", skeleton_ids[1]))
    -- Eli
    
    skeleton_name = "Eliott"
    qtm.settings.processing.skeleton.set_skeleton_name("project", skeleton_ids[1], skeleton_name)
    print(qtm.settings.processing.skeleton.get_skeleton_name("project", skeleton_ids[1]))
    -- Eliott
    
    print(qtm.settings.processing.skeleton.find_skeleton("project", skeleton_name))
    -- 17
    
    segment_ids = qtm.settings.processing.skeleton.get_segment_ids("project", skeleton_ids[1])
    print(segment_ids)
    -- {18, 29, 37, 44, 50, 56, 62, 69, 77, 83, 89, 96, 104, 111, 119, 125, 132, 139, 146, 152, 159, 166}
    
    print(qtm.settings.processing.skeleton.get_segment_name("project", segment_ids[1]))
    -- Hips
    
    segment_child_ids = qtm.settings.processing.skeleton.get_segment_child_ids("project", segment_ids[1])
    print(segment_child_ids)
    -- {29, 119, 146}
    
    print(qtm.settings.processing.skeleton.get_segment_name("project", segment_child_ids[1]))
    -- Spine
    
    segment_name = "Head"
    segment_id = qtm.settings.processing.skeleton.find_segment("project", skeleton_ids[1], segment_name)
    print(segment_id)
    -- 111
    
    qtm.settings.processing.skeleton.get_max_iterations("project", "post")
    -- 3000
    qtm.settings.processing.skeleton.set_max_iterations("project", "post", 1)
    qtm.settings.processing.skeleton.get_max_iterations("project", "post")
    -- 1
    
    qtm.settings.processing.skeleton.get_factor("project", "realtime")
    -- 10000000.0
    qtm.settings.processing.skeleton.set_factor("project", "realtime", 1000)
    qtm.settings.processing.skeleton.get_factor("project", "realtime")
    -- 1000.0
    
    qtm.settings.processing.skeleton.set_settings("project", {post = {max_iterations = 11, factor = 10.0, accuracy = 0.1}, realtime = {max_iterations = 22, factor = 10.0, accuracy = 0.1}, skeletons = {{scale_factor = 1.0, root = {endpoint = {2.68, 1.00, 2.68}, markers = {{position = {108.3, 141.4, 36.95}, name = "RootMarker1", weight = 4.0}, {position = {-108.3, 140.25, 29.70}, name = "RootMarker2", weight = 4.0}}, solver = "global_optimization", transform = {{-0.99, -0.044, 0.008, 3852.77}, {0.044, -0.99, 0.05, -1187.9}, {0.005, 0.05, 0.99, 927.7}, {0.0, 0.0, 0.0, 1.0}}, name = "Root", children = {{endpoint = {-0.0, 0.0, 186.17}, markers = {{position = {-1.032, 125.1, 139.6}, weight = 1.0, name = "ChildMarker"}}, solver = "none", transform = {{0.97, 0.239, -0.015, 3.66}, {-0.238, 0.96, 0.056, 22.8}, {0.028, -0.051, 0.99, 64.3}, {0.0, 0.0, 0.0, 1.0}}, name = "ChildSegment"}}}, name = "ABC"}}, marker_count_threshold = 1})
    print(qtm.settings.processing.skeleton.get_settings("project"))
    -- {post = {factor = 10.0, accuracy = 0.1, max_iterations = 11}, realtime = {factor = 10.0, accuracy = 0.1, max_iterations = 22}, skeletons = {{scale = 1.0, name = "ABC", root = {rigid_bodies = {}, endpoint = {2.68, 1.0, 2.68}, transform = {{-0.98625944584383, -0.043836272040302, 0.0076083123425693, 3852.77}, {0.044163727959698, -0.98502128463476, 0.049855919395466, -1187.9}, {0.0053916876574307, 0.050144080604534, 0.99871926952141, 927.7}, {0.0, 0.0, 0.0, 1.0}}, solver = "global_optimization", default_transform = {{1.0, 0.0, 0.0, 0.0}, {0.0, 1.0, 0.0, 0.0}, {0.0, 0.0, 1.0, 0.0}, {0.0, 0.0, 0.0, 1.0}}, name = "Root", children = {{rigid_bodies = {}, endpoint = {-0.0, 0.0, 186.17}, transform = {{0.97074260204082, 0.2390868622449, -0.014989923469388, 3.66}, {-0.2379131377551, 0.9695181122449, 0.056116198979592, 22.8}, {0.028010076530612, -0.050883801020408, 0.99830382653061, 64.3}, {0.0, 0.0, 0.0, 1.0}}, solver = "none", default_transform = {{1.0, 0.0, 0.0, 0.0}, {0.0, 1.0, 0.0, 0.0}, {0.0, 0.0, 1.0, 0.0}, {0.0, 0.0, 0.0, 1.0}}, name = "ChildSegment", children = {}, markers = {{name = "ChildMarker", weight = 1.0, position = {-1.032, 125.1, 139.6}}}, degrees_of_freedom = {}}}, markers = {{name = "RootMarker1", weight = 4.0, position = {108.3, 141.4, 36.95}}, {name = "RootMarker2", weight = 4.0, position = {-108.3, 140.25, 29.7}}}, degrees_of_freedom = {}}}}, marker_count_threshold = 1}
    ```
=== "REST"
    ``` bat
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_skeleton_ids/
    :: [17,173,329]
    
    set skeleton_id=17
    curl --json "[\"project\", %skeleton_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_skeleton_name/
    :: "Eli"
    
    set skeleton_name=\"Eliott\"
    curl --json "[\"project\", %skeleton_id%, %skeleton_name%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/set_skeleton_name/
    curl --json "[\"project\", %skeleton_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_skeleton_name/
    :: "Eliott"
    
    curl --json "[\"project\", %skeleton_name%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/find_skeleton/
    :: 17
    
    curl --json "[\"project\", %skeleton_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_segment_ids/
    :: [18,29,37,44,50,56,62,69,77,83,89,96,104,111,119,125,132,139,146,152,159,166]
    
    set segment_id=18
    curl --json "[\"project\", %segment_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_segment_name/
    :: "Hips"
    
    curl --json "[\"project\", %segment_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_segment_child_ids/
    :: [29,119,146]
    
    set segment_child_id=29
    curl --json "[\"project\", %segment_child_id%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_segment_name/
    :: "Spine"
    
    set segment_name=\"Head\"
    curl --json "[\"project\", %skeleton_id%, %segment_name%]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/find_segment/
    :: 111
    
    curl --json "[\"project\", \"post\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_max_iterations/
    :: 3000
    curl --json "[\"project\", \"post\", 1]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/set_max_iterations/
    curl --json "[\"project\", \"post\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_max_iterations/
    :: 1
    
    curl --json "[\"project\", \"realtime\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_factor/
    :: 10000000.0
    curl --json "[\"project\", \"realtime\", 1000]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/set_factor/
    curl --json "[\"project\", \"realtime\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_factor/
    :: 1000.0
    
    curl --json "[\"project\", {\"marker_count_threshold\":1,\"post\":{\"accuracy\":0.1,\"factor\":10,\"max_iterations\":11},\"realtime\":{\"accuracy\":0.1,\"factor\":10,\"max_iterations\":22},\"skeletons\":[{\"name\":\"ABC\",\"root\":{\"children\":[{\"children\":null,\"default_transform\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],\"degrees_of_freedom\":{},\"endpoint\":[-0,0,186.09],\"markers\":[{\"name\":\"ChildMarker\",\"position\":[-1.032,125.09,139.59],\"weight\":1}],\"name\":\"ChildSegment\",\"rigid_bodies\":[],\"solver\":\"none\",\"transform\":[[0.97,0.23,-0.014,3.66],[-0.23,0.97,0.055,22.8],[0.027,-0.05,0.99,64.3],[0,0,0,1]]}],\"default_transform\":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],\"degrees_of_freedom\":{},\"endpoint\":[2.68,1,2.68],\"markers\":[{\"name\":\"RootMarker1\",\"position\":[108.3,141.4,36.9],\"weight\":4},{\"name\":\"RootMarker2\",\"position\":[-108.3,140.2,29.69],\"weight\":4}],\"name\":\"Root\",\"rigid_bodies\":[],\"solver\":\"global_optimization\",\"transform\":[[-0.97,-0.04,0.007,3852.69],[0.043,-0.97,0.049,-1187.9],[0.0049,0.049,0.99,927.7],[0,0,0,1]]},\"scale_factor\":1}]}]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/set_settings/
    curl --json "[\"project\"]" http://localhost:7979/api/scripting/qtm/settings/processing/skeleton/get_settings
    :: {"marker_count_threshold":1,"post":{"accuracy":0.10000000000000001,"factor":10,"max_iterations":11},"realtime":{"accuracy":0.10000000000000001,"factor":10,"max_iterations":22},"skeletons":[{"name":"ABC","root":{"children":[{"children":[],"default_transform":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],"degrees_of_freedom":{},"endpoint":[0,0,186.09],"markers":[{"name":"ChildMarker","position":[-1.032,125.09,139.59],"weight":1}],"name":"ChildSegment","rigid_bodies":[],"solver":"none","transform":[[0.97286501272264625,0.23054770992366416,-0.014354961832061069,3.6600000000000001],[-0.22945229007633591,0.97167620865139948,0.054899491094147587,22.800000000000001],[0.026645038167938933,-0.050100508905852423,0.99838346055979643,64.299999999999997],[0,0,0,1]]}],"default_transform":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],"degrees_of_freedom":{},"endpoint":[2.6800000000000002,1,2.6800000000000002],"markers":[{"name":"RootMarker1","position":[108.3,141.40000000000001,36.899999999999999],"weight":4},{"name":"RootMarker2","position":[-108.3,140.19999999999999,29.690000000000001],"weight":4}],"name":"Root","rigid_bodies":[],"solver":"global_optimization","transform":[[-0.96622188295165401,-0.041351628498727727,0.0069848600508905867,3852.6900000000001],[0.041648371501272263,-0.96501801653944019,0.048874338422391861,-1187.9000000000001],[0.0049151399491094159,0.049125661577608143,0.99876010050890585,927.70000000000005],[0,0,0,1]]},"scale":1}]}
    ```
## add_skeleton

Add a skeleton.
```
qtm.settings.processing.skeleton.add_skeleton(source, name)
```

A root segment will be added automatically. If a skeleton with the same name already exists, it will be overwritten.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`name` `string`<br/>
The name of the skeleton.


**Returns**

`integer` The identifier of the added skeleton.

---

## add_segment

Add a segment to a skeleton.
```
qtm.settings.processing.skeleton.add_segment(source, parent_id, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`parent_id` `integer`<br/>
The parent segment identifier.

`name` `string`<br/>
The name of the segment.


**Returns**

`integer` The identifier of the added segment.

---

## delete_skeleton

Delete a skeleton.
```
qtm.settings.processing.skeleton.delete_skeleton(source, skeleton_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.



---

## delete_segment

Delete a segment in a skeleton.
```
qtm.settings.processing.skeleton.delete_segment(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.



---

## clear_skeletons

Delete all skeletons.
```
qtm.settings.processing.skeleton.clear_skeletons(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.



---

## get_skeleton_id

Get a skeleton identifier by index.
```
qtm.settings.processing.skeleton.get_skeleton_id(source, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`index` `integer`<br/>
The index of the skeleton.


**Returns**

`integer` 

---

## get_skeleton_ids

Get all skeleton identifiers.
```
qtm.settings.processing.skeleton.get_skeleton_ids(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`[integer]` 

---

## get_skeleton_count

Get the number of skeletons.
```
qtm.settings.processing.skeleton.get_skeleton_count(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## get_skeleton_name

Get the name of a skeleton.
```
qtm.settings.processing.skeleton.get_skeleton_name(source, skeleton_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`string` 

---

## set_skeleton_name

Set the name of a skeleton.
```
qtm.settings.processing.skeleton.set_skeleton_name(source, skeleton_id, name)
```

If a skeleton with the same name already exists, it will be overwritten.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.

`name` `string`<br/>
The name of the skeleton.



---

## get_skeleton_scale

Get the scale of a skeleton.
```
qtm.settings.processing.skeleton.get_skeleton_scale(source, skeleton_id)
```

The scale represents the size of the skeleton relative to e.g. an avatar. It is used when exporting and streaming such that the scale of the output is always 1.0.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`float` 

---

## set_skeleton_scale

Set the scale of a skeleton.
```
qtm.settings.processing.skeleton.set_skeleton_scale(source, skeleton_id, scale)
```

The scale represents the size of the skeleton relative to e.g. an avatar. It is used when exporting and streaming such that the scale of the output is always 1.0.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.

`scale` `float`<br/>
The scale of the skeleton. Must be within the [0.01, 100.0] range.



---

## get_skeleton_root_id

Get the root segment identifier in a skeleton.
```
qtm.settings.processing.skeleton.get_skeleton_root_id(source, skeleton_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`integer` 

---

## get_segment_id

Get a segment identifier in a skeleton by index.
```
qtm.settings.processing.skeleton.get_segment_id(source, skeleton_id, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.

`index` `integer`<br/>
The segment index.


**Returns**

`integer` 

---

## get_segment_ids

Get all segment identifiers in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_ids(source, skeleton_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`[integer]` 

---

## get_segment_count

Get the number of segments in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_count(source, skeleton_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.


**Returns**

`integer` 

---

## get_segment_name

Get the name of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_name(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`string` 

---

## set_segment_name

Set the name of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_name(source, segment_id, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`name` `string`<br/>
The name of the segment.



---

## get_segment_markers

Get the markers of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_markers(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[{"name": string, "position": vec3f, "weight": float}]` The segment markers (with positions in local coordinates and millimeters).

---

## set_segment_markers

Set the markers of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_markers(source, segment_id, markers)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`markers` `[{"name": string, "position": vec3f, "weight": float}]`<br/>
The segment markers (with positions in local coordinates and millimeters).



---

## get_segment_rigid_bodies

Get the rigid bodies of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_rigid_bodies(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[{"name": string, "transform": mat4x4f, "weight": float}]` The segment rigid bodies (with transforms in local coordinates and translations in millimeters).

---

## set_segment_rigid_bodies

Set the rigid bodies of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_rigid_bodies(source, segment_id, rigid_bodies)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`rigid_bodies` `[{"name": string, "transform": mat4x4f, "weight": float}]`<br/>
The segment rigid bodies (with transforms in local coordinates and translations in millimeters).



---

## get_segment_transform

Get the transform of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_transform(source, segment_id)
```

The transform represents the calibrated pose of the skeleton, and is used as the initial solution when solving.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`mat4x4f` The segment transform (in local coordinates with translation in millimeters).

---

## set_segment_transform

Set the transform of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_transform(source, segment_id, transform)
```

The transform represents the calibrated pose of the skeleton, and is used as the initial solution when solving.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`transform` `mat4x4f`<br/>
The segment transform (in local coordinates with translation in millimeters).



---

## get_segment_default_transform

Get the default transform of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_default_transform(source, segment_id)
```

The default transform brings skeletons with different zero poses (the pose where all segment rotations are zero) to the same default pose (e.g. a t-pose). This is mainly used for retargeting.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`mat4x4f` The segment default transform (in local coordinates with translation in millimeters).

---

## set_segment_default_transform

Set the default transform of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_default_transform(source, segment_id, transform)
```

The default transform brings skeletons with different zero poses (the pose where all segment rotations are zero) to the same default pose (e.g. a t-pose). This is mainly used for retargeting.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`transform` `mat4x4f`<br/>
The segment default transform (in local coordinates with translation in millimeters).



---

## get_segment_degrees_of_freedom

Get the degrees of freedom of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_degrees_of_freedom(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`{"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}` 

---

## set_segment_degrees_of_freedom

Set the degrees of freedom of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_degrees_of_freedom(source, segment_id, degrees_of_freedom)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`degrees_of_freedom` `{"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}`<br/>
The segment degrees of freedom.



---

## get_segment_solver

Get the solver of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_solver(source, segment_id)
```

A skeleton can have multiple solvers (e.g. the hands may be solved separately from the rest of the body). In this case, the solving will be done in a hierarchical manner, starting with the root (which must have a solver). Descendant body parts are then solved locally in the coordinate systems of their parent segments.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`"none"|"global_optimization"?` The segment solver (or null, if the segment is solved together with its ancestors).

---

## set_segment_solver

Set the solver of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_solver(source, segment_id, solver?)
```

A skeleton can have multiple solvers (e.g. the hands may be solved separately from the rest of the body). In this case, the solving will be done in a hierarchical manner, starting with the root (which must have a solver). Descendant body parts are then solved locally in the coordinate systems of their parent segments.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`solver` `"none"|"global_optimization"?`<br/>
The segment solver (if null, the segment will be solved together with its ancestors).



---

## get_segment_endpoint

Get the endpoint of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_endpoint(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`vec3f?` The segment endpoint (in local coordinates and millimeters). Or null, if the segment has children.

---

## set_segment_endpoint

Set the endpoint of a segment in a skeleton.
```
qtm.settings.processing.skeleton.set_segment_endpoint(source, segment_id, endpoint?)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`endpoint` `vec3f?`<br/>
The segment endpoint (in local coordinates and millimeters). If null, the segment is assumed to have children.



---

## get_segment_skeleton_id

Get the skeleton identifier of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_skeleton_id(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer` 

---

## get_segment_parent_id

Get the parent segment identifier of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_parent_id(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer?` The parent segment identifier (or null, if the segment is the root).

---

## get_segment_child_id

Get a child segment identifier of a segment in a skeleton by index.
```
qtm.settings.processing.skeleton.get_segment_child_id(source, segment_id, index)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.

`index` `integer`<br/>
The child index.


**Returns**

`integer` 

---

## get_segment_child_ids

Get all child segment identifiers of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_child_ids(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`[integer]` 

---

## get_segment_child_count

Get the number of child segments of a segment in a skeleton.
```
qtm.settings.processing.skeleton.get_segment_child_count(source, segment_id)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`segment_id` `integer`<br/>
The segment identifier.


**Returns**

`integer` 

---

## find_skeleton

Find a skeleton by name.
```
qtm.settings.processing.skeleton.find_skeleton(source, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`name` `string`<br/>
The name of the skeleton.


**Returns**

`integer?` The identifier of the found skeleton (or null, if no skeleton was found).

---

## find_segment

Find a segment in a skeleton by name.
```
qtm.settings.processing.skeleton.find_segment(source, skeleton_id, name)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`skeleton_id` `integer`<br/>
The skeleton identifier.

`name` `string`<br/>
The name of the segment.


**Returns**

`integer?` The identifier of the found segment (or null, if no segment was found).

---

## get_marker_count_threshold

Get the marker count threshold.
```
qtm.settings.processing.skeleton.get_marker_count_threshold(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The threshold (in percent).

---

## set_marker_count_threshold

Set the marker count threshold.
```
qtm.settings.processing.skeleton.set_marker_count_threshold(source, threshold)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`threshold` `integer`<br/>
The threshold (in percent). Must be within the [1, 100] range.



---

## get_factor

Get the skeleton solver factor.
```
qtm.settings.processing.skeleton.get_factor(source, mode)
```

This is a convergence criteria which defines how many factors of machine precision is considered to be no improvement.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.


**Returns**

`float` 

---

## set_factor

Set the skeleton solver factor.
```
qtm.settings.processing.skeleton.set_factor(source, mode, factor)
```

This is a convergence criteria which defines how many factors of machine precision is considered to be no improvement.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.

`factor` `float`<br/>
The factor.



---

## get_accuracy

Get the skeleton solver accuracy.
```
qtm.settings.processing.skeleton.get_accuracy(source, mode)
```

This is a convergence criteria which defines how small a gradient must be to be considered flat.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.


**Returns**

`float` 

---

## set_accuracy

Set the skeleton solver accuracy.
```
qtm.settings.processing.skeleton.set_accuracy(source, mode, accuracy)
```

This is a convergence criteria which defines how small a gradient must be to be considered flat.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.

`accuracy` `float`<br/>
The accuracy.



---

## get_max_iterations

Get the maximum number of iterations.
```
qtm.settings.processing.skeleton.get_max_iterations(source, mode)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.


**Returns**

`integer` 

---

## set_max_iterations

Set the maximum number of iterations.
```
qtm.settings.processing.skeleton.set_max_iterations(source, mode, max_iterations)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`mode` `"realtime"|"post"`<br/>
The processing mode.

`max_iterations` `integer`<br/>
The maximum number of iterations.



---

## get_settings

Get all settings.
```
qtm.settings.processing.skeleton.get_settings(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"skeletons": [{"name": string, "scale": float?, "root": {"name": string, "markers": [{"name": string, "position": vec3f, "weight": float}]?, "rigid_bodies": [{"name": string, "transform": mat4x4f, "weight": float}]?, "transform": mat4x4f?, "default_transform": mat4x4f?, "degrees_of_freedom": {"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}?, "solver": "none"|"global_optimization"?, "endpoint": vec3f?, "children": [...]?}?}]?, "marker_count_threshold": integer?, "realtime": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?, "post": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?}` 

---

## set_settings

Set some or all settings.
```
qtm.settings.processing.skeleton.set_settings(source, settings)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`settings` `{"skeletons": [{"name": string, "scale": float?, "root": {"name": string, "markers": [{"name": string, "position": vec3f, "weight": float}]?, "rigid_bodies": [{"name": string, "transform": mat4x4f, "weight": float}]?, "transform": mat4x4f?, "default_transform": mat4x4f?, "degrees_of_freedom": {"rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z": {"constraint": {"lower_bound": float, "upper_bound": float}?, "couplings": [{"segment": string, "degree_of_freedom": "rotation_x"|"rotation_y"|"rotation_z"|"translation_x"|"translation_y"|"translation_z", "coefficient": float}], "goal": {"value": float, "weight": float}?}}?, "solver": "none"|"global_optimization"?, "endpoint": vec3f?, "children": [...]?}?}]?, "marker_count_threshold": integer?, "realtime": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?, "post": {"factor": float?, "accuracy": float?, "max_iterations": integer?}?}`<br/>
The settings (if a setting is omitted or null, then it will not be set).



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.skeleton.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

