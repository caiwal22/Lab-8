# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Create a function is_number that returns `True` if the supplied variable is an int or a float
# otherwise it will return false
# It needs one parameter, the number to check

# Call your function for each element in the list below to verify that it works, print what value was checked and the result of each call

# Should be: True, False, False, False, True, True, False
random_things = [1886, "Pokes", True, "7220", 72.20, 1889.006, []]

for elem in random_things:
    print(f"Checking {elem}, result:\t{"""your function call here"""}")
print("*" * 75)


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Otherwise return the converted int or float
# Floats should only have one decimal point in them

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive
# Check to make sure that the lower bound is less than or equal to the upper bound
# Ensure that all input values are numbers (good thing you have a function for that!) return false if not
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# You will again need to ensure that all inputs are numbers
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does teh square root operation 
    # If the number you are trying to take the square root of is negative, return false
