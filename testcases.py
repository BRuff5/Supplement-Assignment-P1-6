import numpy as np
import pytest
from your_module_name import generate_normal_array, solve_equations_cramers_rule

def test_generate_normal_array_shape():
    shape = (3, 3)
    mean = 0
    std_dev = 1
    result = generate_normal_array(shape, mean, std_dev)
    assert result.shape == shape

def test_generate_normal_array_mean_std_dev():
    shape = (1000,)
    mean = 5
    std_dev = 2
    result = generate_normal_array(shape, mean, std_dev)
    assert abs(np.mean(result) - mean) < 0.1
    assert abs(np.std(result) - std_dev) < 0.1

def test_solve_equations_cramers_rule():
    A = np.array([[2, -1], [1, 1]])
    B = np.array([1, 3])
    result = solve_equations_cramers_rule(A, B)
    expected = np.array([2, 1])  # Solves 2x - y = 1, x + y = 3
    np.testing.assert_almost_equal(result, expected)

def test_zero_determinant():
    A = np.array([[1, 2], [2, 4]])
    B = np.array([1, 2])
    with pytest.raises(ValueError):
        solve_equations_cramers_rule(A, B)
