🎮 Number Guessing Game with Leaderboard (Python)
📌 Overview

This is a console-based number guessing game written in Python.
The game allows players to:

Create or log in with a username

Play a number guessing game

Earn points based on correct guesses

Store scores in a SQLite database

View a leaderboard ranked by highest score

The program is split into three modules to keep the code clean and organized.

🧩 Project Structure
project/
│
├── main.py                -> Main entry point of the game
├── game_logic.py          -> Handles the game rules and logic
├── database_fun.py        -> Handles database operations (SQLite)
├── game_records.db        -> SQLite database (auto-created)

🛠 Requirements
✅ Software Requirements

Python 3.8 or higher

Windows, Linux, or macOS

Terminal / Command Prompt / PowerShell

✅ Python Libraries Used

All libraries are built-in, no external installation needed:

sqlite3 → database storage

random → number generation

time → delays in gameplay

▶️ How to Run the Program

Open a terminal in the project folder

Run:

python main.py

🎯 How the Game Works
1️⃣ User Selection

When the game starts, the user is asked:

Option 1: Log in with an existing username

Option 2: Create a new username

Usernames are stored in the database and must be unique.

2️⃣ Game Rules

The computer generates three random numbers

One of them is secretly chosen as the correct number

The player must guess the correct number

The player can:

Guess a number

Type help to play Rock-Paper-Scissors for a clue

Type e to exit the game

3️⃣ Scoring System

Each correct guess = 1 point

Wrong guess = 0 points

The game runs 10 rounds

Final score is saved to the database

4️⃣ Help Feature (Rock-Paper-Scissors)

If the player types help:

They play Rock-Paper-Scissors against the computer

Winning gives a range clue for the correct number

Losing gives no clue

5️⃣ Leaderboard

After the game ends:

Scores are updated in the database

A leaderboard is displayed showing:

Rank

Username

Score (highest first)

🧠 Code Explanation (By File)
📄 database_fun.py

Handles all database-related tasks using SQLite.

Features:

Creates the players table if it doesn’t exist

Adds new players

Checks if a username exists

Updates player scores

Fetches leaderboard data

Table Structure:

players(
  username TEXT PRIMARY KEY,
  score INTEGER
)

📄 game_logic.py

Handles all game mechanics.

Functions:

generate_number() → creates random numbers

logic_game() → runs one game round

Key Features:

Input validation

Help system

Win/lose logic

Returns score for each round

📄 main.py

This is the entry point of the program.

Responsibilities:

User login / registration

Running the game loop (10 rounds)

Updating scores

Displaying final results and leaderboard

🧪 Example Output
do you have a username select below
select 1 if you have
select 2 if you do not have
enter your answer: 2
create a username: blair

choose one number (12 or 45 or 78), or press e to exit:

🚀 Possible Improvements

Add password authentication

Save game history

Add difficulty levels

Create a GUI version

Convert to an EXE using PyInstaller

👨‍💻 Author Notes

This project demonstrates:

Python modular programming

Database integration

Game logic design

Input validation

Basic software architecture

It is suitable for beginners to intermediate Python learners.
