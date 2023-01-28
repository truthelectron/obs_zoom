import psutil
import pyautogui
import subprocess

# Check if Zoom app is running
while True:
    if "Zoom.exe" in (p.name() for p in psutil.process_iter()):
        # Zoom app is running
        # Launch OBS and start recording
        subprocess.Popen('obs.exe')
        pyautogui.press('ctrl', 'alt', 'r')
        break
    # If the zoom app is closed, stop the recording
    else:
        pyautogui.press('ctrl', 'alt', 's')
     
