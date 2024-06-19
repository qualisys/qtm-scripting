# qtm.data.series.skeleton

Access and modify skeleton data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series.skeleton.get_series_ids()
    print(series_ids)
    # [9474, 9485, 9493, 9500, 9506, 9512, 9518, 9525, 9532, 9538, ... ...
    
    sample_ranges = qtm.data.series.skeleton.get_sample_ranges(series_ids[0])
    print(sample_ranges)
    # [{'start': 0, 'end': 3918}]
    
    sample_index = 100
    print(qtm.data.series.skeleton.get_sample(series_ids[0], sample_index))
    # [[0.9405906306958157, 0.3371781617403682, -0.04000190861238576, -1.4210854715202004e-14], [-0.3378169776885003, 0.9174301488204885, -0.21024179323013725, -22.087045432760192], [-0.03418998439097159, 0.21126478476216182, 0.9768307098401148, -421.44593293055993], [0.0, 0.0, 0.0, 1.0]]
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series.skeleton.get_series_ids()
    print(series_ids)
    -- {9474, 9485, 9493, 9500, 9506, 9512, 9518, 9525, 9532, 9538, ... ...
    
    sample_ranges = qtm.data.series.skeleton.get_sample_ranges(series_ids[1])
    print(sample_ranges)
    -- {{start = 0, end = 3918}}
    
    sample_index = 100
    print(qtm.data.series.skeleton.get_sample(series_ids[1], sample_index))
    -- {{0.94059063069582, 0.33717816174037, -0.040001908612386, -1.4210854715202e-14}, {-0.3378169776885, 0.91743014882049, -0.21024179323014, -22.08704543276}, {-0.034189984390972, 0.21126478476216, 0.97683070984011, -421.44593293056}, {0.0, 0.0, 0.0, 1.0}}
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/skeleton/get_series_ids/
    :: [9474,9485,9493,9500,9506,9512,9518,9525,9532,9538, ... ...
    
    set series_id=9769
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/skeleton/get_sample_ranges/
    :: [{"end":3918,"start":0}]
    
    set sample_index=100
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/skeleton/get_sample/
    :: [[0.94059063069581572,0.33717816174036819,-0.040001908612385763,-1.4210854715202004e-14],[-0.33781697768850028,0.91743014882048846,-0.21024179323013725,-22.087045432760192],[-0.034189984390971588,0.21126478476216182,0.97683070984011477,-421.44593293055993],[0,0,0,1]]
    ```
## get_series_id

Get a data series identifier by index.
```
qtm.data.series.skeleton.get_series_id(index)
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
qtm.data.series.skeleton.get_series_ids()
```

**Returns**

`[integer]` 

---

## get_series_count

Get the number of data series.
```
qtm.data.series.skeleton.get_series_count()
```

**Returns**

`integer` 

---

## get_sample_count

Get the number of samples in a data series.
```
qtm.data.series.skeleton.get_sample_count(id)
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
qtm.data.series.skeleton.get_sample_range(id)
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
qtm.data.series.skeleton.get_sample_ranges(id)
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
qtm.data.series.skeleton.get_gap_ranges(id)
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
qtm.data.series.skeleton.get_sample(id, index)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.


**Returns**

`mat4x4f?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.
```
qtm.data.series.skeleton.get_samples(id, range?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[mat4x4f?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## set_sample

Set a single sample in a data series.
```
qtm.data.series.skeleton.set_sample(id, index, sample?)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.

`sample` `mat4x4f?`<br/>
The sample (if null, any previously existing sample will be deleted).



---

## set_samples

Set a range of samples in a data series.
```
qtm.data.series.skeleton.set_samples(id, range, samples)
```

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}`<br/>
The index range of the samples.

`samples` `[mat4x4f?]`<br/>
The samples (if a sample is null, any previously existing sample will be deleted).



---

## delete_sample

Delete a single sample in a data series.
```
qtm.data.series.skeleton.delete_sample(id, index)
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
qtm.data.series.skeleton.delete_samples(id, range?)
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
qtm.data.series.skeleton.get_frequency(id)
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
qtm.data.series.skeleton.get_offset(id)
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
qtm.data.series.skeleton.get_sample_index_at_time(id, time)
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
qtm.data.series.skeleton.get_time_at_sample_index(id, index)
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
qtm.data.series.skeleton.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

