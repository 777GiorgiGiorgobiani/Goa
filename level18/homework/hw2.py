# 2) თქვენით მოიფიქრეთ რაიმე სავარჯიშო რასაც გააკეთებთ if elif else ით ივარჯიშეთ დღევანდელ ნასწავლ მასალაზე ძალიან ბევრი

from random import *

def bot_select():
    rps = ["Rock", "Paper", "Scissors"]
    rps_choice = rps[randint(0, 2)]
    return rps_choice

def update_health(outcome, health):
    if outcome == "W":
        health = min(100, health + 5)
    elif outcome == "L":
        health = max(0, health - 10)
    return health




def playgame():

    health = 100

    while health > 0:
        bot_choice = bot_select()
        user_choice = input("Pick one; Rock, Paper, Scissors: ")


        if user_choice == bot_choice:
            print("Bot chose:", bot_choice)
            print("It's a tie")
            print("health:", health)



        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Paper" and bot_choice == "Rock") or \
             (user_choice == "Scissors" and bot_choice == "Paper"):
            print("Bot chose:", bot_choice)
            print(f"""Human Won!
                {user_choice} beats {bot_choice}""")
            health = update_health("W", health)
            print("Health:", health)



        else:
            print(f"""Human Lost!
                {bot_choice} beats {user_choice}""")
            health = update_health("L", health)
            print("Health: ", health)
        

        if health <= 0:
            print("!!!Y O U   L O S T!!!")
            break






start_game = input("Do you want to play? Y/N: ")
if start_game == "Y":
    playgame()