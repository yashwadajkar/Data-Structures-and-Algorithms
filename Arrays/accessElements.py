# Import the array module
import array

# Creating an array of signed integers ('i' typecode stands for signed integers)
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Function to access an element at a specific index in the array
def accessElements(inputArray, index):
    # Check if the index is within the valid range
    if index >= len(inputArray) or index < 0:
        return None  # Return None if the index is out of range
    else:
        # Return the element at the specified index
        return inputArray[index]

# Accessing the element at index 4 and printing it
# This should return the 5th element in the array, which is 5 (since index is 0-based)
print("Element at index 4:", accessElements(my_array, 4))

# Attempting to access an element at an out-of-range index
# This should print an error message
print("Element at index 10:", accessElements(my_array, 10))
