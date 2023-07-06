# qtm.utilities.color

Utilities for converting various color models to a qtm compatible format.

=== "Python"
    ``` py
    import qtm
    
    print(qtm.utilities.color.rgb(0.855, 0.161, 0.11))
    # 1845722
    
    print(qtm.utilities.color.hsl(4, 0.77, 0.48))
    # 1845464
    ```
=== "Lua"
    ``` lua
    print(qtm.utilities.color.rgb(0.855, 0.161, 0.11))
    -- 1845722
    
    print(qtm.utilities.color.hsl(4, 0.77, 0.48))
    -- 1845464
    ```
=== "REST"
    ``` bat
    curl --json "[0.855, 0.161, 0.11]" http://localhost:7979/api/scripting/qtm/utilities/color/rgb/
    :: 1845722
    
    curl --json "[4, 0.77, 0.48]" http://localhost:7979/api/scripting/qtm/utilities/color/hsl/
    :: 1845464
    ```
## rgb

Make a color from rgb values (red, green, blue).

**Parameters**

`r` `float`<br/>
The red value (in the [0.0, 1.0] range).

`g` `float`<br/>
The green value (in the [0.0, 1.0] range).

`b` `float`<br/>
The blue value (in the [0.0, 1.0] range).


**Returns**

`integer` The color (in 0xbbggrr format).

---

## hsl

Make a color from hsl values (hue, saturation, lightness).

**Parameters**

`h` `float`<br/>
The hue value (in the [0.0, 360.0] range).

`s` `float`<br/>
The saturation value (in the [0.0, 1.0] range).

`l` `float`<br/>
The lightness value (in the [0.0, 1.0] range).


**Returns**

`integer` The color (in 0xbbggrr format).

---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

