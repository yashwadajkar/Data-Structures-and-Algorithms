# Method 1: Using the Standard Array Library

import array

# Creating an array of signed integers
my_array = array.array('i', [1, 2, 3, 4])
print(my_array)  # Output: array('i', [1, 2, 3, 4])

# Method 2: Using the NumPy Module

import numpy as np

# Creating a NumPy array
my_array = np.array([1, 2, 3, 4], dtype=int) # dtype denotes the datatype

# Printing the NumPy array
print(my_array)