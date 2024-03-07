from pathlib import Path
import sys
import inspect

current_script_dir = Path(inspect.getfile(inspect.currentframe())).resolve().parent
this_dir = str(current_script_dir.parents[1])
if this_dir not in sys.path:
    sys.path.append(this_dir)

from helpers.matrix import Mat4x4
import unittest


# HOW TO RUN TESTS
# ----------------
# 1. Open a Python interpreter
# 2. Change directory to ..\qtm-scripting\demo_scripts\Tests
# 3. Run the command: python -m unittest discover -v


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   P R I V A T E   F U N C T I O N S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
class MatrixCompare(unittest.TestCase):
    def assert_almost_equal(self, Mat4x4_1, Mat4x4_2):
        self.assertAlmostEqual(Mat4x4_1[0][0], Mat4x4_2[0][0], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[0][1], Mat4x4_2[0][1], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[0][2], Mat4x4_2[0][2], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[0][3], Mat4x4_2[0][3], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[1][0], Mat4x4_2[1][0], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[1][1], Mat4x4_2[1][1], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[1][2], Mat4x4_2[1][2], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[1][3], Mat4x4_2[1][3], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[2][0], Mat4x4_2[2][0], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[2][1], Mat4x4_2[2][1], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[2][2], Mat4x4_2[2][2], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[2][3], Mat4x4_2[2][3], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[3][0], Mat4x4_2[3][0], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[3][1], Mat4x4_2[3][1], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[3][2], Mat4x4_2[3][2], places=7, msg=None, delta=None)
        self.assertAlmostEqual(Mat4x4_1[3][3], Mat4x4_2[3][3], places=7, msg=None, delta=None)

    def assert_exactly_equal(self, Mat4x4_1, Mat4x4_2):
        self.assertEqual(Mat4x4_1[0][0], Mat4x4_2[0][0])
        self.assertEqual(Mat4x4_1[0][1], Mat4x4_2[0][1])
        self.assertEqual(Mat4x4_1[0][2], Mat4x4_2[0][2])
        self.assertEqual(Mat4x4_1[0][3], Mat4x4_2[0][3])
        self.assertEqual(Mat4x4_1[1][0], Mat4x4_2[1][0])
        self.assertEqual(Mat4x4_1[1][1], Mat4x4_2[1][1])
        self.assertEqual(Mat4x4_1[1][2], Mat4x4_2[1][2])
        self.assertEqual(Mat4x4_1[1][3], Mat4x4_2[1][3])
        self.assertEqual(Mat4x4_1[2][0], Mat4x4_2[2][0])
        self.assertEqual(Mat4x4_1[2][1], Mat4x4_2[2][1])
        self.assertEqual(Mat4x4_1[2][2], Mat4x4_2[2][2])
        self.assertEqual(Mat4x4_1[2][3], Mat4x4_2[2][3])
        self.assertEqual(Mat4x4_1[3][0], Mat4x4_2[3][0])
        self.assertEqual(Mat4x4_1[3][1], Mat4x4_2[3][1])
        self.assertEqual(Mat4x4_1[3][2], Mat4x4_2[3][2])
        self.assertEqual(Mat4x4_1[3][3], Mat4x4_2[3][3])
# endregion


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   T E S T S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
class TestMat4x4Constructors(unittest.TestCase):
    def test_constructor_empty(self):
        Mat4x4()

    def test_constructor_list(self):
        Mat4x4([
            [0.0, 0.1, 0.2, 0.3],
            [1.0, 1.1, 1.2, 1.3],
            [2.0, 2.1, 2.2, 2.3],
            [3.0, 3.1, 3.2, 3.3]
        ])

    def test_constructor_four_lists(self):
        Mat4x4(
            [0.0, 0.1, 0.2, 0.3],
            [1.0, 1.1, 1.2, 1.3],
            [2.0, 2.1, 2.2, 2.3],
            [3.0, 3.1, 3.2, 3.3]
        )

    def test_invalid_constructors(self):
        self.assertRaises(ValueError, Mat4x4, "a")
        self.assertRaises(ValueError, Mat4x4, 1)
        self.assertRaises(TypeError, Mat4x4, [1, 2, 3, 4])
        self.assertRaises(ValueError, Mat4x4, [])
        self.assertRaises(ValueError, Mat4x4, [[], [], [], []])
        self.assertRaises(TypeError, Mat4x4, ["1", "2", "3", "4"])
        self.assertRaises(TypeError, Mat4x4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], ["1", "2", "3", "4"]])


class TestMat4x4GetByIndex(unittest.TestCase):
    temp_mat = Mat4x4([
        [0.0, 0.1, 0.2, 0.3],
        [1.0, 1.1, 1.2, 1.3],
        [2.0, 2.1, 2.2, 2.3],
        [3.0, 3.1, 3.2, 3.3]
    ])

    def test_get_single_index(self):
        self.temp_mat[0]

    def test_get_double_index(self):
        self.temp_mat[0][0]

    def test_get_by_single_index_correct_values(self):
        self.assertEqual(self.temp_mat[-4], [0.0, 0.1, 0.2, 0.3])
        self.assertEqual(self.temp_mat[-1], [3.0, 3.1, 3.2, 3.3])
        self.assertEqual(self.temp_mat[0], [0.0, 0.1, 0.2, 0.3])
        self.assertEqual(self.temp_mat[1], [1.0, 1.1, 1.2, 1.3])
        self.assertEqual(self.temp_mat[2], [2.0, 2.1, 2.2, 2.3])
        self.assertEqual(self.temp_mat[3], [3.0, 3.1, 3.2, 3.3])

    def test_get_by_double_index_correct_values(self):
        self.assertEqual(self.temp_mat[0][-4], 0.0)
        self.assertEqual(self.temp_mat[0][-1], 0.3)
        self.assertEqual(self.temp_mat[0][0], 0.0)
        self.assertEqual(self.temp_mat[1][1], 1.1)
        self.assertEqual(self.temp_mat[2][2], 2.2)
        self.assertEqual(self.temp_mat[3][3], 3.3)

    def test_get_by_single_index_out_of_range(self):
        self.assertRaises(IndexError, lambda: self.temp_mat[4])

    def test_get_by_double_index_out_of_range(self):
        self.assertRaises(IndexError, lambda: self.temp_mat[0][4])

    def test_get_by_index_non_number(self):
        self.assertRaises(TypeError, lambda: self.temp_mat["a"])
        self.assertRaises(TypeError, lambda: self.temp_mat[1.0])
        self.assertRaises(TypeError, lambda: self.temp_mat[self.temp_mat])
        self.assertRaises(TypeError, lambda: self.temp_mat[0]["a"])
        self.assertRaises(TypeError, lambda: self.temp_mat[0][1.0])
        self.assertRaises(TypeError, lambda: self.temp_mat[0][self.temp_mat])


class TestMat4x4SetByIndex(unittest.TestCase):
    temp_mat = Mat4x4([
        [0.0, 0.1, 0.2, 0.3],
        [1.0, 1.1, 1.2, 1.3],
        [2.0, 2.1, 2.2, 2.3],
        [3.0, 3.1, 3.2, 3.3]
    ])

    def test_set_by_single_index(self):
        temp_mat_copy = self.temp_mat
        temp_mat_copy[0] = [0, 1, 2, 3]
        self.assertEqual(temp_mat_copy[0], [0, 1, 2, 3])

    def test_set_by_double_index(self):
        temp_mat_copy = self.temp_mat
        temp_mat_copy[0][3] = 3
        self.assertEqual(temp_mat_copy[0][3], 3)

    def test_set_using_int(self):
        temp_mat_copy = self.temp_mat
        temp_mat_copy[0][0] = 0
        temp_mat_copy[0][1] = 1
        temp_mat_copy[0][2] = 2
        temp_mat_copy[0][3] = 3
        self.assertEqual(type(temp_mat_copy[0][0]), int)
        self.assertEqual(type(temp_mat_copy[0][1]), int)
        self.assertEqual(type(temp_mat_copy[0][2]), int)
        self.assertEqual(type(temp_mat_copy[0][3]), int)

    def test_set_using_float(self):
        temp_mat_copy = self.temp_mat
        temp_mat_copy[0][0] = 0.0
        temp_mat_copy[0][1] = 0.1
        temp_mat_copy[0][2] = 0.2
        temp_mat_copy[0][3] = 0.3
        self.assertEqual(type(temp_mat_copy[0][0]), float)
        self.assertEqual(type(temp_mat_copy[0][1]), float)
        self.assertEqual(type(temp_mat_copy[0][2]), float)
        self.assertEqual(type(temp_mat_copy[0][3]), float)

    def test_set_by_index_non_number(self):
        with self.assertRaises(TypeError):
            self.temp_mat[0] = "a"
        with self.assertRaises(TypeError):
            self.temp_mat[0] = 1
        with self.assertRaises(TypeError):
            self.temp_mat[0] = {1}
        with self.assertRaises(ValueError):
            self.temp_mat[2] = [0, 1, 2]
        with self.assertRaises(ValueError):
            self.temp_mat[2] = [0, 1, 2, 3, 4]
        with self.assertRaises(TypeError):
            self.temp_mat[3] = self.temp_mat


class TestMat4x4CastToStr(unittest.TestCase):
    temp_mat = Mat4x4([
        [0.0, 0.1, 0.2, 0.3],
        [1.0, 1.1, 1.2, 1.3],
        [2.0, 2.1, 2.2, 2.3],
        [3.0, 3.1, 3.2, 3.3]
    ])

    def test_cast_to_str(self):
        self.assertEqual(str(self.temp_mat), "[[0.0, 0.1, 0.2, 0.3], [1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3], [3.0, 3.1, 3.2, 3.3]]")
        self.assertEqual(str(Mat4x4()), "[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]")


class TestMat4x4CastToList(unittest.TestCase):
    temp_mat = Mat4x4([[0.0, 0.1, 0.2, 0.3], [1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3], [3.0, 3.1, 3.2, 3.3]])

    def test_cast_to_list(self):
        self.assertEqual(list(self.temp_mat), [[0.0, 0.1, 0.2, 0.3], [1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3], [3.0, 3.1, 3.2, 3.3]])
        self.assertEqual(list(Mat4x4()), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


class TestMat4x4Addition(unittest.TestCase):
    temp_mat = Mat4x4([[0.0, 0.1, 0.2, 0.3], [1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3], [3.0, 3.1, 3.2, 3.3]])

    def test_matrix_addition(self):
        MatrixCompare.assert_exactly_equal(self, (self.temp_mat + self.temp_mat), Mat4x4([[0, 0.2, 0.4, 0.6], [2, 2.2, 2.4, 2.6], [4, 4.2, 4.4, 4.6], [6, 6.2, 6.4, 6.6]]))

    def test_matrix_addition_assignment(self):
        temp_mat_copy = self.temp_mat
        temp_mat_copy += self.temp_mat
        MatrixCompare.assert_exactly_equal(self, temp_mat_copy, Mat4x4([[0, 0.2, 0.4, 0.6], [2, 2.2, 2.4, 2.6], [4, 4.2, 4.4, 4.6], [6, 6.2, 6.4, 6.6]]))

    def test_invalid_addition(self):
        self.assertRaises(TypeError, lambda: (self.temp_mat + "a"))
        self.assertRaises(TypeError, lambda: (self.temp_mat + "1"))
        self.assertRaises(TypeError, lambda: (self.temp_mat + 1))
        self.assertRaises(TypeError, lambda: (self.temp_mat + 1.0))
        self.assertRaises(TypeError, lambda: (self.temp_mat + [1.0, 2.0, 3.0]))
        with self.assertRaises(TypeError):
            self.temp_mat += 1
        with self.assertRaises(TypeError):
            self.temp_mat += 1.0


class TestMat4x4Multiplication(unittest.TestCase):
    temp_mat = Mat4x4([
        [0.0, 0.1, 0.2, 0.3],
        [1.0, 1.1, 1.2, 1.3],
        [2.0, 2.1, 2.2, 2.3],
        [3.0, 3.1, 3.2, 3.3]
    ])

    def test_matrix_multiplication(self):
        temp_mat_copy = self.temp_mat * self.temp_mat
        result_mat = Mat4x4([[1.4, 1.46, 1.52, 1.58], [7.4, 7.86, 8.32, 8.78], [13.4, 14.26, 15.12, 15.98], [19.4, 20.66, 21.92, 23.18]])
        MatrixCompare.assert_almost_equal(self, temp_mat_copy, result_mat)

    def test_matrix_multiplication_assignment(self):
        result_mat = Mat4x4([[1.4, 1.46, 1.52, 1.58], [7.4, 7.86, 8.32, 8.78], [13.4, 14.26, 15.12, 15.98], [19.4, 20.66, 21.92, 23.18]])
        temp_mat_copy = self.temp_mat
        temp_mat_copy *= self.temp_mat
        MatrixCompare.assert_almost_equal(self, temp_mat_copy, result_mat)

    def test_matrix_multiplication_with_scalar(self):
        self.assertEqual((2.0 * self.temp_mat), Mat4x4([[0.0, 0.2, 0.4, 0.6], [2.0, 2.2, 2.4, 2.6], [4.0, 4.2, 4.4, 4.6], [6.0, 6.2, 6.4, 6.6]]))
        self.assertEqual((2 * self.temp_mat), Mat4x4([[0.0, 0.2, 0.4, 0.6], [2.0, 2.2, 2.4, 2.6], [4.0, 4.2, 4.4, 4.6], [6.0, 6.2, 6.4, 6.6]]))

    def test_invalid_multiplication(self):
        self.assertRaises(TypeError, lambda: (self.temp_mat * "a"))
        self.assertRaises(TypeError, lambda: (self.temp_mat * "1"))
        self.assertRaises(TypeError, lambda: (self.temp_mat * 1))
        self.assertRaises(TypeError, lambda: (self.temp_mat * 1.0))
        self.assertRaises(TypeError, lambda: (self.temp_mat * [1.0, 2.0, 3.0, 4.0]))


class TestMat4x4Equal(unittest.TestCase):
    temp_mat_1 = Mat4x4([
        [0.0, 0.1, 0.2, 0.3],
        [1.0, 1.1, 1.2, 1.3],
        [2.0, 2.1, 2.2, 2.3],
        [3.0, 3.1, 3.2, 3.3]
    ])
    temp_mat_2 = Mat4x4([
        [-0.0, -0.1, -0.2, -0.3],
        [-1.0, -1.1, -1.2, -1.3],
        [-2.0, -2.1, -2.2, -2.3],
        [-3.0, -3.1, -3.2, -3.3]
    ])
    # NOTE: One negative value at the end, rest positive
    temp_mat_3 = Mat4x4([[0.0, 0.1, 0.2, 0.3], [1.0, 1.1, 1.2, 1.3], [2.0, 2.1, 2.2, 2.3], [3.0, 3.1, 3.2, -3.3]])

    def test_compare_equivalent(self):
        self.assertTrue(self.temp_mat_1 == self.temp_mat_1)
        self.assertTrue(self.temp_mat_2 == self.temp_mat_2)
        self.assertTrue(self.temp_mat_3 == self.temp_mat_3)

    def test_compare_non_equivalent(self):
        self.assertFalse(self.temp_mat_1 == self.temp_mat_2)
        self.assertFalse(self.temp_mat_2 == self.temp_mat_3)
        self.assertTrue(self.temp_mat_1 != self.temp_mat_2)
        self.assertTrue(self.temp_mat_2 != self.temp_mat_3)
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E N T R Y   P O I N T (local 'main')   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    unittest.main()
