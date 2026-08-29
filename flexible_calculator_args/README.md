# Flexible Calculator (*args)

A simple command-line calculator built in Python to practice using `*args`
for functions that accept a variable number of arguments.

## Features

- Add, Subtract, Multiply, Divide — with any number of inputs
- Handles empty input, invalid numbers, and division by zero
- Runs in a loop until you choose to exit

## Usage

\`\`\`bash
python3 flexible_calculator_args.py
\`\`\`

Choose an operation from the menu, then enter numbers separated by spaces:

\`\`\`
Choose an operation: 1
Enter numbers separated by spaces: 1 2 3 4 5
Result: 15.0
\`\`\`

## Core Concept

\`\`\`python
def hesapla(islem, *args):
    ...
\`\`\`

`*args` collects any number of numbers into a tuple, so the function works
whether you pass 1 number or 20 — no need to change its definition.