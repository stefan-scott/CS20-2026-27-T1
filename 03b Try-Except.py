# Try-Except Demo
# Mr. Scott
# Nov 16, 2026
# Trying to stop our programs from crashing...

#          int int     string
my_list = [88, 44, "Twenty Two"]
#          0   1       2          X

# Try/except is a bit like if/else
# If there's an exception in the try section
# Instead of crashing, code jumps to the except...
while True:
    try:
        index = int(input("an index: ")) #ValueError
        chosen_num = my_list[index] #IndexError
        print("num: " + chosen_num) #TypeError
        #If we reach this break statement
        #it implies no exceptions occurred
        #so we can exit the loop
        break
    
    except: #catch-all generic case
        print("Something went wrong...")
#     except TypeError:
#         print("Type Error! The only string is a pos 2")
#     except IndexError:
#         print("Index Error! Valid indices are 0-2")
#     except ValueError:
#         # jumps here if a ValueError occurs in the
#         # try section
#         print("Value Error! Enter a number")