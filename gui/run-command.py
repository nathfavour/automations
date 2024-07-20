import subprocess
import pyautogui
import time

# Open PowerShell
# subprocess.Popen('powershell')


subprocess.Popen(['start', 'powershell'], shell=True)


time.sleep(2)  # Wait for PowerShell to open

# Type the command in the PowerShell window
pyautogui.typewrite('gh api user', interval=0.1)
time.sleep(1)  # Wait a bit before pressing Enter

# Press Enter to execute the command
pyautogui.press('enter')