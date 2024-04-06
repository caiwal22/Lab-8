# Caitlin Walling
# UWYO COSC 1010
# Submission Date
# Lab 8
# Lab Section: 40
# Sources, people worked with, help given to: Autumn, TA
# your
# comments
# here


# Create a function is_number that returns `True` if the supplied variable is an int or a float
# otherwise it will return false
# It needs one parameter, the number to check

def is_number(num):
    if type(num) is int or type(num) is float:
        return True
    else:
        return False
        
# Call your function for each element in the list below to verify that it works, print what value was checked and the result of each call

# Should be: True, False, False, False, True, True, False
random_things = [1886, "Pokes", True, "7220", 72.20, 1889.006, []]

for elem in random_things:
    print(f"Checking {elem}, result:\t{is_number(elem)}")
print("*" * 75)

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Otherwise return the converted int or float
# Floats should only have one decimal point in them
def adv_convert(num):
    negative=False
    if num[0]=="-":
        negative=True
        num=num.replace("-", "")
    if "." in num:
        split_num=num.split(".")
        if len(split_num)==2 and split_num[0].isdigit() and split_num[1].isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    else:
        return False

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

def slope_intercept(m,b,lower_bound,upper_bound):
    if (is_number(m) and is_number(b) and is_number(lower_bound) and is_number(upper_bound) and (lower_bound < upper_bound)):
        for x in range(lower_bound,upper_bound):
            y = (m*x) + b
            y_values.append(y)
            y_values = []
        return y_values
while True:
    m_input = input("Enter a value for 'm' or type 'exit' to quit: ")
    if m_input == "exit":
        break
    b_input = input("Enter a value for 'b' or type 'exit' to quit: ")
    if b_input == "exit":
        break
    lower_bound_input = input("Enter a value for 'lower bound' or type 'exit' to quit: ")
    if lower_bound_input == "exit":
        break
    upper_bound_input = input("Enter a value for 'upper bound' or type 'exit' to quit: ")
    if upper_bound_input == "exit":
        break
    result = slope_intercept(m,b,lower_bound,upper_bound)
    if result:
        print("Y values for the given x range:", result)

print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# You will again need to ensure that all inputs are numbers
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return false
