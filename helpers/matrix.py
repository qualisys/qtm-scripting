import math

# variables
# WARNING: Adding variables here is potentially dangerous; variables are reset each time a script loads this module


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   C L A S S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
class Mat4x4:
    # - - - - - - - - - - - - - - - - - - -
    # ////////   P R I V A T E   ////////
    # - - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    def __init__(self, *args):
        self._values = [[0]*4 for _ in range(4)]
        # Empty (default constructor)
        if len(args) == 0:
            # Already initialized so just return
            return
        # List of four lists
        elif len(args) == 1:
            if not isinstance(args[0], list):
                raise ValueError("Expected a list but received type '" + str(type(args[0])).split("'", 2)[1] + "'.")
            if len(args[0]) != 4:
                raise ValueError("Expected a list with length 4 but received a list with length '" + str(len(args[0])) + "'.")
            for curr_row in range(len(args[0])):  # AKA: 'curr_list'
                if not isinstance(args[0][curr_row], list):
                    raise TypeError("Expected list of lists but object at index '" + str(curr_row) + "' is of type '" + str(type(args[0][curr_row])).split("'", 2)[1] + "'.")
                if len(args[0][curr_row]) != 4:
                    raise ValueError("Expected list at index '" + str(curr_row) + "' to have a length of 4 but its length is '" + str(len(args[0][curr_row])) + "'.")
                for curr_col in range(len(args[0][curr_row])):
                    if not isinstance(args[0][curr_row][curr_col], (float, int)):
                        raise TypeError("Expected list of lists to contain only ints or floats but list at index '" + str(curr_row) + "' contains type '" + str(type(args[0][curr_row][curr_col]).split("'", 2)[1]) + "' at index '" + str(curr_col) + "'.")
                    else:
                        self._values[curr_row][curr_col] = args[0][curr_row][curr_col]
        # Four lists
        elif len(args) == 4:
            for curr_row in range(len(args)):
                if not isinstance(args[curr_row], list):
                    raise TypeError("Expected 4 lists but argument number '" + str(curr_row+1) + "' is of type '" + str(type(args[curr_row])).split("'", 2)[1] + "'.")
                if len(args[curr_row]) != 4:
                    raise ValueError("Expected each list to have a length of 4 but list number '" + str(curr_row+1) + "' has a length of '" + str(len(args[0][curr_row])) + "'.")
                for curr_col in range(len(args[curr_row])):
                    if not isinstance(args[curr_row][curr_col], (float, int)):
                        raise TypeError("Expected all lists to contain only ints or floats but list number '" + str(curr_row+1) + "' contains type '" + str(type(args[curr_row][curr_col]).split("'", 2)[1]) + "' at index '" + str(curr_col) + "'.")
                    else:
                        self._values[curr_row][curr_col] = args[curr_row][curr_col]
        # Sixteen ints or floats
        elif len(args) == 16:
            curr_arg_index = 0
            for curr_row in range(4):
                for curr_col in range(4):
                    if not isinstance(args[curr_arg_index], (float, int)):
                        raise TypeError("Expected 16 ints or floats but argument number '" + str(curr_arg_index+1) + "' is of type '" + str(type(args[curr_arg_index]).split("'", 2)[1]) + "'.")
                    else:
                        self._values[curr_row][curr_col] = args[curr_arg_index]
                        curr_arg_index += 1
        else:
            exception_str = "Unsupported construction of type '" + self.__class__.__name__ + "' using '" + str(len(args)) + "' argument(s):"
            for i in range(len(args)):
                if i != 0:
                    exception_str += ","
                exception_str += (" '" + str(type(args[i])).split("'", 2)[1] + "'")
            raise AttributeError(exception_str)

    def __getitem__(self, key):
        return self._values[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Indexing using type '" + str(type(key)).split("'", 2)[1] + "' is not supported.")
        if not isinstance(value, list):
            raise TypeError("Inserting a value of type '" + str(type(value)).split("'", 2)[1] + "' is not supported.")
        if len(value) != 4:
            raise ValueError("Expected a list with length 4 but received a list with length '" + str(len(value)) + "'.")
        for i in range(4):
            if not isinstance(value[i], (float, int)):
                raise TypeError("Expected list to contain only ints or floats but found type '" + str(type(value[i]).split("'", 2)[1]) + "' at index '" + str(i) + "'.")
        self._values[key] = value

    def __str__(self):
        return str(self._values)

    def __iter__(self):
        # NOTE: This is equivalent to a '__list__' overload
        return iter(self._values)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return_matrix = [[0]*4 for _ in range(4)]
            for curr_row in range(4):
                for curr_col in range(4):
                    return_matrix[curr_row][curr_col] = self._values[curr_row][curr_col] + other._values[curr_row][curr_col]
            return self.__class__(return_matrix)
        else:
            raise TypeError("Addition to a 4x4 matrix with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return_matrix = [[0]*4 for _ in range(4)]
            for curr_row in range(4):
                for curr_col in range(4):
                    return_matrix[curr_row][curr_col] = self._values[curr_row][curr_col] - other._values[curr_row][curr_col]
            return self.__class__(return_matrix)
        else:
            raise TypeError("Subtraction from a 4x4 matrix with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return_matrix = [[0]*4 for _ in range(4)]
            for curr_row in range(4):
                for curr_col in range(4):
                    for section in range(4):
                        return_matrix[curr_row][curr_col] += self._values[curr_row][section] * other._values[section][curr_col]
            return self.__class__(return_matrix)
        else:
            raise TypeError("Multiplication between left-side operand 4x4 matrix and right-side operand type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        # NOTE: Mathematically, Scalar*Mat4x4 is an acceptable operation. However,
        #       the operation is not defined in Python, so we need to check for it.
        if (isinstance(other, (int, float))):
            return_matrix = [[0]*4 for _ in range(4)]
            for curr_row in range(4):
                for curr_col in range(4):
                    return_matrix[curr_row][curr_col] = self._values[curr_row][curr_col] * other
            return self.__class__(return_matrix)
        else:
            return other.__mul__(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for curr_row in range(4):
                for curr_col in range(4):
                    if self._values[curr_row][curr_col] != other._values[curr_row][curr_col]:
                        return False
            return True
        else:
            raise TypeError("Comparing type '" + self.__class__.__name__ + "' with type '" + str(type(other)).split("'", 2)[1] + "' is not supported.")
    # endregion

    # - - - - - - - - - - - - - - - - - -
    # ////////   P U B L I C   ////////
    # - - - - - - - - - - - - - - - -
    # region [ COLLAPSE / EXPAND ]
    @classmethod
    def create_identity_matrix(self):
        return Mat4x4([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @classmethod
    def create_translation_matrix(self, translation_vec):
        return Mat4x4([
            [1.0, 0.0, 0.0, translation_vec[0]],
            [0.0, 1.0, 0.0, translation_vec[1]],
            [0.0, 0.0, 1.0, translation_vec[2]],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @classmethod
    def create_rotation_matrix(self, radians_rot_x, radians_rot_y, radians_rot_z):
        matrix_rot_x = Mat4x4([
            [1, 0,                       0,                        0],
            [0, math.cos(radians_rot_x), -math.sin(radians_rot_x), 0],
            [0, math.sin(radians_rot_x), math.cos(radians_rot_x),  0],
            [0, 0,                       0,                        1]
        ])
        matrix_rot_y = Mat4x4([
            [math.cos(radians_rot_y),  0, math.sin(radians_rot_y), 0],
            [0,                        1, 0,                       0],
            [-math.sin(radians_rot_y), 0, math.cos(radians_rot_y), 0],
            [0,                        0, 0,                       1]
        ])
        matrix_rot_z = Mat4x4([
            [math.cos(radians_rot_z), -math.sin(radians_rot_z), 0, 0],
            [math.sin(radians_rot_z), math.cos(radians_rot_z),  0, 0],
            [0,                       0,                        1, 0],
            [0,                       0,                        0, 1]
        ])
        return ((matrix_rot_x * matrix_rot_y) * matrix_rot_z)
    # endregion
