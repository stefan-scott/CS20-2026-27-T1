# (Comment Header Requirement)

# ****************************************
# Warm-up                (Title)
# Mr. Scott              (Name)
# Nov 12, 2026           (Date)
# Headers + IO excercise (One-line descr.)
# ****************************************

# (inline comment requirements)
#  one comment per function OR
#  major chunk of code not in a function

# 1. Ask the user for an amount in CAD
cad = input("Enter an amount in CAD: ")
cad = float(cad) 

# 2. Convert that amount into YEN (1:112)
yen = cad * 112

# 3. Print out the converted amount
#    in a nice sentence

#         STR      str(FLOAT)   STR
print("You have " + str(yen) + " yen.")
