import sqlite3
conn=sqlite3.connect("game_records.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS players(username TEXT PRIMARY KEY,score INTEGER)""")

def add_player(username,score):
  try:
    cursor.execute("INSERT INTO players(username,score)VALUES(?,?)",(username,score))
    conn.commit()
    print("player added sucessfully")
    return True
  except sqlite3.IntegrityError:
    print(f"{username} aready exixts try again")
    
def player_exists(username):
  cursor.execute("SELECT *FROM players WHERE username=?",(username,))
  return cursor.fetchone() is not None

def update_score(username,score):
  cursor.execute("UPDATE players set score=? WHERE username=?",(score,username))
  conn.commit()

def get_leaderboard():
    cursor.execute("SELECT username, score FROM players ORDER BY score DESC")
    return cursor.fetchall()



