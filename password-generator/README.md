# Password Generator

A customizable password generator built with Python. Users can choose which character types to include (uppercase letters, lowercase letters, digits, special characters) and specify the desired password length.

## Features

- Choose from four character types: uppercase, lowercase, digits, special characters
- Guarantees at least one character from each selected type
- Validates that password length is sufficient for the selected character types
- Warns if no character type is selected
- Shuffles the final password so guaranteed characters aren't predictably placed
- Option to generate multiple passwords in one session

## How It Works

1. Enter the desired password length (minimum 4 characters)
2. Select which character types to include (comma-separated, e.g. `1,2,3`)
3. The generator builds a character pool from your selections
4. One character from each selected type is guaranteed to appear
5. The remaining length is filled with random characters from the pool
6. All characters are shuffled together to form the final password

## Example