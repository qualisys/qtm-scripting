from Classes.vector import Vec3
import unittest


# HOW TO RUN TESTS
# ----------------
# 1. Open a Python interpreter
# 2. Change directory to ..\qtm\Api\Python\Scripts
# 3. Run the command: python -m unittest discover -v


# - - - - - - - - - - - - - - - - - - -  - - - - - -
# ////////   E X P O R T E D   T E S T S   ////////
# - - - - - - - - - - - - - - - - - - - - - - - -
# region [ COLLAPSE / EXPAND ]
class TestVec3Constructors(unittest.TestCase):
    def test_constructor_empty(self):
        Vec3()

    def test_constructor_list(self):
        Vec3([0, -5, 7])
        Vec3([0.1, -5.2, 7.3])

    def test_constructor_three_values(self):
        Vec3(0, -5, 7)
        Vec3(0.1, -5.2, 7.3)

    def test_invalid_constructors(self):
        self.assertRaises(ValueError, Vec3, "a")
        self.assertRaises(ValueError, Vec3, ["1", "2", "3"])
        self.assertRaises(ValueError, Vec3, ["1.0", "2.0", "3.0"])
        self.assertRaises(ValueError, Vec3, "1", "2", "3")
        self.assertRaises(ValueError, Vec3, "1.0", "2.0", "3.0")
        self.assertRaises(ValueError, Vec3, ["a", "b", "c"])
        self.assertRaises(ValueError, Vec3, "a", "b", "c")


class TestVec3GetByIndex(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_get_first_index(self):
        self.temp_vec[0]
        self.temp_vec[-3]
        self.temp_vec[-6]

    def test_get_second_index(self):
        self.temp_vec[1]
        self.temp_vec[-2]
        self.temp_vec[-5]

    def test_get_third_index(self):
        self.temp_vec[2]
        self.temp_vec[-1]
        self.temp_vec[-4]

    def test_get_by_index_correct_values(self):
        self.assertEqual(self.temp_vec[0], 1.0)
        self.assertEqual(self.temp_vec[-3], 1.0)
        self.assertEqual(self.temp_vec[-6], 1.0)
        self.assertEqual(self.temp_vec[1], 2.0)
        self.assertEqual(self.temp_vec[-2], 2.0)
        self.assertEqual(self.temp_vec[-5], 2.0)
        self.assertEqual(self.temp_vec[2], 3.0)
        self.assertEqual(self.temp_vec[-1], 3.0)
        self.assertEqual(self.temp_vec[-4], 3.0)

    def test_get_by_index_out_of_range(self):
        self.assertRaises(IndexError, lambda: self.temp_vec[3])

    def test_get_by_index_non_number(self):
        self.assertRaises(TypeError, lambda: self.temp_vec["a"])
        self.assertRaises(TypeError, lambda: self.temp_vec[1.0])
        self.assertRaises(TypeError, lambda: self.temp_vec[self.temp_vec])


class TestVec3SetByIndex(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_set_first_index(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy[0] = 1.0
        self.assertEqual(temp_vec_copy._x, 1.0)
        temp_vec_copy[-3] = -1.0
        self.assertEqual(temp_vec_copy._x, -1.0)
        temp_vec_copy[-6] = 1.0
        self.assertEqual(temp_vec_copy._x, 1.0)

    def test_set_second_index(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy[1] = 2.0
        self.assertEqual(temp_vec_copy._y, 2.0)
        temp_vec_copy[-2] = -2.0
        self.assertEqual(temp_vec_copy._y, -2.0)
        temp_vec_copy[-5] = 2.0
        self.assertEqual(temp_vec_copy._y, 2.0)

    def test_set_third_index(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy[2] = 3.0
        self.assertEqual(temp_vec_copy._z, 3.0)
        temp_vec_copy[-1] = -3.0
        self.assertEqual(temp_vec_copy._z, -3.0)
        temp_vec_copy[-4] = 3.0
        self.assertEqual(temp_vec_copy._z, 3.0)

    def test_set_using_int(self):
        temp_vec_copy = Vec3(float(self.temp_vec[0]), float(self.temp_vec[1]), float(self.temp_vec[2]))
        temp_vec_copy[0] = 1
        temp_vec_copy[1] = 2
        temp_vec_copy[2] = 3
        self.assertEqual(type(temp_vec_copy._x), int)
        self.assertEqual(type(temp_vec_copy._y), int)
        self.assertEqual(type(temp_vec_copy._z), int)

    def test_set_using_float(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy[0] = 1.0
        temp_vec_copy[1] = 2.0
        temp_vec_copy[2] = 3.0
        self.assertEqual(type(temp_vec_copy._x), float)
        self.assertEqual(type(temp_vec_copy._y), float)
        self.assertEqual(type(temp_vec_copy._z), float)

    def test_set_by_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.temp_vec[3] = 0.0

    def test_set_by_index_non_number(self):
        with self.assertRaises(ValueError):
            self.temp_vec[0] = "a"
        with self.assertRaises(ValueError):
            self.temp_vec[1] = {1}
        with self.assertRaises(ValueError):
            self.temp_vec[2] = self.temp_vec


class TestVec3CastToStr(unittest.TestCase):
    def test_cast_to_str(self):
        self.assertEqual(str(Vec3(1, 2, 3)), "[1, 2, 3]")
        self.assertEqual(str(Vec3(1.0, 2.0, 3.0)), "[1.0, 2.0, 3.0]")
        self.assertEqual(str(Vec3(1.1, 2, 3.3)), "[1.1, 2, 3.3]")


class TestVec3CastToList(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_cast_to_list(self):
        self.assertEqual(list(self.temp_vec), [1.0, 2.0, 3.0])


class TestVec3Addition(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_vector_addition(self):
        self.assertEqual((self.temp_vec + self.temp_vec), Vec3(2, 4, 6))
        self.assertEqual((self.temp_vec + Vec3([1, 2, 3])), Vec3(2, 4, 6))
        self.assertEqual((self.temp_vec + Vec3([1.5, 2.2, 2.6])), Vec3(2.5, 4.2, 5.6))

    def test_vector_addition_assignment(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy += self.temp_vec
        self.assertEqual(temp_vec_copy, Vec3(2, 4, 6))
        temp_vec_copy += Vec3([1, 2, 3])
        self.assertEqual(temp_vec_copy, Vec3(3, 6, 9))

    def test_invalid_addition(self):
        self.assertRaises(TypeError, lambda: (self.temp_vec + "a"))
        self.assertRaises(TypeError, lambda: (self.temp_vec + "1"))
        self.assertRaises(TypeError, lambda: (self.temp_vec + 1))
        self.assertRaises(TypeError, lambda: (self.temp_vec + 1.0))
        self.assertRaises(TypeError, lambda: (self.temp_vec + [1.0, 2.0, 3.0]))
        with self.assertRaises(TypeError):
            self.temp_vec += 1
        with self.assertRaises(TypeError):
            self.temp_vec += 1.0


class TestVec3Subtraction(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_vector_subtraction(self):
        temp_vec_copy = self.temp_vec
        self.assertEqual((temp_vec_copy - self.temp_vec), Vec3(0.0, 0.0, 0.0))
        self.assertEqual((temp_vec_copy - Vec3([1, 2, 3])), Vec3(0.0, 0.0, 0.0))
        temp_vec_copy = temp_vec_copy - (Vec3([1.5, 1.8, 2.6]))
        self.assertAlmostEqual(temp_vec_copy[0], -0.5, places=7, msg=None, delta=None)
        self.assertAlmostEqual(temp_vec_copy[1], 0.2, places=7, msg=None, delta=None)
        self.assertAlmostEqual(temp_vec_copy[2], 0.4, places=7, msg=None, delta=None)

    def test_vector_subtraction_assignment(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy -= self.temp_vec
        self.assertEqual(temp_vec_copy, Vec3(0.0, 0.0, 0.0))
        temp_vec_copy -= Vec3([1.0, 2.0, 3.0])
        self.assertEqual(temp_vec_copy, Vec3(-1.0, -2.0, -3.0))

    def test_invalid_subtraction(self):
        self.assertRaises(TypeError, lambda: (self.temp_vec - "a"))
        self.assertRaises(TypeError, lambda: (self.temp_vec - "1"))
        self.assertRaises(TypeError, lambda: (self.temp_vec - 1))
        self.assertRaises(TypeError, lambda: (self.temp_vec - 1.0))
        self.assertRaises(TypeError, lambda: (self.temp_vec - [1.0, 2.0, 3.0]))
        with self.assertRaises(TypeError):
            self.temp_vec -= 1
        with self.assertRaises(TypeError):
            self.temp_vec -= 1.0


class TestVec3Multiplication(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_vector_dot_product(self):
        self.assertEqual(self.temp_vec * self.temp_vec, 14)
        self.assertEqual(self.temp_vec * Vec3([1, 2, 3]), 14)
        self.assertEqual(self.temp_vec * Vec3([1.5, 2.5, 3.5]), 17)

    def test_vector_dot_product_assignment(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy *= self.temp_vec
        self.assertEqual(temp_vec_copy, 14)
        temp_vec_copy = self.temp_vec
        temp_vec_copy *= Vec3([1.0, 2.0, 3.0])
        self.assertEqual(temp_vec_copy, 14)

    def test_scalar_multiplication(self):
        self.assertEqual(self.temp_vec * 1, Vec3(1.0, 2.0, 3.0))
        self.assertEqual(self.temp_vec * 1.5, Vec3(1.5, 3, 4.5))
        self.assertEqual(self.temp_vec * float("2"), Vec3(2.0, 4.0, 6.0))
        self.assertEqual(self.temp_vec * float("1.5"), Vec3(1.5, 3, 4.5))

    def test_scalar_multiplication_assignment(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy *= 1
        self.assertEqual(temp_vec_copy, Vec3(1, 2, 3))
        temp_vec_copy *= 1.0
        self.assertEqual(temp_vec_copy, Vec3(1.0, 2.0, 3.0))
        temp_vec_copy *= float("2.0")
        self.assertEqual(temp_vec_copy, Vec3(2.0, 4.0, 6.0))

    def test_scalar_multiplication_reverse(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy = 1.0 * temp_vec_copy
        self.assertEqual(temp_vec_copy, Vec3(1.0, 2.0, 3.0))
        temp_vec_copy = float("2.0") * temp_vec_copy
        self.assertEqual(temp_vec_copy, Vec3(2.0, 4.0, 6.0))

    def test_invalid_multiplication(self):
        self.assertRaises(TypeError, lambda: (self.temp_vec * "a"))
        self.assertRaises(TypeError, lambda: (self.temp_vec * "1"))
        self.assertRaises(TypeError, lambda: (self.temp_vec * [1.0, 2.0, 3.0]))


class TestVec3Division(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_scalar_division(self):
        self.assertEqual(self.temp_vec / 1.0, Vec3(1.0, 2.0, 3.0))
        self.assertEqual(self.temp_vec / float("2.0"), Vec3(0.5, 1.0, 1.5))

    def test_scalar_division_assignment(self):
        temp_vec_copy = self.temp_vec
        temp_vec_copy /= 1.0
        self.assertEqual(temp_vec_copy, Vec3(1.0, 2.0, 3.0))
        temp_vec_copy /= float("2.0")
        self.assertEqual(temp_vec_copy, Vec3(0.5, 1.0, 1.5))

    def test_invalid_division(self):
        self.assertRaises(TypeError, lambda: (self.temp_vec / "a"))
        self.assertRaises(TypeError, lambda: (self.temp_vec / "1"))
        self.assertRaises(TypeError, lambda: (self.temp_vec / [1.0, 2.0, 3.0]))
        self.assertRaises(TypeError, lambda: (self.temp_vec / self.temp_vec))


class TestVec3Equal(unittest.TestCase):
    temp_vec_1 = Vec3(1, 2, 3)
    temp_vec_2 = Vec3(-1, 2, 3)

    def test_compare_equivalent(self):
        self.assertTrue(self.temp_vec_1 == Vec3(1.0, 2.0, 3.0))
        self.assertTrue(self.temp_vec_2 == Vec3([-1.0, 2.0, 3.0]))

    def test_compare_non_equivalent(self):
        self.assertFalse(self.temp_vec_1 == self.temp_vec_2)
        self.assertTrue(self.temp_vec_1 != self.temp_vec_2)


class TestVec3Magnitude(unittest.TestCase):
    def test_calculate_magnitude(self):
        self.assertEqual(Vec3(1, 2, 2).magnitude(), 3.0)


class TestVec3CrossProduct(unittest.TestCase):
    temp_vec = Vec3(1, 2, 3)

    def test_cross_product(self):
        self.assertEqual(self.temp_vec.cross(Vec3(1.0, 2.0, 3.0)), Vec3(0.0, 0.0, 0.0))
        self.assertEqual(self.temp_vec.cross(Vec3(3.0, 2.0, 1.0)), Vec3(-4.0, 8.0, -4.0))

    def test_invalid_cross_product(self):
        self.assertRaises(TypeError, self.temp_vec.cross, 1)
        self.assertRaises(TypeError, self.temp_vec.cross, "a")
        self.assertRaises(TypeError, self.temp_vec.cross, "1")
        self.assertRaises(TypeError, self.temp_vec.cross, [1.0, 2.0, 3.0])
# endregion


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ////////   E N T R Y   P O I N T (local 'main')   ////////
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    unittest.main()
