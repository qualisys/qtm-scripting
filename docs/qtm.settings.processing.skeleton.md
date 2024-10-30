# qtm.settings.processing.skeleton

Access and modify skeleton processing settings.

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

