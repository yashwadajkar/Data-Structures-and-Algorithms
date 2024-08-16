# Import the array module
import array

# Creating an array of signed integers ('i' typecode stands for signed integers)
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Function to search for an element in the array using linear search
def searchArray(inputArray, element):
    # Loop through each element in the array
    for i in inputArray:
        # Check if the current element is equal to the element we're searching for
        if i == element:
            return True  # Element found, return True
    return False  # Element not found, return False

# Searching for an element in the array
# This should return False as 0 is not in the array
print("Is 0 in the array?", searchArray(my_array, 0))

# Searching for an element that is in the array
# This should return True as 5 is in the array
print("Is 5 in the array?", searchArray(my_array, 5))
