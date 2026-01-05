import time,random
def generate_number():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    num3=random.randint(1,100)

    computer_number=random.choice([num1,num2,num3])
    return computer_number, num1 , num2,num3

def logic_game():
    computer_number, num1, num2 ,num3 = generate_number()

    while True:
        user_answer = input(
            f"choose one number ({num1} or {num2} or {num3} ), or press e to exit: "
        )

        if user_answer.lower() == "e":
            print("bye 😒")
            time.sleep(2)
            exit()

        if user_answer.lower() == "help":
            print("play rock paper scissors to get a clue")

            while True:
                computer_play = random.choice(["rock", "paper", "scissors"])
                user_choice = input("enter [rock, paper, scissors] or exit: ")

                if user_choice == "exit":
                    break

                if computer_play == user_choice:
                    print("same choice, no clue")
                elif (user_choice == "rock" and computer_play == "scissors") or \
                     (user_choice == "paper" and computer_play == "rock") or \
                     (user_choice == "scissors" and computer_play == "paper"):
                    print("you WON!!!!")
                    print(
                        f"clue: number is between {computer_number-10} and {computer_number+10}"
                    )
                    break
                else:
                    print(f"you lost 🤣 computer chose {computer_play}")

            continue 

        if not user_answer.isdigit():
            print("enter integer\n")
            continue

        user_answer = int(user_answer)

        if user_answer == computer_number:
            print("you are correct ✅\n")
            return 1
        else:
            print("you guessed wrongly 🤦‍♂️")
            print(f"computer chose {computer_number}\n")
            return 0
