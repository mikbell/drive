#!/usr/bin/env python3
"""
Terminal Snake Game
A classic Snake game implementation using Python and curses.

Controls:
- Arrow keys or WASD to move
- 'q' to quit
- 'r' to restart after game over

Author: AI Assistant
"""

import curses
import random
import time

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.setup_screen()
        self.init_game()
    
    def setup_screen(self):
        """Initialize the game screen"""
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(1)  # Non-blocking input
        self.stdscr.timeout(100)  # Refresh rate
        
        # Get screen dimensions
        self.height, self.width = self.stdscr.getmaxyx()
        
        # Create game window (leave space for borders and UI)
        self.game_height = self.height - 4
        self.game_width = self.width - 4
        self.win = curses.newwin(self.game_height, self.game_width, 2, 2)
        self.win.box()
        self.win.keypad(1)
        
    def init_game(self):
        """Initialize game state"""
        self.score = 0
        self.game_over = False
        
        # Snake starts in the middle, moving right
        start_y = self.game_height // 2
        start_x = self.game_width // 2
        self.snake = [(start_y, start_x), (start_y, start_x - 1), (start_y, start_x - 2)]
        
        # Initial direction (right)
        self.direction = (0, 1)
        
        # Place first food
        self.place_food()
    
    def place_food(self):
        """Place food at random location not occupied by snake"""
        while True:
            food_y = random.randint(1, self.game_height - 2)
            food_x = random.randint(1, self.game_width - 2)
            if (food_y, food_x) not in self.snake:
                self.food = (food_y, food_x)
                break
    
    def handle_input(self):
        """Handle user input for snake movement"""
        key = self.stdscr.getch()
        
        # Quit game
        if key == ord('q'):
            return False
        
        # Restart game
        if key == ord('r') and self.game_over:
            self.init_game()
            return True
        
        # Movement controls
        directions = {
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -1),
            curses.KEY_RIGHT: (0, 1),
            ord('w'): (-1, 0),
            ord('s'): (1, 0),
            ord('a'): (0, -1),
            ord('d'): (0, 1),
        }
        
        if key in directions:
            new_direction = directions[key]
            # Prevent snake from moving backwards into itself
            if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
                self.direction = new_direction
        
        return True
    
    def move_snake(self):
        """Move snake in current direction"""
        if self.game_over:
            return
        
        # Calculate new head position
        head_y, head_x = self.snake[0]
        new_head = (head_y + self.direction[0], head_x + self.direction[1])
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.game_height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.game_width - 1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food was eaten
        if new_head == self.food:
            self.score += 10
            self.place_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw(self):
        """Draw the game state"""
        self.stdscr.clear()
        
        # Draw title and score
        title = "🐍 SNAKE GAME 🐍"
        score_text = f"Score: {self.score}"
        
        self.stdscr.addstr(0, (self.width - len(title)) // 2, title)
        self.stdscr.addstr(1, 2, score_text)
        
        # Draw game border
        self.win.box()
        
        # Draw snake
        for i, (y, x) in enumerate(self.snake):
            if i == 0:  # Head
                self.win.addstr(y, x, '@')
            else:  # Body
                self.win.addstr(y, x, '*')
        
        # Draw food
        food_y, food_x = self.food
        self.win.addstr(food_y, food_x, '#')
        
        # Draw game over message
        if self.game_over:
            game_over_text = "GAME OVER! Press 'r' to restart or 'q' to quit"
            msg_y = self.height - 2
            msg_x = (self.width - len(game_over_text)) // 2
            self.stdscr.addstr(msg_y, msg_x, game_over_text)
        else:
            # Draw controls
            controls = "Controls: Arrow Keys/WASD to move, 'q' to quit"
            msg_y = self.height - 2
            msg_x = (self.width - len(controls)) // 2
            self.stdscr.addstr(msg_y, msg_x, controls)
        
        # Refresh screens
        self.win.refresh()
        self.stdscr.refresh()
    
    def run(self):
        """Main game loop"""
        while True:
            if not self.handle_input():
                break
            
            self.move_snake()
            self.draw()
            
            # Small delay for smoother animation
            time.sleep(0.05)

def main(stdscr):
    """Main function to initialize and run the game"""
    # Initialize colors if terminal supports it
    if curses.has_colors():
        curses.start_color()
    
    game = SnakeGame(stdscr)
    game.run()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure your terminal is large enough to run the game!")
