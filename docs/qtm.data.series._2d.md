# qtm.data.series._2d

Access 2d data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series._2d.get_series_ids()
    print(series_ids)
    # [106723, 106724, 106725, 106726, 106727, 106728, 106729, 106730, ... ...
    
    sample_ranges = qtm.data.series._2d.get_sample_ranges(series_ids[0])
    print(sample_ranges)
    # [{'start': 0, 'end': 322}]
    
    sample_index = 100
    print(qtm.data.series._2d.get_sample(series_ids[0], sample_index))
    # [[{'position': [119658, 5486], 'size': [978, 768]}, {'position': [120837, 8429], 'size': [1116, 1088]}, ... ...
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series._2d.get_series_ids()
    print(series_ids)
    -- {106723, 106724, 106725, 106726, 106727, 106728, 106729, 106730, ... ...
    
    sample_ranges = qtm.data.series._2d.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    -- {{start = 0, end = 322}}
    
    sample_index = 100
    print(qtm.data.series._2d.get_sample(series_ids[1], sample_index))
    -- {{{size = {978, 768}, position = {119658, 5486}}, {size = {1116, 1088}, position = {120837, 8429}}, {size = {750, 704}, ... ...
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/_2d/get_series_ids/
    :: [106723,106724,106725,106726,106727,106728,106729,106730,106731,106732,106733,106734,106735,106736]
    
    set series_id=106723
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/_2d/get_sample_ranges/
    :: [{"end":322,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/_2d/get_sample/
    : [[{"position":[119658,5486],"size":[978,768]},{"position":[120837,8429],"size":[1116,1088]}, ... ...
    ```
## get_series_id

Get a data series identifier by index.
```
qtm.data.series._2d.get_series_id(index)
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
qtm.data.series._2d.get_series_ids()
```

**Returns**

`[integer]` 

---

## get_series_count

Get the number of data series.
```
qtm.data.series._2d.get_series_count()
```

**Returns**

`integer` 

---

## get_sample_count

Get the number of samples in a data series.
```
qtm.data.series._2d.get_sample_count(id)
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
qtm.data.series._2d.get_sample_range(id)
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
qtm.data.series._2d.get_sample_ranges(id)
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
qtm.data.series._2d.get_gap_ranges(id)
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
qtm.data.series._2d.get_sample(id, index)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`[{"position": vec2i, "size": vec2i}]?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.
```
qtm.data.series._2d.get_samples(id, range?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[[{"position": vec2i, "size": vec2i}]?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## get_frequency

Get the frequency of a data series.
```
qtm.data.series._2d.get_frequency(id)
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
qtm.data.series._2d.get_offset(id)
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
qtm.data.series._2d.get_sample_index_at_time(id, time)
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
qtm.data.series._2d.get_time_at_sample_index(id, index)
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
qtm.data.series._2d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

