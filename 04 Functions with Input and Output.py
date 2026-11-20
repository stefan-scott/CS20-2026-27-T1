# More about Functions (input/output)
# Mr. Scott
# Nov 17, 2026
#
# Arguments, Parameters, Return
# Variable Scope
#
# Variable Scope: WHERE in a program a variable is accessible
#   - variable is LOCAL to the CODE BLOCK (def, if, while, for)
#     it is defined within.
#
#   - if you make a variable inside a function, it only EXISTS
#     in that function.

# variables inside the brackets are PARAMETERS
# - these are LOCAL to the function
# - they receive the input data
def add_three(num1, num2, num3):
    # adds three numbers together
    # num1,2,3 → INT numbers to add
    
    a = 99
    print("function: ", a)
    result = num1 + num2 + num3
    # result is LOCAL
    # if I only need this value short term: use in function
    # if I need it later/elsewhere, RETURN it from the function
    return result
    #return EXITs the function, but also brings data out...

# WITH NO INDENTATION (not in a code block) → GLOBAL VARIABLE
# can access from anywhere, but CAN'T CHANGE from in a function
a = 10

# With returned data, typically 2 OPTIONS
# 1. Store in a variable
# 2. Print it out directly

r = add_three(2,4,6)
print(r)
print(add_three(5,5,5))
print("global: ", a)

# to change a global from within a function
# use the RETURN mechanism
a = add_three(22,33,22)
print("global", a)
