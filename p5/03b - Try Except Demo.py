# Try-Except Demo
# Mr. Scott
# Nov 16, 2026
# Try to stop our programs from crashing

#          int  int     str
my_list = [88,  44, "Twenty Two"]
#           0    1        2          X

# try-except is a bit like if-else
# run the code in TRY, knowing there might
# an exception.
# If there is, code jumps to the EXCEPT
while True:
    try:
        index = int(input("an index: ")) #ValueError
        chosen_num = my_list[index] #IndexError
        print("Num: " + chosen_num) #TypeError
        # if we reach this line (↓), there
        # were no exceptions. So no need
        # to repeat
        break
#     except TypeError:
#         print("Type Error! Choose string at pos 2")
#     except IndexError:
#         print("Number must be in range 0-2")
#     except ValueError:
#         print("Value Error. Enter a number")
    except: #catch-all generic exception
        print("Something went wrong.")
        