# obs_zoom
launch obs recording automatically when zoom is launched
OBS Automation Script
This script is designed to automatically launch OBS and start recording when the Zoom app is opened. It uses the psutil and pyautogui libraries to check for the presence of the Zoom app and control OBS.

##Installation
To run this script, you will need to have Python 3 and the following libraries installed:

psutil
pyautogui
You can install these libraries using pip:

```python
pip install psutil
pip install pyautogui
```
##Usage
Make sure that OBS is installed on your system.
Open a command prompt or terminal and navigate to the directory where the script is located.
Run the script with the command python obs-automation.py
When you open the Zoom app, OBS will automatically launch and start recording.
Note: You may need to specify the path of the OBS executable in the subprocess.Popen() function if the script is unable to find it.

##Troubleshooting
If you get ModuleNotFoundError for pyautogui library.It means the library is not installed.You can install it by running pip install pyautogui
If you get attributeError for 'getWindows' .It means the version of pyautogui is not supported with this function, you can try updating the version of pyautogui

##Contributing
Fork it (https://github.com/yourusername/obs-automation/fork)
Create your feature branch (git checkout -b feature/fooBar)
Commit your changes (git commit -am 'Add some fooBar')
Push to the branch (git push origin feature/fooBar)
Create a new Pull Request

##License
This project is licensed under the MIT License - see the LICENSE.md file for details.

##Acknowledgments
Inspiration for this script came from the need for an easy way to automate the process of starting recordings during Zoom meetings.
The psutil and pyautogui libraries were used to make the task of checking for running processes and controlling OBS much easier.
