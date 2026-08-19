# 🎲 Dice Roll Game

A simple command-line dice game. The player and the computer take turns rolling a die, and whoever rolls higher wins that round. The first to reach the target score wins the game.

## Features
- Player sets the winning score
- Each round rolls a random number from 1 to 6
- Tie rounds are handled
- Quit anytime by typing `q`
- Input validation for both the score and the menu choice

## Requirements
- Python 3.x (standard library only)

## How to Run
python3 dice_roll.py

## Usage
1. Enter the score that ends the game (e.g. `5`).
2. Each round: press Enter to roll, or type `q` to quit.
3. Whoever rolls higher wins the round.
4. First to reach the target score wins.

## Fixes Made
The original code had indentation errors in the `try`, `if`, and `while` blocks (Python raises `IndentationError` at runtime for these). Fixed all block indentation, and cleaned the `secim` input with `.strip().lower()`.