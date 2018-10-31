from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5

def winorlose(status):
    print("Called win or lose function")
    print("***********************************")
    print("You", status, " ! would like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":

        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = Falsecomputr = choices[randint(0,2)]
    elif choice == "N" or choice == "n":
        print("You chose to quit!")
        print("****************************************")
        exit()

computer_choice = choices[randint(0, 2)]

# print the choice to the terminal window
print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
    print("==================================")
    print("player lives:", player_lives, "/5")
    print("==================================")
    # set player to True by making a selection
    print("Choose your weapon")
    player = input("Rock, Paper or Scissors?")

    print(player, "\n")
    # check for a tie = choices are the same
    if player == computer_choice:
        print("Tie! You live to shoot another day")

    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
        # computer won. crap!!
            player_lives = player_lives - 1
            print("You lose!", computer_choice, "covers", player)
        else:
        # we win! such winning
            computer_lives = computer_lives - 1
            print("You win!", player, "smashed", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            player_lives = player_lives -1
            print("You lose!", computer_choice, "cut", player)
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            player_lives = player_lives -1
            print("You lose!", computer_choice, "smashed", player)
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "cut", computer_choice)

    elif player == "Quit":
        exit()

    else:
        print("Check your spelling... that's not a valid choice\n")

        #check for win or lose
    if player_lives is 0:
            winorlose("lose")

    if computer_lives is 0:
            winorlose("win")

    player = False
    computer_choice = choices[randint(0, 2)]
