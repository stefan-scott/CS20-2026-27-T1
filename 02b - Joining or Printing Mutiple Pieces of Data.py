# Printing | Joining Multiple Things
# Mr. Scott
# Nov 12, 2026
# Three ways to output text from
# Multiple variables in print()

# can convert data forms
# str()  int()  float()  bool()

# Create Some Variables
name = "Timothy"
age = 22
height = 170.5
awake = True

# Three main ways to print multiple
# Values / Data Types

#1. Join strings using +  (concatenation)
#   -must ensure all values are strings
#   -python adds no spaces/newlines

#      STR    STR   str(int)     STR
print(name + "is" + str(age) + "yrs old.")

#2. If using print(), can separate each data item
#   with a comma
#    - print() adds a space b/w each thing
#    - data types can be mixed
print(name, "is", age, "yrs old.")

#3. Formatted String
#     - combine a string literal with:
#       variable / code substitution.
#     - special symbol before ""   f
#     - no added whitespace
result = f"Hello there, {name}"
# result +=      means:  result = result + ______
result += f" You are {age} years old."
print(result)