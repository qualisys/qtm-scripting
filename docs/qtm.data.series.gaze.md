# qtm.data.series.gaze

Access gaze data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series.gaze.get_series_ids()
    print(series_ids)
    # [389, 390]
    
    sample_ranges = qtm.data.series.gaze.get_sample_ranges(series_ids[0])
    print(sample_ranges)
    # [{'start': 0, 'end': 300}]
    
    sample_index = 100
    print(qtm.data.series.gaze.get_sample(series_ids[0], sample_index))
    # {'position': [25.00000037252903, -12.000000104308128, -25.00000037252903], 'direction': [-0.624884307384491, -0.01765182428061962, 0.7805178165435791]}
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series.gaze.get_series_ids()
    print(series_ids)
    -- {389, 390}
    
    sample_ranges = qtm.data.series.gaze.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    -- {{end = 300, start = 0}}
    
    sample_index = 100
    print(qtm.data.series.gaze.get_sample(series_ids[1], sample_index))
    -- {position = {25.000000372529, -12.000000104308, -25.000000372529}, direction = {-0.62488430738449, -0.01765182428062, 0.78051781654358}}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/gaze/get_series_ids/
    :: [389,390]
    
    set series_id=389
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/gaze/get_sample_ranges/
    :: [{"end":300,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/gaze/get_sample/
    :: {"direction":[-0.62488430738449097,-0.017651824280619621,0.7805178165435791],"position":[25.00000037252903,-12.000000104308128,-25.00000037252903]}
    ```
## get_series_id

Get a data series identifier by index.
```
qtm.data.series.gaze.get_series_id(index)
```

**Parameters**

`index` `integer`<br/>
The index of the data series.


**Returns**

`integer` 

---

## get_series_ids

Get all data series identifiers.
```
qtm.data.series.gaze.get_series_ids()
```

**Returns**

`[integer]` 

---

## get_series_count

Get the number of data series.
```
qtm.data.series.gaze.get_series_count()
```

**Returns**

`integer` 

---

## get_sample_count

Get the number of samples in a data series.
```
qtm.data.series.gaze.get_sample_count(id)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`integer` 

---

## get_sample_range

Get the total sample index range in a data series (first to last).
```
qtm.data.series.gaze.get_sample_range(id)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`{"start": integer, "end": integer}?` The total sample index range (or null, if no samples existed).

---

## get_sample_ranges

Get the contiguous sample index ranges in a data series.
```
qtm.data.series.gaze.get_sample_ranges(id)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`[{"start": integer, "end": integer}]` 

---

## get_gap_ranges

Get the contiguous sample index gap ranges in a data series.
```
qtm.data.series.gaze.get_gap_ranges(id)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`[{"start": integer, "end": integer}]` 

---

## get_sample

Get a single sample in a data series.
```
qtm.data.series.gaze.get_sample(id, index)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`{"position": vec3f, "direction": vec3f}?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.
```
qtm.data.series.gaze.get_samples(id, range?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[{"position": vec3f, "direction": vec3f}?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## get_frequency

Get the frequency of a data series.
```
qtm.data.series.gaze.get_frequency(id)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`float` 

---

## get_offset

Get the offset (start time) of a data series.
```
qtm.data.series.gaze.get_offset(id)
```

The offset is relative to the start of the measurement and may be negative (in which case the data series begins before the measurement).

**Parameters**

`id` `integer`<br/>
The data series identifier.


**Returns**

`float` The offset of the data series (in seconds).

---

## get_sample_index_at_time

Get the index of a sample in a data series at a given time.
```
qtm.data.series.gaze.get_sample_index_at_time(id, time)
```

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
```
qtm.data.series.gaze.get_time_at_sample_index(id, index)
```

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
```
qtm.data.series.gaze.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

