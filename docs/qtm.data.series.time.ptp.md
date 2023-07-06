# qtm.data.series.time.ptp

Access and modify ptp (precision time protocol) data series.

=== "Python"
    ``` py
    import qtm
    
    series_ids = qtm.data.series.time.ptp.get_series_ids()
    print(series_ids)
    # [15664]
    
    print(qtm.data.series.time.ptp.get_sample_count(series_ids[0]))
    # 12000
    
    print(qtm.data.series.time.ptp.get_frequency(series_ids[0]))
    # 20.0
    
    sample_index = 150
    print(qtm.data.series.time.ptp.get_sample(series_ids[0], sample_index))
    # {'second': 1500388477, 'nanosecond': 203316000}
    
    print(qtm.data.series.time.ptp.get_time_at_sample_index(series_ids[0], sample_index))
    # 7.5
    ```
=== "Lua"
    ``` lua
    series_ids = qtm.data.series.time.ptp.get_series_ids()
    print(series_ids)
    -- {15664}
    
    print(qtm.data.series.time.ptp.get_sample_count(series_ids[1]))
    -- 12000
    
    print(qtm.data.series.time.ptp.get_frequency(series_ids[1]))
    -- 20.0
    
    sample_index = 150
    print(qtm.data.series.time.ptp.get_sample(series_ids[1], sample_index))
    -- {second = 1500388477, nanosecond = 203316000}
    
    print(qtm.data.series.time.ptp.get_time_at_sample_index(series_ids[1], sample_index))
    -- 7.5
    ```
=== "REST"
    ``` bat
    curl --json "" http://localhost:7979/api/scripting/qtm/data/series/time/ptp/get_series_ids/
    :: [15664]
    
    set series_id=15664
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/time/ptp/get_sample_count/
    :: 12000
    
    curl --json "[%series_id%]" http://localhost:7979/api/scripting/qtm/data/series/time/ptp/get_frequency/
    :: 20
    
    set sample_index=150
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/time/ptp/get_sample/
    :: {"nanosecond":203316000,"second":1500388477}
    
    curl --json "[%series_id%, %sample_index%]" http://localhost:7979/api/scripting/qtm/data/series/time/ptp/get_time_at_sample_index/
    :: 7.5
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

`{"second": integer, "nanosecond": integer}?` The sample (or null, if no sample existed at the given index).

---

## get_samples

Get a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}?`<br/>
The index range of the samples (if null, all samples will be returned).


**Returns**

`[{"second": integer, "nanosecond": integer}?]` The samples (may include null values, if no samples existed at the corresponding indices).

---

## set_sample

Set a single sample in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`index` `integer`<br/>
The index of the sample.

`sample` `{"second": integer, "nanosecond": integer}?`<br/>
The sample (if null, any previously existing sample will be deleted).



---

## set_samples

Set a range of samples in a data series.

**Parameters**

`id` `integer`<br/>
The data series identifier.

`range` `{"start": integer, "end": integer}`<br/>
The index range of the samples.

`samples` `[{"second": integer, "nanosecond": integer}?]`<br/>
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

