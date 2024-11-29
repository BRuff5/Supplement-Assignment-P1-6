import unittest
import numpy as np
from testcases import generate_normal_array, solve_equations_cramers_rule, generate_integer_array_with_even_odd_indexes

class TestFunctions(unittest.TestCase):
    def test_generate_normal_array(self):
        shape = (4, 8)
        mean = 0
        std_dev = 1
        array = generate_normal_array(shape, mean, std_dev)
        self.assertEqual(array.shape, shape)
        self.assertAlmostEqual(np.mean(array), mean, delta=0.5)
        self.assertAlmostEqual(np.std(array), std_dev, delta=0.5)

    def test_solve_equations_cramers_rule(self):
        A = np.array([[2, 1], [2, 3]])
        B = np.array([8, 13])
        solutions = solve_equations_cramers_rule(A, B)
        expected_solutions = np.array([3, 2])  # Solved manually or using a calculator
        np.testing.assert_array_almost_equal(solutions, expected_solutions)

        with self.assertRaises(ValueError):
            solve_equations_cramers_rule(np.array([[1, 2], [2, 4]]), np.array([5, 10]))

    def test_generate_integer_array_with_even_odd_indexes(self):
        shape = (10,)
        even_indices, odd_indices, array = generate_integer_array_with_even_odd_indexes(shape, low=0, high=100)
        for i in even_indices:
            self.assertEqual(array[i] % 2, 0)
        for i in odd_indices:
            self.assertEqual(array[i] % 2, 1)
        self.assertEqual(len(even_indices) + len(odd_indices), len(array))

if __name__ == "__main__":
    unittest.main()
