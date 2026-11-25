# Reading from files demo
# Mr. Scott
# Nov 24, 2026
# How to read in text data from files
# and format it into a usable state

# Make sure the file to read is in the
# SAME FOLDER as your python file.

# STEP ONE: open the file
my_file = open("poem.txt", "r") #r → READ-ONLY

# STEP TWO: read in the contents

# Option A → read the whole file into a single string
# full_text = my_file.read()
    # usually. at this point we would
    # split up the string somehow....
    
# Option B → Read each line, store in list
list_of_lines = my_file.readlines()

# STEP THREE: strip away newline character
#             for each line
for i in range(len(list_of_lines)):  #i:  0,1,2
    list_of_lines[i] = list_of_lines[i].rstrip("\n")

# TO TEST:
print(f"""A poem:
{list_of_lines[2]}
{list_of_lines[1]}
{list_of_lines[0]}""")

my_file.close()  #LAST STEP
