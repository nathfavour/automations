import pyautogui
import pytesseract
from PIL import Image
import sys

# Specify the path to the Tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

def find_string_on_screen(search_string):
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Use pytesseract to convert the image to text
    text = pytesseract.image_to_string(screenshot)

    # Count the occurrences of the search string in the text
    count = text.count(search_string)

    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <search_string>")
        sys.exit(1)

    search_string = sys.argv[1]
    occurrences = find_string_on_screen(search_string)
    if occurrences > 0:
        print(f"The string '{search_string}' was found {occurrences} times on the screen.")
    else:
        print(f"The string '{search_string}' was not found on the screen.")