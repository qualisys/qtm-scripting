# qtm.utilities.color

Utilities for converting various color models to a qtm compatible format.

## rgb

Make a color from rgb values (red, green, blue).
```
qtm.utilities.color.rgb(r, g, b)
```

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
```
qtm.utilities.color.hsl(h, s, l)
```

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
```
qtm.utilities.color.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

