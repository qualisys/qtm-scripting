# qtm.gui._3d

Interface to the measurement 3d view with methods for custom drawing.

=== "Python"
    ``` py
    import qtm
    
    def draw_sphere():
        # Draw a red sphere located in (x=1000, y=500, z=750), with a diameter of 500 mm.
        position = [1000, 500, 750]
        diameter = 500
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_sphere(position, diameter, color)
    
    def draw_arrow():
        # Draw a red arrow, with its base at (x=1000, y=-500, z=750), and points towards the sphere.
        starting_point = [1000, -500, 750]
        pointing_at = [1000, 150, 750]
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_arrow(starting_point, pointing_at, color)
        
    def draw_axes():
        # Draw an axis in (x=-1000, y=-500, z=750) and 500 mm in size.
        translation_matrix = ([
                [1.0, 0.0, 0.0, -1000,0],
                [0.0, 1.0, 0.0,  -500.0],
                [0.0, 0.0, 1.0,   750.0],
                [0.0, 0.0, 0.0,     1.0]
            ])
        size = 500
        qtm.gui._3d.draw_axes(translation_matrix, size)
    
    def draw_text_2d(measurement_time):
        # Draw the current frames measurement time in the middle of the 3D view.
        position = [0, 0]
        font_size = 24
        text_to_draw = '{:.2f}'.format(measurement_time)
        origin = {"horizontal": "center", "vertical": "center"}
        alignment = {"horizontal": "center", "vertical": "center"}
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_text_2d(position, font_size, text_to_draw, origin, alignment, color)
    
    def draw_callback(measurement_time):
        draw_sphere()
        draw_arrow()
        draw_axes()
        draw_text_2d(measurement_time)
    
    # - Set "draw_callback" as the draw function
    qtm.gui._3d.set_draw_function(draw_callback)
    ```
=== "Lua"
    ``` lua
    function draw_sphere()
        -- Draw a red sphere located in (x=1000, y=500, z=750), with a diameter of 500 mm.
        position = {1000, 500, 750}
        diameter = 500
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_sphere(position, diameter, color)
    end
    
    function draw_arrow()
        -- Draw a red arrow, with its base at (x=1000, y=-500, z=750), and points towards the sphere.
        starting_point = {1000, -500, 750}
        pointing_at = {1000, 150, 750}
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_arrow(starting_point, pointing_at, color)
    end
    
    function draw_axes()
        -- Draw an axis in (x=-1000, y=-500, z=750) and 500 mm in size.
        translation_matrix = {
            {1.0, 0.0, 0.0, -1000.0},
            {0.0, 1.0, 0.0,  -500.0},
            {0.0, 0.0, 1.0,   750.0},
            {0.0, 0.0, 0.0,     1.0}
        }
        qtm.gui._3d.draw_axes(translation_matrix, 500)
    end
    
    function draw_text_2d(measurement_time)
        -- Draw the current frames  measurement time in the middle of the 3D view.
        position = {0, 0}
        font_size = 24
        text_to_draw = string.format("%.2f", measurement_time)
        origin = {horizontal="center", vertical="center"}
        alignment = {horizontal="center", vertical="center"}
        color = qtm.utilities.color.rgb(0.855, 0.161, 0.11)
        qtm.gui._3d.draw_text_2d(position, font_size, text_to_draw, origin, alignment, color)
    end
    
    
    function draw_callback(measurement_time)
        draw_sphere()
        draw_arrow()
        draw_axes()
        draw_text_2d(measurement_time)
    end
    
    -- - Set "draw_callback" as the draw function
    qtm.gui._3d.set_draw_function(draw_callback)
    ```
## draw_sphere

Draw a sphere.

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

This method may only be used in a draw callback function (see 'set_draw_function').

**Parameters**

`transform` `mat4x4f`<br/>
The transform of the axes (with translation in millimeters).

`size` `float`<br/>
The size of the axes (in millimeters).



---

## draw_mesh

Draw a mesh.

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

**Parameters**

`function` `function?`<br/>
The function to invoke when the 3d view is redrawn (if null, custom drawing will be disabled). The function must have a single float parameter receiving the measurement time to be drawn (in seconds).



---

## help

Get the documentation for a module or method.

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

