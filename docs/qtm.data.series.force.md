# qtm.data.series.force

Access force data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series.force.get_series_ids()
    print(series_ids)
    # [162, 163, 164]
    
    sample_ranges = qtm.data.series.force.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    # [{'start': 0, 'end': 3999}]
    
    sample_index = 1000
    print(qtm.data.series.force.get_sample(series_ids[1], sample_index))
    # {'force': [-43.66947368659142, -1.024620490494561, 339.9732299043336], 'moment': [35.271949647601424, 13.23768784042157, 7.189612166113668], 'center_of_pressure': [-27.376964978234895, 104.02044155564013, 0.0]}
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series.force.get_series_ids()
    print(series_ids)
    -- {162, 163, 164}
    
    sample_ranges = qtm.data.series.force.get_sample_ranges(series_ids[2])
    print(sample_ranges)
    -- {{end = 3999, start = 0}}
    
    sample_index = 1000
    print(qtm.data.series.force.get_sample(series_ids[2], sample_index))
    -- {moment = {35.271949647601, 13.237687840422, 7.1896121661137}, force = {-43.669473686591, -1.0246204904946, 339.97322990433}, center_of_pressure = {-27.376964978235, 104.02044155564, 0.0}}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/force/get_series_ids/
    :: [162,163,164]
    
    set series_id=163
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/force/get_sample_ranges/
    :: [{"end":3999,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/force/get_sample/
    :: {"center_of_pressure":[-27.376964978234895,104.02044155564013,0],"force":[-43.669473686591417,-1.0246204904945611,339.97322990433361],"moment":[35.271949647601424,13.23768784042157,7.189612166113668]}
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

`{"force": vec3f, "moment": vec3f, "center_of_pressure": vec3f}?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[{"force": vec3f, "moment": vec3f, "center_of_pressure": vec3f}?]` The samples (may include null values, if no samples existed at the corresponding indices).

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

