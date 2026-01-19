from database_fun import *
from game_logic import *

def ask_username():
    while True:
        print("Do you have a username? Select below:")
        print("1. Yes")
        print("2. No")
        try:
            d_ans = int(input("Enter your answer (1 or 2): "))
            if d_ans in [1, 2]:
                return d_ans
        except ValueError:
            pass
        print("Invalid choice. Try again.\n")

def get_username():
    while True:
        choice = ask_username()
        if choice == 1:
            username = input("Enter your username: ")
            if player_exists(username):
                return username
            else:
                print("User not found. Try again.\n")
        else:  
            username = input("Create a new username: ")
            if player_exists(username):
                print("Username already taken. Try again.\n")
            else:
                add_player(username, 0)
                return username

username = get_username()
score = 0
for i in range(10):
    score += logic_game()

update_score(username, score)
print(f"\nGame over! {username}, your score is {score}/10")

print("\nLEADERBOARD")
for rank, (user, s) in enumerate(get_leaderboard(), start=1):
    print(f"{rank}. {user} → {s}")



