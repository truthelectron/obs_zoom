# obs_zoom
launch obs recording automatically when zoom is launched
OBS Automation Script
This script is designed to automatically launch OBS and start recording when the Zoom app is opened. It uses the psutil and pyautogui libraries to check for the presence of the Zoom app and control OBS.

## Installation
To run this script, you will need to have Python 3 and the following libraries installed:

psutil
pyautogui
You can install these libraries using pip:

```python
pip install psutil
pip install pyautogui
```
## Usage
Make sure that OBS is installed on your system.
Open a command prompt or terminal and navigate to the directory where the script is located.
Run the script with the command python obs-automation.py
When you open the Zoom app, OBS will automatically launch and start recording.
Note: You may need to specify the path of the OBS executable in the subprocess.Popen() function if the script is unable to find it.

## To automate the script in Windows, you can use the Task Scheduler to schedule the script to run automatically at a specific time or upon certain events.

1. Open the Task Scheduler by searching for it in the Start menu or by running "taskschd.msc" in the Command Prompt.

2. In the Task Scheduler, click on "Create Basic Task" in the Actions pane on the right side of the window.

3. Give the task a name and description, then click Next.

4. Choose when you want the task to start. For example, you can choose "When I log on" or "At a specific time" and then specify the time.

5. Select "Start a program" as the action to be taken.

6. In the Program/script field, enter the path of the script you want to run.

7. Click Next, then Finish to create the task.

8. You can also go to the Task Scheduler Library and check the task properties and triggers.

9. To make sure that the task runs with the highest privilege, go to the "Actions" tab and then click on "Edit" and check the "Run with highest privileges"

10. Task Scheduler will now automatically run the script at the specified time or event.

## Troubleshooting
If you get ModuleNotFoundError for pyautogui library.It means the library is not installed.You can install it by running pip install pyautogui
If you get attributeError for 'getWindows' .It means the version of pyautogui is not supported with this function, you can try updating the version of pyautogui

## Contributing
Fork it (https://github.com/yourusername/obs-automation/fork)
Create your feature branch (git checkout -b feature/fooBar)
Commit your changes (git commit -am 'Add some fooBar')
Push to the branch (git push origin feature/fooBar)
Create a new Pull Request

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Inspiration for this script came from the need for an easy way to automate the process of starting recordings during Zoom meetings.
The psutil and pyautogui libraries were used to make the task of checking for running processes and controlling OBS much easier.
