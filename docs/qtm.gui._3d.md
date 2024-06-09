# qtm.gui._3d

Interface to the measurement 3d view with methods for custom drawing.

## draw_sphere

Draw a sphere.
```
qtm.gui._3d.draw_sphere(position, size, color?)
```

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`position` `vec3f`<br/>
The position of the center of the sphere (in millimeters).

`size` `float`<br/>
The diameter of the sphere (in millimeters).

`color` `integer?`<br/>
The color of the sphere (in 0xbbggrr format, see 'qtm.utilities.color' module). If null, white (0xffffff) will be used.



---

## draw_arrow

Draw an arrow.
```
qtm.gui._3d.draw_arrow(position, endpoint, color?)
```

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`position` `vec3f`<br/>
The position of the tail of the arrow (in millimeters).

`endpoint` `vec3f`<br/>
The position of the head of the arrow (in millimeters).

`color` `integer?`<br/>
The color of the arrow (in 0xbbggrr format, see 'qtm.utilities.color' module). If null, white (0xffffff) will be used.



---

## draw_axes

Draw coordinate system axes.
```
qtm.gui._3d.draw_axes(transform, size)
```

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`transform` `mat4x4f`<br/>
The transform of the axes (with translation in millimeters).

`size` `float`<br/>
The size of the axes (in millimeters).



---

## draw_mesh

Draw a mesh.
```
qtm.gui._3d.draw_mesh(transform, scale, filename)
```

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`transform` `mat4x4f`<br/>
The transform of the mesh (with translation in millimeters).

`scale` `float`<br/>
The scale of the mesh (the units of the mesh is assumed to be in meters).

`filename` `string`<br/>
The filename of the mesh. Only .obj files are supported. The file must be located next to the measurement or in one of the project's meshes folders.



---

## draw_text_2d

Draw 2d text.
```
qtm.gui._3d.draw_text_2d(position, size, text, origin?, alignment?, color?)
```

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`position` `vec2f`<br/>
The position of the text (in pixels relative to the given origin, with positive axes pointing down-right).

`size` `integer`<br/>
The font size.

`text` `string`<br/>
The text.

`origin` `{"horizontal": "left"|"center"|"right", "vertical": "top"|"center"|"bottom"}?`<br/>
The origin of the text position (if null, top-left corner will be used).

`alignment` `{"horizontal": "left"|"center"|"right", "vertical": "top"|"center"|"bottom"}?`<br/>
The alignment of the text (if null, top-left alignment will be used).

`color` `integer?`<br/>
The color of the text (in 0xbbggrr format, see 'qtm.utilities.color' module). If null, white (0xffffff) will be used.



---

## set_draw_function

Set a draw callback function.
```
qtm.gui._3d.set_draw_function(function?)
```

**Parameters**

`function` `function?`<br/>
The function to invoke when the 3d view is redrawn (if null, custom drawing will be disabled). The function must have a single float parameter receiving the measurement time to be drawn (in seconds).



---

## help

Get the documentation for a module or method.
```
qtm.gui._3d.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

