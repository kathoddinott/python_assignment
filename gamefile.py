# import from the random package so we can generate random numbers
from random import randint 

#choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]

computer_choice = choices[randint(0,2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)