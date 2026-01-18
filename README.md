# 🎮 Number Guessing Game with Leaderboard

A **console-based number guessing game** in Python. Players can log in, play the game, earn points, and compete on a leaderboard. Scores are stored in a SQLite database.

---

## 📌 Overview

The game allows players to:

* Create or log in with a **username**
* Play a **number guessing game**
* Earn points based on **correct guesses**
* Store scores in a **SQLite database**
* View a **leaderboard** ranked by highest score

The project is split into modules for clean organization.

---

## 🧩 Project Structure

```
project/
├── main.py           # Main entry point of the game
├── game_logic.py     # Handles game rules and logic
├── database_fun.py   # Handles SQLite database operations
├── game_records.db   # SQLite database (auto-created)
```

---

## 🛠 Requirements

### ✅ Software Requirements

* Python 3.8 or higher
* Windows, Linux, or macOS
* Terminal / Command Prompt / PowerShell

### ✅ Python Libraries Used

All libraries are **built-in**, no installation needed:

* `sqlite3` → database storage
* `random` → number generation
* `time` → delays in gameplay

---

## ▶️ How to Run

1. Open a terminal in the project folder
2. Run the program:

```bash
python main.py
```

---

## 🎯 How the Game Works

### 1️⃣ User Selection

* Option 1: Log in with an existing username
* Option 2: Create a new username

> Usernames must be **unique** and are stored in the database.

### 2️⃣ Game Rules

* The computer generates **three random numbers**
* One number is secretly chosen as the **correct number**
* Player must guess the correct number
* Player can:

  * Guess a number
  * Type `help` to play Rock-Paper-Scissors for a clue
  * Type `e` to exit the game

### 3️⃣ Scoring System

* Correct guess = **1 point**
* Wrong guess = **0 points**
* The game runs **10 rounds**
* Final score is **saved to the database**

### 4️⃣ Help Feature (Rock-Paper-Scissors)

* Typing `help` triggers a **Rock-Paper-Scissors game**
* **Winning** gives a **range clue** for the correct number
* **Losing** gives no clue

### 5️⃣ Leaderboard

* Scores are updated in the database after the game
* Leaderboard displays:

  * **Rank**
  * **Username**
  * **Score** (highest first)

---

## 🧠 Code Explanation

### 📄 `database_fun.py`

Handles all database tasks:

* Creates `players` table if it doesn’t exist
* Adds new players
* Checks if a username exists
* Updates player scores
* Fetches leaderboard data

**Table Structure**:

| Column   | Type      |
| -------- | --------- |
| username | TEXT (PK) |
| score    | INTEGER   |

### 📄 `game_logic.py`

Handles all game mechanics:

* `generate_number()` → creates random numbers
* `logic_game()` → runs one game round

**Features:**

* Input validation
* Help system
* Win/lose logic
* Returns score for each round

### 📄 `main.py`

Main entry point:

* User login / registration
* Runs the game loop (10 rounds)
* Updates scores
* Displays results and leaderboard

---

## 🧪 Example Output

```
Do you have a username?  
Select 1 if you do, 2 if you do not  
Enter your answer: 2

Create a username: blair

Choose one number (12 or 45 or 78), or press e to exit:
```

---

## 🚀 Possible Improvements

* Add **password authentication**
* Save **game history**
* Add **difficulty levels**
* Create a **GUI version**
* Convert to an **EXE using PyInstaller**

---

## 👨‍💻 Author Notes

This project demonstrates:

* Python **modular programming**
* **Database integration**
* Game logic design
* Input validation
* Basic software architecture

> Suitable for **beginners to intermediate Python learners**.

