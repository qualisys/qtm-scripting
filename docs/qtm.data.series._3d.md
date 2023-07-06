# qtm.data.series._3d

Access and modify 3d data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series._3d.get_series_ids()
    print(series_ids)
    # [106038, 106043, 106047, 106051, 106053, 106055, 106057, 106059, ... ...
    
    sample_ranges = qtm.data.series._3d.get_sample_ranges(series_ids[0])
    print(sample_ranges)
    # [{'start': 0, 'end': 322}]
    
    sample_index = 100
    print(qtm.data.series._3d.get_sample(series_ids[0], sample_index))
    # {'position': [-5421.754065180638, -1070.7176908513354, 120.57418268723374], 'residual': 0.9671389652802037}
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series._3d.get_series_ids()
    print(series_ids)
    -- {106038, 106043, 106047, 106051, 106053, 106055, 106057, 106059, ... ...
    
    sample_ranges = qtm.data.series._3d.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    -- {{end = 322, start = 0}}
    
    sample_index = 100
    print(qtm.data.series._3d.get_sample(series_ids[1], sample_index))
    -- {residual = 0.9671389652802, position = {-5421.7540651806, -1070.7176908513, 120.57418268723}}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/_3d/get_series_ids/
    :: [106038,106043,106047,106051,106053,106055,106057,106059, ... ...
    
    set series_id=106038
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/_3d/get_sample_ranges/
    :: [{"end":322,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/_3d/get_sample/
    :: {"position":[-5421.7540651806376,-1070.7176908513354,120.57418268723374],"residual":0.96713896528020371}
    ```
## get_series_id

Get a data series identifier by index.

**Parameters**

`index` `integer`<br/>
The index of the data series.


**Returns**

`integer` 

---

## get_series_ids

Get all data series identifiers.

**Returns**

`[integer]` 

---

## get_series_count

Get the number of data series.

**Returns**

`integer` 

---

## get_sample_count

Get the number of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`integer` 

---

## get_sample_range

Get the total sample index range in a data series (first to last).

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`{"start": integer, "end": integer}` 

---

## get_sample_ranges

Get the contiguous sample index ranges in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`[{"start": integer, "end": integer}]` 

---

## get_gap_ranges

Get the contiguous sample index gap ranges in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`[{"start": integer, "end": integer}]` 

---

## get_sample

Get a single sample in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`{"position": vec3f, "residual": float}?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[{"position": vec3f, "residual": float}?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## set_sample

Set a single sample in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.

`sample` `{"position": vec3f, "residual": float}?`<br/>
The sample (if null, any previously existing sample will be deleted).



---

## set_samples

Set a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}`<br/>
The index range of the samples.

`samples` `[{"position": vec3f, "residual": float}?]`<br/>
The samples (if a sample is null, any previously existing sample will be deleted).



---

## delete_sample

Delete a single sample in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.



---

## delete_samples

Delete a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be deleted).



---

## get_frequency

Get the frequency of a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`float` 

---

## get_offset

Get the offset (start time) of a data series.

The offset is relative to the start of the measurement and may be negative (in which case the data series begins before the measurement).

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`float` The offset of the data series (in seconds).

---

## get_sample_index_at_time

Get the index of a sample in a data series at a given time.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`time` `float`<br/>
The time relative to the start of the measurement (in seconds). May be negative.


**Returns**

`integer` The index of the sample.

---

## get_time_at_sample_index

Get the start time of a sample in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`float` The start time of the sample relative to the start of the measurement (in seconds). May be negative.

---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

