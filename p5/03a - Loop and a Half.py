# Loop and a Half
# Mr. Scott
# Nov 16, 2026
# "Forever" Loop, break, continue

# break → exit the loop it is most
#         immediately within
# continue → stops the current loop iteration
#            and we begin the next one

while True: #Always repeats...
    choice = input("Pick an option: [one, two] ")
    #ONE One one ONe 
    if choice.lower() == "one":
        print("Breaking out of loop")
        break
    elif choice.upper() == "TWO":
        print("Restarting loop...")
        continue
    else:
        print("please enter a valid choice")
    print("let's ask again!")