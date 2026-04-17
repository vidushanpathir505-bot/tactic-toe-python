# ❌⭕ Tic-Tac-Toe — CLI & GUI

This repository contains two versions of Tic-Tac-Toe built with Python, showing the evolution from a simple command-line script to a fully structured GUI application.

---

## 📁 Repository Structure

```
tic-tac-toe/
├── cli/                        # Version 1 — Command Line
│   └── tictactoe.py
│
└── gui/                        # Version 2 — GUI + OOP
    ├── main.py
    ├── gui.py
    ├── game.py
    ├── player.py
    └── bot.py
```

---

## 🖥️ Version 1 — Command Line

A lightweight CLI game playable directly in the terminal. The board is numbered 1–9 and players enter a position each turn.

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

### Features
- 🎯 Player vs Player and Player vs Bot modes
- ✅ Input validation — handles non-numeric and out-of-range entries
- 🚫 Occupied position detection
- 🔄 Board resets automatically after each round
- 🏆 Automatic win and draw detection

### How to Run
```bash
cd tic-tac-toe
python tictactoe.py
```

**Requirements:** Python 3.10+ *(no external dependencies)*

---

## 🎮 Version 2 — GUI + OOP

A fully rebuilt version using Tkinter for a graphical interface and Object-Oriented Programming for a clean, modular codebase.

### Features
- 🎯 Player vs Player and Player vs Bot modes
- 🧠 Smart game logic with win/draw detection
- 🖱️ Interactive clickable board (Tkinter)
- 🔄 Restart button without closing the app
- 💡 Clean OOP architecture across multiple modules

### How to Run
```bash
cd tic-tac-toe-v2
python main.py
```

**Requirements:** Python 3.x · Tkinter *(included with Python)*

---

## 🔀 Version Comparison

| Feature | CLI | GUI |
|---|---|---|
| Interface | Terminal | Tkinter window |
| Architecture | Procedural | OOP |
| Player vs Player | ✅ | ✅ |
| Player vs Bot | ✅ | ✅ |
| Input validation | ✅ | ✅ (click-based) |
| Restart | ✅ | ✅ |
| Visual feedback | ❌ | ✅ |

---

## 💡 Future Improvements

- 🎨 Highlight the winning line on the board
- 🧠 Smarter AI using the Minimax algorithm
- 👤 Player name input on the start screen
- 💾 Score tracking across rounds

---

## 👨‍💻 Author

**Vidushan Pathirana**

⭐ If you like this project, give it a star!
