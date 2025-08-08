# Terminal Snake Game 🐍

A classic Snake game implemented in Python using the curses library, designed to run in your terminal.

## How to Play

1. **Run the game:**
   ```bash
   python snake_game.py
   ```

2. **Controls:**
   - **Arrow Keys** or **WASD** - Move the snake
   - **'q'** - Quit the game
   - **'r'** - Restart the game (after game over)

3. **Objective:**
   - Control the snake (@) to eat food (#)
   - Each piece of food increases your score by 10 points
   - The snake grows longer each time it eats food
   - Avoid hitting the walls or the snake's own body

## Game Elements

- `@` - Snake head
- `*` - Snake body
- `#` - Food
- Score is displayed at the top

## Requirements

- Python 3.x
- `windows-curses` package (automatically installed)
- Terminal window large enough to display the game

## Features

- Smooth snake movement
- Collision detection (walls and self-collision)
- Score tracking
- Game over and restart functionality
- Responsive controls
- Clean terminal-based graphics

## Tips

- Make sure your terminal window is maximized for the best experience
- The snake cannot move backward into itself
- Try to plan your moves ahead to avoid getting trapped!

Enjoy the game! 🎮
