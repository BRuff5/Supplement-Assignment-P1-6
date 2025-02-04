import numpy as np


def generate_normal_array(shape, mean, std_dev):
    return np.random.normal(loc=mean, scale=std_dev, size=shape)
    
"""Generate an array.
    Args
        Shape: Shape of the array created
        Mean: Mean of the number
        std_dev: Standard deviation of the normal distribution
    Returns: 
        Numpy array of numbers
"""


def solve_equations_cramers_rule(A, B):
    determinant_A = np.linalg.det(A)
    if determinant_A == 0:
        raise ValueError("The determinant is zero, system error.")
    
    n = A.shape[0]
    solutions = np.zeros(n)
    
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B
        solutions[i] = np.linalg.det(Ai) / determinant_A
    
    return solutions

"""Solve using Cramer's rule.

    Args:
        A: coefficients
        B: constant
    Returns: 
        Values of the variables as a numpy array
"""

def generate_integer_array_with_even_odd_indexes(shape, low=0, high=100):
    array = np.random.randint(low, high, size=shape)
    even_indices = np.where(array % 2 == 0)[0].tolist()
    odd_indices = np.where(array % 2 != 0)[0].tolist()
    
    return even_indices, odd_indices, array

"""Generate an array of integers and returns even and odd numbers.
    Args:
        shape: Shape of the array to be generated
        low: Minimum integer value
        high: Maximum integer value
    Returns: 
        Tuple of indices of even numbers, indices of odd numbers, and the generated array
"""

if __name__ == "__main__":
    mean = 0
    std_dev = 1
    shape = (4, 8)  
    normal_array = generate_normal_array(shape, mean, std_dev)
    print("Normally distributed array:\n", normal_array)
    
    # Solve equation
    A = np.array([[2, 1], [2, 3]])
    B = np.array([8, 13])
    solutions = solve_equations_cramers_rule(A, B)
    print("Solutions to the equations:", solutions)
    
    # Generate array
    shape_integers = (3,) 
    even_indices, odd_indices, integer_array = generate_integer_array_with_even_odd_indexes(shape_integers)
    print("Integer array:", integer_array)
    print("Even indices:", even_indices)
    print("Odd indices:", odd_indices)
    
    