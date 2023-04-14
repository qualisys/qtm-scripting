# QTM Common API

The Common API (Application Programming Interface) provides scripting support
for QTM (Qualisys Track Manager). Scripting is supported through both
[Python](https://www.python.org/) and [Lua](https://www.lua.org/).
Additionally, the Common API is also exposed through a REST API.

The API's functionality (that is, what QTM functionality can be accessed) is
exposed through a number of modules. This documentation provides a language
agnostic description of the modules. For more details, see the [list of
modules](modules.md). Below follows some short examples:

=== "Python"
    ``` py
    from qtm.data.series import _3d
    from qtm.data.object import trajectory
    # Get the data series identifier of a trajectory with the label "F_HeadFront".
    id = trajectory.find_trajectory("F_HeadFront")
    # Get the first sample of this trajectory.
    _3d.get_sample(id, 0)
    {'position': [-1193.8392806851402, 1428.9096641692772, 1677.330950395389], 'residual': 1.933161315987386}
    ```

=== "Lua"
    ``` lua
    -- Get the data series identifier of a trajectory with the label "F_HeadFront".
    id = qtm.data.object.trajectory.find_trajectory("F_HeadFront")
    -- Get the first sample of this trajectory.
    qtm.data.series._3d.get_sample(id, 0)
    {position = {-1193.8392806851, 1428.9096641693, 1677.3309503954}, residual = 1.9331613159874}
    ```

=== "REST"
    ``` js
    curl --json '["F_HeadFront"]' http://localhost:7979/api/common/qtm/data/object/trajectory/find_trajectory
    2985
    curl --json '[2985, 0]' http://localhost:7979/api/common/qtm/data/series/_3d/get_sample
    {"position":[-1193.8392806851402,1428.9096641692772,1677.330950395389],"residual":1.9331613159873859}
    ```
