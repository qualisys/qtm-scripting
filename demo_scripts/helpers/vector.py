import math


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   C L A S S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
class Vec3:
    # - - - - - - - - - - - - - - - - - - -
    # ////////   P R I V A T E   ////////
    # - - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def __init__(self, *args):
        # Empty (default constructor)
        if len(args) == 0:
            self._x = 0.0
            self._y = 0.0
            self._z = 0.0
        # List of ints or floats
        elif len(args) == 1:
            if not isinstance(args[0], list):
                raise ValueError("Expected a list but received type '" + str(type(args[0])).split("'", 2)[1] + "'.")
            if len(args[0]) != 3:
                raise ValueError("Expected a list with length 3 but received a list with length '" + str(len(args[0])) + "'.")
            if (isinstance(args[0][0], (float, int)) and isinstance(args[0][1], (float, int)) and isinstance(args[0][2], (float, int))):
                self._x = args[0][0]
                self._y = args[0][1]
                self._z = args[0][2]
            else:
                exception_str = "Unsupported construction of type '" + self.__class__.__name__ + "'."
                exception_str += " Expected three floats or integers but received:"
                exception_str += " '" + str(args[0][0]) + "', '" + str(args[0][1]) + "', '" + str(args[0][2]) + "'"
                raise ValueError(exception_str)
        # Three ints or floats
        elif len(args) == 3:
            if (isinstance(args[0], (float, int)) and isinstance(args[1], (float, int)) and isinstance(args[2], (float, int))):
                self._x = args[0]
                self._y = args[1]
                self._z = args[2]
            else:
                exception_str = "Unsupported construction of type '" + self.__class__.__name__ + "'."
                exception_str += " Expected three floats or integers but received:"
                exception_str += " '" + str(args[0]) + "', '" + str(args[1]) + "', '" + str(args[2]) + "'"
                raise ValueError(exception_str)
        else:
            exception_str = "Unsupported construction of type '" + self.__class__.__name__ + "' using '" + str(len(args)) + "' argument(s):"
            for i in range(len(args)):
                if i != 0:
                    exception_str += ","
                exception_str += (" '" + str(type(args[i])).split("'", 2)[1] + "'")
            raise AttributeError(exception_str)

    def __getitem__(self, key):
        if isinstance(key, int):
            # NOTE: Default Python behaviour allows indexing with negative numbers
            if (key < 0):
                key %= 3
            if key == 0:
                return self._x
            elif key == 1:
                return self._y
            elif key == 2:
                return self._z
            else:  # Index larger than 2
                raise IndexError("Incorrect index value " + str(key) + " provided. Index cannot be larger than 2.")
        else:
            raise TypeError("Indexing using type '" + str(type(key)).split("'", 2)[1] + "' is not supported.")

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Indexing using type '" + str(type(key)).split("'", 2)[1] + "' is not supported.")
        if not isinstance(value, (int, float)):
            raise ValueError("Inserting a value of type '" + str(type(value)).split("'", 2)[1] + "' is not supported.")
        # NOTE: Default Python behaviour allows indexing with negative numbers
        if (key < 0):
            key %= 3
        if key == 0:
            self._x = value
        elif key == 1:
            self._y = value
        elif key == 2:
            self._z = value
        else:
            raise IndexError("Incorrect index value " + str(key) + " provided. Index must be 0, 1, or 2.")

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"

    def __iter__(self):
        # NOTE: This is equivalent to a '__list__' overload
        return iter([self._x, self._y, self._z])

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self._x + other._x, self._y + other._y, self._z + other._z)
        else:
            raise TypeError("Addition to a vector with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self._x - other._x, self._y - other._y, self._z - other._z)
        else:
            raise TypeError("Subtraction from a vector with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return (self._x * other._x + self._y * other._y + self._z * other._z)
        elif isinstance(other, (int, float)):
            return self.__class__(self._x * other, self._y * other, self._z * other)
        else:
            raise TypeError("Multiplication between a vector and type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        # NOTE: Mathematically, Vec3*Scalar produces the same result as Scalar*Vec3.
        #       However, the operation is not defined in Python, so we need to check for it.
        if (isinstance(other, (int, float))):
            return self.__mul__(other)
        else:
            return other.__mul__(self)  # Attempt reverse multiplication

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self._x / other, self._y / other, self._z / other)
        elif isinstance(other, self.__class__):
            raise TypeError("Dividing a vector by another vector is not mathematically possible.")
        else:
            raise TypeError("Dividing a vector with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if (self._x == other._x and self._y == other._y and self._z == other._z):
                return True
            else:
                return False
        else:
            raise TypeError("Comparing type '" + self.__class__.__name__ + "' with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")
    # endregion

    # - - - - - - - - - - - - - - - - - -
    # ////////   P U B L I C   ////////
    # - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def cross(self, other):
        if isinstance(other, Vec3):
            return_vec_x = ((self._y * other._z) - (self._z * other._y))
            return_vec_y = ((self._z * other._x) - (self._x * other._z))
            return_vec_z = ((self._x * other._y) - (self._y * other._x))
            return Vec3(return_vec_x, return_vec_y, return_vec_z)
        else:
            raise TypeError("Vector cross product with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def magnitude(self):
        return math.sqrt(self.__mul__(self))
    # endregion
