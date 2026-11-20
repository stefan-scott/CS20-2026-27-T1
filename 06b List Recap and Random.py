# List Modify + Madlib
# Mr. Scott
# Nov 19, 2026

# ----------- LIST MODIFY ---------------
# foods[2] = x    → replace item at pos 2 with x
# foods.append(x) → adds x to the end of the list
# foods.pop(i)    → removes and returns item a pos i

#           0         1           2 
foods = ["apple", "banana", "cantaloupe"]
foods[2] = "durian"
foods.append("eggplant")
foods.pop(1)

# ------ random ------- 
import random
# random.choice(list) → pick one item at random

# MICRO MADLIB
def create_story():
    # be used to generate a simple madlib
    num = input("enter a number 1-10: ")
    cost = input("enter a cost: ")
    food = random.choice(foods)
    
    # generate a story using substitutions (f-string)
    # if string starts and ends with """    """
    # the string can span multiple lines
    story = f"""I am hungry for {food}.
I wish I had {num}.
But I would need {cost} dollars. """
    print(story)

# MAIN CODE STARTS HERE (Madlib)
create_story()
    



