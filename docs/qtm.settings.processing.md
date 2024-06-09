# qtm.settings.processing

Access and modify processing settings.

## get_process_every_frame

Get whether to process every frame during realtime.
```
qtm.settings.processing.get_process_every_frame()
```

**Returns**

`bool` 

---

## set_process_every_frame

Set whether to process every frame during realtime.
```
qtm.settings.processing.set_process_every_frame(enable)
```

**Parameters**

`enable` `bool`<br/>
True if every frame should be processed, otherwise false.



---

## get_store_realtime

Get whether to store realtime data during capture.
```
qtm.settings.processing.get_store_realtime()
```

**Returns**

`bool` 

---

## set_store_realtime

Set whether to store realtime data during capture.
```
qtm.settings.processing.set_store_realtime(enable)
```

**Parameters**

`enable` `bool`<br/>
True if realtime data should be stored, otherwise false.



---

## get_auto_backup

Get whether to automatically backup files before processing.
```
qtm.settings.processing.get_auto_backup(type)
```

This method requires 'capture' or 'batch' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_auto_backup

Set whether to automatically backup files before processing.
```
qtm.settings.processing.set_auto_backup(type, enable)
```

This method requires 'capture' or 'batch' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if files should be automatically backed up before processing, otherwise false.



---

## get_process_2d

Get whether to process 2d data.
```
qtm.settings.processing.get_process_2d(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_process_2d

Set whether to process 2d data.
```
qtm.settings.processing.set_process_2d(type, enable)
```

This method requires post-processing to be enabled during capture (see 'set_store_realtime').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if 2d data should be processed, otherwise false.



---

## get_track_2d

Get whether to track 2d data.
```
qtm.settings.processing.get_track_2d(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_track_2d

Set whether to track 2d data.
```
qtm.settings.processing.set_track_2d(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type. Additionally, post-processing must be enabled during capture (see 'set_store_realtime').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if 2d data should be tracked, otherwise false.



---

## get_track_3d

Get whether to track 3d data.
```
qtm.settings.processing.get_track_3d(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_track_3d

Set whether to track 3d data.
```
qtm.settings.processing.set_track_3d(type, enable)
```

This method requires post-processing to be enabled during capture (see 'set_store_realtime').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if 3d data should be tracked, otherwise false.



---

## get_merge_twin

Get whether to merge with twin slave.
```
qtm.settings.processing.get_merge_twin(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_merge_twin

Set whether to merge with twin slave.
```
qtm.settings.processing.set_merge_twin(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type. Additionally, post-processing must be enabled during capture (see 'set_store_realtime').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if twin slave should be merged with, otherwise false.



---

## get_fill_gaps

Get whether to fill gaps.
```
qtm.settings.processing.get_fill_gaps(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_fill_gaps

Set whether to fill gaps.
```
qtm.settings.processing.set_fill_gaps(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type. Additionally, tracking must be enabled during capture (see 'set_track_2d' and 'set_track_3d').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if gaps should be filled, otherwise false.



---

## get_apply_aim

Get whether to apply aim (automatic identification of markers).
```
qtm.settings.processing.get_apply_aim(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_apply_aim

Set whether to apply aim (automatic identification of markers).
```
qtm.settings.processing.set_apply_aim(type, enable)
```

This method requires tracking to be enabled during realtime and capture (see 'set_track_2d' and 'set_track_3d').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if aim should be applied, otherwise false.



---

## get_calculate_6d

Get whether to calculate 6dof.
```
qtm.settings.processing.get_calculate_6d(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_calculate_6d

Set whether to calculate 6dof.
```
qtm.settings.processing.set_calculate_6d(type, enable)
```

This method requires tracking to be enabled during realtime and capture (see 'set_track_2d' and 'set_track_3d').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if 6dof should be calculated, otherwise false.



---

## get_solve_skeletons

Get whether to solve skeletons.
```
qtm.settings.processing.get_solve_skeletons(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_solve_skeletons

Set whether to solve skeletons.
```
qtm.settings.processing.set_solve_skeletons(type, enable)
```

This method requires labeling to be enabled during realtime and capture (see 'set_apply_aim' and 'set_calculate_6d').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if skeletons should be solved, otherwise false.



---

## get_apply_glove

Get whether to apply glove data.
```
qtm.settings.processing.get_apply_glove(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_apply_glove

Set whether to apply glove data.
```
qtm.settings.processing.set_apply_glove(type, enable)
```

This method requires skeleton solving to be enabled during realtime and capture (see 'set_solve_skeletons').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if glove data should be applied, otherwise false.



---

## get_apply_sal

Get whether to apply sal (skeleton assisted labeling).
```
qtm.settings.processing.get_apply_sal(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_apply_sal

Set whether to apply sal (skeleton assisted labeling).
```
qtm.settings.processing.set_apply_sal(type, enable)
```

This method requires skeleton solving to be enabled during realtime and capture (see 'set_solve_skeletons').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if sal should be applied, otherwise false.



---

## get_calculate_force

Get whether to calculate force data.
```
qtm.settings.processing.get_calculate_force(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_calculate_force

Set whether to calculate force data.
```
qtm.settings.processing.set_calculate_force(type, enable)
```

This method requires post-processing to be enabled during capture (see 'set_store_realtime').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if force data should be calculated, otherwise false.



---

## get_calculate_gaze

Get whether to calculate gaze data.
```
qtm.settings.processing.get_calculate_gaze(type)
```

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_calculate_gaze

Set whether to calculate gaze data.
```
qtm.settings.processing.set_calculate_gaze(type, enable)
```

This method requires 6dof to be enabled during realtime and capture (see 'set_calculate_6d').

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if gaze data should be calculated, otherwise false.



---

## get_export_tsv

Get whether to export tsv.
```
qtm.settings.processing.get_export_tsv(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_tsv

Set whether to export tsv.
```
qtm.settings.processing.set_export_tsv(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if tsv should be exported, otherwise false.



---

## get_export_c3d

Get whether to export c3d.
```
qtm.settings.processing.get_export_c3d(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_c3d

Set whether to export c3d.
```
qtm.settings.processing.set_export_c3d(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if c3d should be exported, otherwise false.



---

## get_export_mat

Get whether to export mat.
```
qtm.settings.processing.get_export_mat(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_mat

Set whether to export mat.
```
qtm.settings.processing.set_export_mat(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if mat should be exported, otherwise false.



---

## get_export_avi

Get whether to export avi.
```
qtm.settings.processing.get_export_avi(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_avi

Set whether to export avi.
```
qtm.settings.processing.set_export_avi(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if avi should be exported, otherwise false.



---

## get_export_fbx

Get whether to export fbx.
```
qtm.settings.processing.get_export_fbx(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_fbx

Set whether to export fbx.
```
qtm.settings.processing.set_export_fbx(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if fbx should be exported, otherwise false.



---

## get_export_json

Get whether to export json.
```
qtm.settings.processing.get_export_json(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_export_json

Set whether to export json.
```
qtm.settings.processing.set_export_json(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if json should be exported, otherwise false.



---

## get_start_program

Get whether to start a program.
```
qtm.settings.processing.get_start_program(type)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.


**Returns**

`bool` 

---

## set_start_program

Set whether to start a program.
```
qtm.settings.processing.set_start_program(type, enable)
```

This method requires 'capture', 'batch', 'reprocess' or 'force' processing type.

**Parameters**

`type` `"realtime"|"capture"|"batch"|"reprocess"|"force"`<br/>
The processing type.

`enable` `bool`<br/>
True if a program should be started, otherwise false.



---

## help

Get the documentation for a module or method.
```
qtm.settings.processing.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

