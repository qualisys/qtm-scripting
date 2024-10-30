# qtm.utilities.documentation

Various documentation utilities.

## get_package_name

Get the name of the package.
```
qtm.utilities.documentation.get_package_name()
```

**Returns**

`string` 

---

## get_package_documentation

Get the complete documentation of the package.
```
qtm.utilities.documentation.get_package_documentation()
```

**Returns**

`{"name": string, "modules": [{"path": string, "brief": string, "details": string, "methods": [{"name": string, "brief": string, "details": string, "parameters": [{"name": string, "type": string, "description": string}], "return_value": {"type": string, "description": string}?}]}]}` 

---

## get_module_count

Get the number of modules in the package.
```
qtm.utilities.documentation.get_module_count()
```

**Returns**

`integer` 

---

## get_module_path

Get the path of a module.
```
qtm.utilities.documentation.get_module_path(module_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.


**Returns**

`string` 

---

## get_module_brief

Get the brief description of a module.
```
qtm.utilities.documentation.get_module_brief(module_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.


**Returns**

`string` 

---

## get_module_details

Get the detailed description of a module.
```
qtm.utilities.documentation.get_module_details(module_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.


**Returns**

`string` 

---

## get_module_documentation

Get the complete documentation of a module.
```
qtm.utilities.documentation.get_module_documentation(module_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.


**Returns**

`{"path": string, "brief": string, "details": string, "methods": [{"name": string, "brief": string, "details": string, "parameters": [{"name": string, "type": string, "description": string}], "return_value": {"type": string, "description": string}?}]}` 

---

## get_method_count

Get the number of methods in a module.
```
qtm.utilities.documentation.get_method_count(module_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.


**Returns**

`integer` 

---

## get_method_name

Get the name of a method in a module.
```
qtm.utilities.documentation.get_method_name(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string` 

---

## get_method_brief

Get the brief description of a method in a module.
```
qtm.utilities.documentation.get_method_brief(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string` 

---

## get_method_details

Get the detailed description of a method in a module.
```
qtm.utilities.documentation.get_method_details(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string` 

---

## get_method_signature

Get the signature of a method in a module.
```
qtm.utilities.documentation.get_method_signature(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string` 

---

## get_method_documentation

Get the complete documentation of a method in a module.
```
qtm.utilities.documentation.get_method_documentation(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`{"name": string, "brief": string, "details": string, "parameters": [{"name": string, "type": string, "description": string}], "return_value": {"type": string, "description": string}?}` 

---

## get_parameter_count

Get the number of parameters in a method.
```
qtm.utilities.documentation.get_parameter_count(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`integer` 

---

## get_parameter_name

Get the name of a parameter in a method.
```
qtm.utilities.documentation.get_parameter_name(module_index, method_index, parameter_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.

`parameter_index` `integer`<br/>
The index of the parameter.


**Returns**

`string` 

---

## get_parameter_type

Get the type of a parameter in a method.
```
qtm.utilities.documentation.get_parameter_type(module_index, method_index, parameter_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.

`parameter_index` `integer`<br/>
The index of the parameter.


**Returns**

`string` 

---

## get_parameter_description

Get the description of a parameter in a method.
```
qtm.utilities.documentation.get_parameter_description(module_index, method_index, parameter_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.

`parameter_index` `integer`<br/>
The index of the parameter.


**Returns**

`string` 

---

## get_parameter_documentation

Get the complete documentation of a parameter in a method.
```
qtm.utilities.documentation.get_parameter_documentation(module_index, method_index, parameter_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.

`parameter_index` `integer`<br/>
The index of the parameter.


**Returns**

`{"name": string, "type": string, "description": string}` 

---

## get_return_value_type

Get the type of the return value in a method.
```
qtm.utilities.documentation.get_return_value_type(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string?` The return value type (or null, if method isn't returning a value).

---

## get_return_value_description

Get the description of the return value in a method.
```
qtm.utilities.documentation.get_return_value_description(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`string?` The return value description (or null, if method isn't returning a value).

---

## get_return_value_documentation

Get the complete documentation of the return value in a method.
```
qtm.utilities.documentation.get_return_value_documentation(module_index, method_index)
```

**Parameters**

`module_index` `integer`<br/>
The index of the module.

`method_index` `integer`<br/>
The index of the method.


**Returns**

`{"type": string, "description": string}?` The return value documentation (or null, if method isn't returning a value).

---

## get_help_text

Get the help text for a given topic.
```
qtm.utilities.documentation.get_help_text(topic?)
```

This method is used internally by the global 'help' function.

**Parameters**

`topic` `"overview"|"modules"|"types"|"signatures"|"changelog"?`<br/>
The help topic.


**Returns**

`string` 

---

## help

Get the documentation for a module or method.
```
qtm.utilities.documentation.help(method?)
```

**Parameters**

`method` `string?`<br/>
The name of the method (if null, the documentation for the module will be returned instead).


**Returns**

`string` 

---

