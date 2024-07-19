import pyautogui
import random
import time

def move_mouse_randomly(duration_seconds):
    end_time = time.time() + duration_seconds
    while time.time() < end_time:
        # Get the size of the primary monitor.
        screen_width, screen_height = pyautogui.size()
        
        # Generate a random position within the screen bounds.
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        
        # Move the mouse to the random position.
        pyautogui.moveTo(x, y, duration=0.1)
        
        # Wait a bit before moving again to make the movements noticeable.
        time.sleep(0.5)

# Example usage: Move the mouse randomly for 10 seconds.
move_mouse_randomly(10)