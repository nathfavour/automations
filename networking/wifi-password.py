import subprocess
import re

def get_current_wifi_password():
    try:
        # Get the currently connected SSID on Windows
        ssid_output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
        ssid_match = re.search(r'SSID\s*:\s*(.+)\r', ssid_output)
        if ssid_match:
            ssid = ssid_match.group(1)
            # Get the WiFi profile details, including the password
            key_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8')
            key_match = re.search(r'Key Content\s*:\s*(.+)\r', key_output)
            if key_match:
                password = key_match.group(1)
                print(f"SSID: {ssid}\nPassword: {password}")
            else:
                print("Password could not be retrieved.")
        else:
            print("No WiFi connected or SSID could not be retrieved.")
    except Exception as e:
        print(f"An error occurred: {e}")

get_current_wifi_password()















# from wifi_password import wifi_password

# def get_current_wifi_password():
#     try:
#         # Get the name (SSID) of the currently connected WiFi
#         ssid = wifi_password.connected_ssid()
#         if ssid:
#             # Get the password of the currently connected WiFi
#             password = wifi_password.get_password(ssid)
#             print(f"SSID: {ssid}\nPassword: {password}")
#         else:
#             print("No WiFi connected.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# get_current_wifi_password()