import unittest
#import numpy as np
from main import (
    generate_normal_array,
)

class TestYourFunctions(unittest.TestCase):

    def test_generate_normal_array(self):
        shape = (3, 4)
        mean = 0
        std_dev = 1
        array = generate_normal_array(shape, mean, std_dev)
        self.assertEqual(array.shape, shape)
        self.assertTrue(np.isclose(np.mean(array), mean, atol=1))
        self.assertTrue(np.isclose(np.std(array), std_dev, atol=1))