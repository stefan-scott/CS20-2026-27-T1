# Reading Data from Files
# Mr. Scott
# Nov 24, 2026

# Make sure the file(s) to read are located
# in the SAME FOLDER as your python file.

# STEP ONE: open the file (file handle variable)
my_file = open("poem.txt", "r") #r → read only

# STEP TWO: read the contents.
# Option One: read whole file into a string
# full_text = my_file.read()

# Option Two: read each line, store in list
line_list = my_file.readlines()

# STEP THREE: Strip away any newline chars
#             for each item
for i in range(len(line_list)): #i: 0, 1, 2...
    line_list[i] = line_list[i].rstrip("\n")

# TO TEST
print(f"""A poem:
{line_list[0]}
{line_list[1]}
{line_list[2]}
""")