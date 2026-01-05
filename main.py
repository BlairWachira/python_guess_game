from database_fun import*
from game_logic import*

print("do you have a username select below")
print("select 1 if you have")
print("select 2 if you do not have")
d_ans=int(input("enter your answer: ")) 

if d_ans==1:
    username=input("enter your user name: ")
    if not player_exists(username):
      print("user not found")
      exit()
else:
  username=input("create a username: ")
  add_player(username,0)
  if player_exists(username):
    print("username already taken")
    exit()


score=0
for i in range(10):
  score += logic_game()

update_score(username,score)
print(f"Game over! {username}, your score is {score}/10")

print("\n LEADERBOARD ")
for rank, (user, s) in enumerate(get_leaderboard(), start=1):
    print(f"{rank}. {user} → {s}")


