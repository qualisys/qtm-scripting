# qtm.settings.processing._3d

Access and modify 3d processing settings.

## get_prediction_error

Get the prediction error.
```
qtm.settings.processing._3d.get_prediction_error(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` The prediction error (in millimeters).

---

## set_prediction_error

Set the prediction error.
```
qtm.settings.processing._3d.set_prediction_error(source, error)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`error` `float`<br/>
The prediction error (in millimeters).



---

## get_max_residual

Get the maximum residual.
```
qtm.settings.processing._3d.get_max_residual(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` The maximum residual (in millimeters).

---

## set_max_residual

Set the maximum residual.
```
qtm.settings.processing._3d.set_max_residual(source, residual)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`residual` `float`<br/>
The maximum residual (in millimeters).



---

## get_min_trajectory_length

Get the minimum trajectory length.
```
qtm.settings.processing._3d.get_min_trajectory_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The minimum trajectory length (in samples).

---

## set_min_trajectory_length

Set the minimum trajectory length.
```
qtm.settings.processing._3d.set_min_trajectory_length(source, length)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `integer`<br/>
The minimum trajectory length (in samples). Must be within the [2, 100] range.



---

## get_min_ray_count

Get the minimum marker ray count.
```
qtm.settings.processing._3d.get_min_ray_count(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` 

---

## set_min_ray_count

Set the minimum marker ray count.
```
qtm.settings.processing._3d.set_min_ray_count(source, count)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`count` `integer`<br/>
The minimum ray count. Must be within the [2, 5] range.



---

## get_auto_limit_ray_length

Get whether to automatically calculate ray length limits.
```
qtm.settings.processing._3d.get_auto_limit_ray_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_auto_limit_ray_length

Set whether to automatically calculate ray length limits.
```
qtm.settings.processing._3d.set_auto_limit_ray_length(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if ray length limits should be automatically calculated, otherwise false.



---

## get_min_ray_length

Get the minimum ray length.
```
qtm.settings.processing._3d.get_min_ray_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` The minimum ray length (in meters).

---

## set_min_ray_length

Set the minimum ray length.
```
qtm.settings.processing._3d.set_min_ray_length(source, length)
```

This method requires manual ray length limits (see 'set_auto_limit_ray_length')

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `float`<br/>
The minimum ray length (in meters).



---

## get_max_ray_length

Get the maximum ray length.
```
qtm.settings.processing._3d.get_max_ray_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`float` The maximum ray length (in meters).

---

## set_max_ray_length

Set the maximum ray length.
```
qtm.settings.processing._3d.set_max_ray_length(source, length)
```

This method requires manual ray length limits (see 'set_auto_limit_ray_length').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `float`<br/>
The maximum ray length (in meters).



---

## get_store_rays

Get whether to store rays.
```
qtm.settings.processing._3d.get_store_rays(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_store_rays

Set whether to store rays.
```
qtm.settings.processing._3d.set_store_rays(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if rays should be stored, otherwise false.



---

## get_auto_join

Get whether to automatically join trajectories.
```
qtm.settings.processing._3d.get_auto_join(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_auto_join

Set whether to automatically join trajectories.
```
qtm.settings.processing._3d.set_auto_join(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if trajectories should be automatically joined, otherwise false.



---

## get_max_auto_join_gap_length

Get the maximum gap length for automatically joining trajectories.
```
qtm.settings.processing._3d.get_max_auto_join_gap_length(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`integer` The maximum gap length (in samples).

---

## set_max_auto_join_gap_length

Set the maximum gap length for automatically joining trajectories.
```
qtm.settings.processing._3d.set_max_auto_join_gap_length(source, length)
```

This method requires automatic joining of trajectories to be enabled (see 'set_auto_join').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`length` `integer`<br/>
The maximum gap length (in samples).



---

## get_use_bounding_box

Get whether to use a bounding box.
```
qtm.settings.processing._3d.get_use_bounding_box(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_use_bounding_box

Set whether to use a bounding box.
```
qtm.settings.processing._3d.set_use_bounding_box(source, enable)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if a bounding box should be used, otherwise false.



---

## get_bounding_box

Get the bounding box.
```
qtm.settings.processing._3d.get_bounding_box(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`{"min_x": float, "max_x": float, "min_y": float, "max_y": float, "min_z": float, "max_z": float}` The bounding box (in millimeters).

---

## set_bounding_box

Set the bounding box.
```
qtm.settings.processing._3d.set_bounding_box(source, box)
```

This method requires bounding box to be enabled (see 'set_use_bounding_box').

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`box` `{"min_x": float, "max_x": float, "min_y": float, "max_y": float, "min_z": float, "max_z": float}`<br/>
The bounding box (in millimeters).



---

## get_auto_select_range

Get whether to automatically set the selected range after tracking.
```
qtm.settings.processing._3d.get_auto_select_range(source)
```

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.


**Returns**

`bool` 

---

## set_auto_select_range

Set whether to automatically set the selected range after tracking.
```
qtm.settings.processing._3d.set_auto_select_range(source, enable)
```

If enabled, the selected range will be set to the tracked range.

**Parameters**

`source` `"project"|"measurement"`<br/>
The settings source.

`enable` `bool`<br/>
True if selected range should be automatically set, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing._3d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

