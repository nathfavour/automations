import sys
import pytesseract
import pyautogui
from PIL import Image

def find_and_click_string(search_string):
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Use pytesseract to extract text and bounding boxes
    text_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)
    text_list = text_data['text']
    
    # Iterate through detected text elements to find the search string
    for i, text in enumerate(text_list):
        if search_string in text:
            # Calculate the center of the bounding box
            x = text_data['left'][i] + text_data['width'][i] // 2
            y = text_data['top'][i] + text_data['height'][i] // 2
            
            # Move the mouse to the center of the bounding box and double-click
            pyautogui.moveTo(x, y)
            pyautogui.click(clicks=2)
            return True

    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_and_click.py 'string_to_find'")
        sys.exit(1)

    search_string = sys.argv[1]
    if not find_and_click_string(search_string):
        print(f"The string '{search_string}' was not found on the screen.")