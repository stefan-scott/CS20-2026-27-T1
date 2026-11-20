# Lists, Strings, For Loops
# Mr. Scott
# Nov 18, 2026
# Some more Python practice...

# ------------ LISTS ---------------
#  num items:  1      2       3       4           5
pet_names = ["Bob","Midna","Rufus","Steve","Liquideous Esq."]
#              0      1       2       3           4  (num_items-1)
#             -5     -4      -3      -2          -1

# access list items:
# pet_names[3]   → accesses item at index 3 ("Rufus")
# pet_names[-1]  → negative index counts from right to the left
# len(pet_names) → return # items

# ------------ For Loops     + strings -----------
# repeats ONCE per item in a collection (string/list)
# current item is stored in a LOOP VARIABLE

#for  loop_var  in   collection
# for current_pet in pet_names: #repeat 5
#     print(f"I love my pet {current_pet}")

# If you just want to repeat n times
# use range(n) → autogenerates list w/ n things
# 0, 1, 2, 3, 4, ..., n-1
# for i in range(5):  #[0,1,2,3,4]
#     print(f"hi {i}")

#             inc,exc
# for i in range(5,10): #[5,6,7,8,9]
#     print(f"hi {i}")
    
# for i in range(0,100,5): #start, end, step 
#     print(f"hi {i}")

for letter in "SASKATOON":
    if letter == "S":
        print("$")
    else:
        print(letter)
 