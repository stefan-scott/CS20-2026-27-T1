# List Recap, Random, Mini Madlib
# Mr. Scott
# Nov 19, 2026
# Preparing for Assignment 2

# LIST MODIFY
# foods[1] = x  → set item at pos 1 to x
# foods.append(x) → add x to the end of list
# foods.pop(i) → remove AND return item at pos i

#           0         1          2           3
foods = ["apple", "banana", "cantaloupe"] #"eggplant"
foods[1] = "durian"
foods.append("eggplant")
foods.pop(0)

# ------- RANDOM -------
import random  #usually this is at very top
# random.choice(list) → picks one item at random

# MICRO MADLIB
def create_story():
    # create a simple madlib
    num = input("enter a number 1-10: ")
    cost = input("enter a cost: ")
    food = random.choice(foods)
    # generate a story w/ substitutions
    story = f"""I am hungry for {food}.
I wish I had {num}.
But I would need {cost} dollars!"""
    print(story)

# MAIN CODE STARTS HERE...
create_story()
    


