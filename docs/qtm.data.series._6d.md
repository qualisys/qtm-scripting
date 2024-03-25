# qtm.data.series._6d

Access and modify 6dof data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series._6d.get_series_ids()
    print(series_ids)
    # [106751, 106752, 106753, 106754]
    
    sample_ranges = qtm.data.series._6d.get_sample_ranges(series_ids[0])
    print(sample_ranges)
    # [{'start': 0, 'end': 3380}]
    
    sample_index = 100
    print(qtm.data.series._6d.get_sample(series_ids[0], sample_index))
    # {'transform': [[-0.6398715972900391, 0.7683062553405762, 0.016427502036094666, 475.34625733104804], [-0.7682338953018188, -0.6400619745254517, 0.0117202028632164, -1057.2460105715884], [0.019519325345754623, -0.005120739806443453, 0.9997963905334473, 66.71982557748521], [0.0, 0.0, 0.0, 1.0]], 'residual': 0.6208022236824036}
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series._6d.get_series_ids()
    print(series_ids)
    -- {106751, 106752, 106753, 106754}
    
    sample_ranges = qtm.data.series._6d.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    -- {{start = 0, end = 3380}}
    
    sample_index = 100
    print(qtm.data.series._6d.get_sample(series_ids[1], sample_index))
    -- {transform = {{-0.63987159729004, 0.76830625534058, 0.016427502036095, 475.34625733105}, {-0.76823389530182, -0.64006197452545, 0.011720202863216, -1057.2460105716}, {0.019519325345755, -0.0051207398064435, 0.99979639053345, 66.719825577485}, {0.0, 0.0, 0.0, 1.0}}, residual = 0.6208022236824}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/_6d/get_series_ids/
    :: [106751,106752,106753,106754]
    
    set series_id=106751
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/_6d/get_sample_ranges/
    :: [{"end":3380,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/_6d/get_sample/
    :: {"residual":0.62080222368240356,"transform":[[-0.63987159729003906,0.76830625534057617,0.016427502036094666,475.34625733104804],[-0.76823389530181885,-0.64006197452545166,0.0117202028632164,-1057.2460105715884],[0.019519325345754623,-0.0051207398064434528,0.99979639053344727,66.71982557748521],[0,0,0,1]]}
    ```
## get_series_id

Get a data series identifier by index.
```
qtm.data.series._6d.get_series_id(index)
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
qtm.data.series._6d.get_series_ids()
```

**Returns**

`[integer]` 

---

## get_series_count

Get the number of data series.
```
qtm.data.series._6d.get_series_count()
```

**Returns**

`integer` 

---

## get_sample_count

Get the number of samples in a data series.
```
qtm.data.series._6d.get_sample_count(id)
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
qtm.data.series._6d.get_sample_range(id)
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
qtm.data.series._6d.get_sample_ranges(id)
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
qtm.data.series._6d.get_gap_ranges(id)
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
qtm.data.series._6d.get_sample(id, index)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`{"transform": mat4x4f, "residual": float}?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.
```
qtm.data.series._6d.get_samples(id, range?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[{"transform": mat4x4f, "residual": float}?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## set_sample

Set a single sample in a data series.
```
qtm.data.series._6d.set_sample(id, index, sample?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.

`sample` `{"transform": mat4x4f, "residual": float}?`<br/>
The sample (if null, any previously existing sample will be deleted).



---

## set_samples

Set a range of samples in a data series.
```
qtm.data.series._6d.set_samples(id, range, samples)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}`<br/>
The index range of the samples.

`samples` `[{"transform": mat4x4f, "residual": float}?]`<br/>
The samples (if a sample is null, any previously existing sample will be deleted).



---

## delete_sample

Delete a single sample in a data series.
```
qtm.data.series._6d.delete_sample(id, index)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.



---

## delete_samples

Delete a range of samples in a data series.
```
qtm.data.series._6d.delete_samples(id, range?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be deleted).



---

## get_frequency

Get the frequency of a data series.
```
qtm.data.series._6d.get_frequency(id)
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
qtm.data.series._6d.get_offset(id)
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
qtm.data.series._6d.get_sample_index_at_time(id, time)
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
qtm.data.series._6d.get_time_at_sample_index(id, index)
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
qtm.data.series._6d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

