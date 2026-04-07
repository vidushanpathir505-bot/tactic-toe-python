# ❌⭕ Tic-Tac-Toe

A command-line Tic-Tac-Toe game with two modes — play against a friend or challenge a bot.

## How It Works

The board is numbered 1–9, left to right, top to bottom. Players take turns entering a position to place their mark. The first to align three in a row (horizontal, vertical, or diagonal) wins. If all squares are filled with no winner, the game ends in a draw.

```
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

## Getting Started

**Requirements:** Python 3.10+ (no external dependencies)

```bash
python tictactoe.py
```

## Game Modes

| Mode | Description |
|------|-------------|
| 1 VS 1 | Two players take turns on the same machine |
| Game Bot | Play against a bot that makes random moves |
| Exit | Quit the game |

## Gameplay Example

```
1. 1 VS 1
2. Game BOT
3. Exit
__: 2

Enter your move (1-9): 5
X | _ | _
---------
_ | O | _
---------
_ | _ | _
```

## Features

- Two game modes — local multiplayer and bot
- Input validation — handles non-numeric and out-of-range entries
- Occupied position detection
- Automatic win and draw detection after every move
- Board resets automatically after each round

## Future Improvements

- **Refactor to OOP** — restructure the codebase using classes (e.g. `Board`, `Player`, `Bot`, `Game`) for better organisation and maintainability
- **GUI version** — rebuild the interface using Tkinter with clickable cells and visual feedback
