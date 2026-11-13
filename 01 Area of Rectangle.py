print("--- First Python Program ---")

# Write code to calculate area of a rectangle

# Ask user for a width, store in var
# input()  ALWAYS yields a string.

width = input("Enter a width:")
height = input("Enter a height:")

# In order to do math (multiply), we need to
# change these variables from strings to
# numbers.

width = float(width)
height = float(height)

# str(x)  → convert x to a string
# bool(x) → convert x to a boolean
# int(x)  → convert x to a integer
# float(x)→ convert x to a float

# calculate result and print as output:
area = width * height

#        STR   +   STR
# joining strings, no spaces added for you...
print("Area is " + str(area))

# To finish, let's check if it's a BIG number
# 0-99.9     small
# 100-999.9  med
# 1000+      large
if area < 100:
    print("SMALL NUMBER")
elif area < 1000:
    print("MED")
else:
    print("LARGE NUMBER")

