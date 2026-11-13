print("--- First Python Program ---")

# Ask user for width and height
# and calculate the rect area...

# input() ALWAYS yields a string..

width = input("Enter a width: ")
height = input("Enter a height: ")

# to convert data types:
# str(x)  → convert x to string
# bool(x) → convert x to boolean
# float(x)→ convert x to float
# int(x)  → convert x to integer

width = float(width)
height = float(height)

area = width * height  #area is float

# Output the result to the user
#        STR     +  STR
print("Area is " + str(area))

# Lastly, let's determine if this is
# a SMALL, MEDIUM, or LARGE number...
# 0-99.9      - small
# 100-999.9   - medium
# 1000+       - large

if area < 100:
    print("Small Number")
elif area >=100 and area < 1000:
    print("Medium Number")
else:
    print("Large Number")
    
    