import random

choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


# Freeplay Functions


def rock():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")      

    print(f"I choose {tell_player}")      

    if tell_player.lower() == 'rock':
        print("Stop hitting yourself")
    if tell_player.lower() == 'scissors':
        print("You crushed scissors!!!")
    if tell_player.lower() == 'paper':
        print("Paper covered you")
    if tell_player.lower() == 'lizard':
        print("You smashed lizard!!!")
    if tell_player.lower() == 'spock':
        print("Spock vaporized you")


def scissors():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("Rock crushed you!!!")
    if tell_player.lower() == 'scissors':
        print("Stop hitting yourself")
    if tell_player.lower() == 'paper':
        print("You cut paper")
    if tell_player.lower() == 'lizard':
        print("You decapitated lizard!!!")
    if tell_player.lower() == 'spock':
        print("Spock smashed you!!!")


def paper():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("You covered rock")
    if tell_player.lower() == 'scissors':
        print("Scissors cut you")
    if tell_player.lower() == 'paper':
        print("Stop hitting yourself")
    if tell_player.lower() == 'lizard':
        print("Lizard ate you")
    if tell_player.lower() == 'spock':
        print("You disproved Spock")


def lizard():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("Rock smashed you!!")
    if tell_player.lower() == 'scissors':
        print("Scissors decapitated you!!")
    if tell_player.lower() == 'paper':
        print("You ate paper")
    if tell_player.lower() == 'lizard':
        print("Stop hitting yourself")
    if tell_player.lower() == 'spock':
        print("You poisoned Spock")


def spock():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("You vaporized rock")
    if tell_player.lower() == 'scissors':
        print("You smashed scissors!!")
    if tell_player.lower() == 'paper':
        print("Paper disproved you")
    if tell_player.lower() == 'lizard':
        print("Lizard poisoned you")
    if tell_player.lower() == 'spock':
        print("Stop hitting yourself")


# Ranked Functions


def ranked_rock():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")      

    print(f"I choose {tell_player}")      

    if tell_player.lower() == 'rock':
        print("Stop hitting yourself")
        score(scoreboard)
    elif tell_player.lower() == 'scissors':
        print("You crushed scissors!!!")
        scoreboard[name] += 1
        score(scoreboard)
    elif tell_player.lower() == 'paper':
        print("Paper covered you")
        scoreboard[pc_name] += 1
        score(scoreboard)
    elif tell_player.lower() == 'lizard':
        print("You smashed lizard!!!")
        scoreboard[name] += 1
        score(scoreboard)
    elif tell_player.lower() == 'spock':
        print("Spock vaporized you")
        scoreboard[pc_name] += 1
        score(scoreboard)


def ranked_scissors():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")      

    print(f"I choose {tell_player}")      

    if tell_player.lower() == 'rock':
        print("Rock crushed you!!!")
        scoreboard[pc_name] += 1
        score(scoreboard)   
    elif tell_player.lower() == 'scissors':
        print("Stop hitting yourself")
        score(scoreboard)
    elif tell_player.lower() == 'paper':
        print("You cut paper")
        scoreboard[name] += 1
        score(scoreboard)
    elif tell_player.lower() == 'lizard':
        print("You decapitated lizard!!!")
        scoreboard[name] += 1
        score(scoreboard)
    elif tell_player.lower() == 'spock':
        print("Spock smashed you")
        scoreboard[pc_name] += 1
        score(scoreboard)


def ranked_paper():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("You covered rock")
        scoreboard[name] += 1
        score(scoreboard) 
    if tell_player.lower() == 'scissors':
        print("Scissors cut you")
        scoreboard[pc_name] += 1
        score(scoreboard) 
    if tell_player.lower() == 'paper':
        print("Stop hitting yourself")
        score(scoreboard) 
    if tell_player.lower() == 'lizard':
        print("Lizard ate you")
        scoreboard[pc_name] += 1
        score(scoreboard) 
    if tell_player.lower() == 'spock':
        print("You disproved Spock")
        scoreboard[name] += 1
        score(scoreboard) 


def ranked_lizard():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("Rock smashed you!!")
        scoreboard[pc_name] += 1
        score(scoreboard) 
    if tell_player.lower() == 'scissors':
        print("Scissors decapitated you!!")
        scoreboard[pc_name] += 1
        score(scoreboard)         
    if tell_player.lower() == 'paper':
        print("You ate paper")
        scoreboard[name] += 1
        score(scoreboard) 
    if tell_player.lower() == 'lizard':
        print("Stop hitting yourself")
        score(scoreboard) 
    if tell_player.lower() == 'spock':
        print("You poisoned Spock")
        scoreboard[name] += 1
        score(scoreboard) 


def ranked_spock():
    tell_player = random.choice(choices)

    print(f"Ryan chooses {tell_player}")

    print(f"I choose {tell_player}")

    if tell_player.lower() == 'rock':
        print("You vaporized rock")
        scoreboard[name] += 1
        score(scoreboard)        
    if tell_player.lower() == 'scissors':
        print("You smashed scissors!!")
        scoreboard[name] += 1
        score(scoreboard)        
    if tell_player.lower() == 'paper':
        print("Paper disproved you")
        scoreboard[pc_name] += 1
        score(scoreboard)        
    if tell_player.lower() == 'lizard':
        print("Lizard poisoned you")
        scoreboard[pc_name] += 1
        score(scoreboard)       
    if tell_player.lower() == 'spock':
        print("Stop hitting yourself")
        score(scoreboard)        


def score(board):
    for name, points_player in scoreboard.items():
        print("{} ({})".format(name, points_player))

    

scoreboard = {}

# def score(board):
#     for name, points_player in scoreboard.items():
#         print("{} ({})".format(name, points_player))
#         if scoreboard[name] == "3":
#             break


while True:
    welcome = input("Hi, welcome to our game.  Would you like to play? Y/N: ")
    if welcome.lower() == 'n':
        print("Maybe next time")
        break

    elif welcome.lower() == 'y':
        player_input = input("There are 2 game types: Free(non-competitive) and Ranked(Best of 5)\nWhich mode would you like to play?: Free or Ranked: ")
        if player_input.lower() == 'free':

            name = input("What is your name? ").title()
            pc_name = "Ryan"
            print(f"Hello, {name}!!  Enjoy your time.\nWhen you are finished type Quit, but for now...")
            while True:
                ask_player = input("Would you like to choose Rock, Paper, Scissors, Lizard, or Spock?: ").title()
                if ask_player.lower() == 'rock':
                    print(f"You chose {ask_player}")
                    rock()
                elif ask_player.lower() == 'scissors':
                    print(f"You chose {ask_player}")
                    scissors()
                elif ask_player.lower() == 'paper':
                    print(f"You chose {ask_player}")
                    paper()
                elif ask_player.lower() == 'spock':
                    print(f"You chose {ask_player}")
                    spock()
                elif ask_player.lower() == 'lizard':
                    print(f"You chose {ask_player}")

            name = input("What is your name? ")
            pc_name = "Ryan"
            print(f"Hello, {name.title()}!!  Enjoy your time.\nWhen you are finished type Quit, but for now...")
            while True:
                ask_player = input("Would you like to choose Rock, Paper, Scissors, Lizard, or Spock?: ")
                if ask_player.lower() == 'rock':
                    print(f"You chose {ask_player.title()}")
                    rock()
                elif ask_player.lower() == 'scissors':
                    print(f"You chose {ask_player.title()}")
                    scissors()
                elif ask_player.lower() == 'paper':
                    print(f"You chose {ask_player.title()}")
                    paper()
                elif ask_player.lower() == 'spock':
                    print(f"You chose {ask_player.title()}")
                    spock()
                elif ask_player.lower() == 'lizard':
                    print(f"You chose {ask_player.title()}")

                    lizard()
                elif ask_player.lower() == 'quit':
                    print("Thanks for playing.")
                    break
                else:
                    print("Sorry, that input is not valid.")
              
        elif player_input.lower() == 'ranked':

            name = input("What is your name? ").title()
            pc_name = "Ryan"
            scoreboard = {}
            scoreboard[name] = 0
            scoreboard[pc_name] = 0
            print(f"Hello, {name}!!  You are playing {pc_name}.  Good luck, you're going to need it.")
            while scoreboard[name] or scoreboard[pc_name] != 3:
                ask_player = input("Would you like to choose Rock, Paper, Scissors, Lizard, or Spock?: ")
                if ask_player.lower() == 'rock':
                    print(f"You chose {ask_player}")
                    ranked_rock()
                elif ask_player.lower() == 'scissors':
                    print(f"You chose {ask_player}")
                    ranked_scissors()
                elif ask_player.lower() == 'paper':
                    print(f"You chose {ask_player}")
                    ranked_paper()   
                elif ask_player.lower() == 'spock':
                    print(f"You chose {ask_player}")
                    ranked_spock() 
                elif ask_player.lower() == 'lizard':
                    print(f"You chose {ask_player}")
                    ranked_lizard()
                else:
                    print("Please choose a valid input.")
                if scoreboard[name] == 3:
                    print(f"Congratulations!! You beat {pc_name}!!")
                    print(scoreboard)
                    break
                elif scoreboard[pc_name] == 3:
                    print(f"Sorry {name}, {pc_name} destroyed you.")
                    print(scoreboard)
                    break

            name = input("What is your name? ")
            pc_name = "Ryan"
            scoreboard[name] = 0
            scoreboard[pc_name] = 0
            print(f"Hello, {name.title()}!!  You are playing {pc_name}.  Good luck, you're going to need it.\nWhen you are finished type Quit, but for now...")
            while True:
                def score(board):
                    for name, points_player in scoreboard.items():
                        print("{} ({})".format(name, points_player))
                ask_player = input("Would you like to choose Rock, Paper, Scissors, Lizard, or Spock?: ")
                if ask_player.lower() == 'rock':
                    print(f"You chose {ask_player.title()}")
                    ranked_rock()
                elif ask_player.lower() == 'scissors':
                    print(f"You chose {ask_player.title()}")
                    ranked_scissors()
                elif ask_player.lower() == 'paper':
                    print(f"You chose {ask_player.title()}")
                    ranked_paper()   
                elif ask_player.lower() == 'spock':
                    print(f"You chose {ask_player.title()}")
                    ranked_spock() 
                elif ask_player.lower() == 'lizard':
                    print(f"You chose {ask_player.title()}")
                    ranked_lizard()
                elif scoreboard[name] == "3":
                    print(f"Game Over: {scoreboard}")
                    break
                else:
                    print("Sorry, that input is not valid.")
                
                    
                    
                

        
        


        

        
            

        
    

