import pygetwindow as gw

def print_active_window_title():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            print(f"Active window title: {active_window.title}")
        else:
            print("No active window detected.")
    except Exception as e:
        print(f"An error occurred: {e}")

print_active_window_title()