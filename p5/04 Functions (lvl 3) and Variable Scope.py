# Functions w/ Inputs and Outputs
# + Variable Scope
# Mr. Scott
# Nov 17, 2026

# Terms: Arguments, Parameters, Return
# 
#
#

# Variable Scope: WHERE in a program a variable exists
#  - varaible is LOCAL to the CODE BLOCK (def, if, while)
#    it is defined within
#
#  - if you make a variable in a function, it only
#    exists in that function.

# variables listed in the brackets are
# called PARAMETERS and store the inputs
# to the function. They are LOCAL.
def add_three(n1, n2, n3):
    #Adds three numbers together
    #n1,n2,n3 → INT numbers to add
    a = 99 #LOCAL VARIABLE
    print("function",a)
    
    result = n1 + n2 + n3
    #result is LOCAL.
    #If I only need it now, use it in function only
    #If I need it later/elsewhere, RETURN the data.
    return result
    # return immediately EXITS the function
    # and sends a value back to the line that
    # called the function in the first place.

# WITHOUT ANY INDENTATION (not in a code block)
# variables defined here are GLOBAL
# - can be accessed from anywhere
# - can't be changed from within functions
a = 10
# 2,4,6 are ARGUMENTS, and get stored in
# corresponding function PARAMETERS.

# With returned data, 2 main options:
# 1. store in a var
# 2. print it directly / send into another function
r = add_three(2,4,6)
print(add_three(22,33,22))

print("global",a)
