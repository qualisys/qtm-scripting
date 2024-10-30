# Types

| **Type** | **Description** |
| ------ | ------ |
| bool | Boolean (true or false). | 
| integer | 64-bit signed integer. | 
| float | 64-bit floating-point number. | 
| string | 8-bit ansi string (codepage depends on the user settings in windows). | 
| function | Any callable object such as a function or a lambda. | 
| enumeration | String from a predefined set (e.g. "enumerator1"\|"enumerator2" can be either "enumerator1" or "enumerator2"). | 
| matrix | NxM matrix or 1xM vector with integer or float values (e.g. mat4x4f means a 4x4 matrix of floats, and vec3i means a 1x3 vector of integers). | 
| structure | Map with predefined string keys (e.g. {"field1": integer, "field2": vec3f}). | 
| optional | Nullable (e.g. bool? can be either a bool or null). | 
| vector | List/array (e.g. [float] means a vector with float elements). For linear algebra vectors, see 'matrix' above. | 
| map | Dictionary/table (e.g. {integer: string} means a map with integer keys and string values). | 
