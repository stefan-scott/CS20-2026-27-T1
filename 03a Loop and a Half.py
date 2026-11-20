# Loop and a Half
# Mr. Scott
# Nov 16, 2026
# "Forever" Loop, break, continue

# break → exits the loop it is most
#         immediately within
# continue → stops the current iteration
#            and begins the next one.

while True: #classic "forever" - no way to stop up here...
    choice = input("Stop the Loop? [yes/no]")
    #Yes YES yes yEs
    if choice.lower() == "yes":
        break
    elif choice.upper() == "MAYBE":
        print("restarting loop")
        continue
    else:
        print("invalid choice")
    print("Let's ask again...")
    
    