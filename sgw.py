import random
def get_computer_choice():
    return random.choice(["snake","water","gun"])
def winner(user,computer):
    if user==computer:
        return "it's a tie!"
    elif(user=="snake" and computer == "water")or\
        (user == "water" and computer =="gun")or\
        (user == "gun" and computer =="snake"):
        return "you win"
    else:
        return "computer win!"
def play_game():
    print("welcome to the snake gun water game")
    choice=["snake","gun", "water"]
    while True:
        user_choice=input("enter your choice or exit to quit").lower()
        if user_choice=="exit":
            print("thank you!")
            break
        elif user_choice not in choice:
            print("invalind choice")
            continue
        computer=get_computer_choice()
        print(f"computer choice:{computer}")
        print(winner(user_choice,computer))
play_game()       
        
    
    
