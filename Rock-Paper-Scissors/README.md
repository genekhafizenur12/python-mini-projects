# Rock-Paper-Scissors

A simple terminal-based Rock-Paper-Scissors game. Play against the computer — first to reach the target score wins.

## Requirements

- Python 3.x

## Runs

```bash
python3 Rock-Paper-Scissors.py
```

## How to Play

1. Enter the winning score when the game starts.
2. Press Enter to continue each round, or type `q` to quit.
3. Type your choice: Taş (Rock), Kağıt (Paper), or Makas (Scissors).
4. The computer picks randomly, the winner is decided, and the score updates.
5. The game ends automatically once a score reaches the winning score.

## Code Structure

- `get_winning_score()` — gets a valid winning score from the user
- `get_player_choice(secenekler)` — gets a valid player choice
- `winner(...)` — decides the round's winner and updates scores
- `score_yazdir(...)` — prints the round result and current scores