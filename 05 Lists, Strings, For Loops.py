# Lists, Strings, For Loops
# Mr. Scott
# November 18, 2026
# More basic python practice

# ------ LISTS ---------
pet_names = ["Goldfish", "Luca", "Whisky", "Margie", "Bart"]
#                 0         1        2         3        4
#                -5        -4       -3        -2       -1

# access list items
# pet_names[3]   → access item at index 3 ("Margie")
# pet_names[-1]  → negative index counts from right to left
# len(pet_names) → returns # items as INT

# ------ For Loops -------
# repeats ONCE per item in a collection (string/list)
# current item is stored in a LOOP VARIABLE

#for loop_var   in  collection
# for current_pet in pet_names: #repeat 5:
#     print(f"I love my pet {current_pet}")
    
# If you just want to repeat N times
# use range(n) → autogenerates a list with n items
#                  0,1,2,3,4,...,n-1

# for i in range(6):  #[0,1,2,3,4,5]
#     print(f"hi {i}")
#             inc,excl

# for i in range(5,10):  #[5,6,7,8,9]
#     print(f"hi {i}")
                          #[5,10,15,20,25,...,90,95]
# for i in range(0, 100, 5):  #start, end, skip
#     print(f"hi {i}")

for letter in "Centennial Collegiate":
    if letter=="e":
        print(3)
    else:
        print(letter)