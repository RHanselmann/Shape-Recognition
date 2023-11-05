# Shape-Recognition
This program can recognise diffrent shapes and its colors.

# Cam or Image mode
In the Variables you can choose either the Camera or the Image mode.
Image mode:     Normal mode. It reads an already existing image for the program.
                Edit the path variable to your desired images path!
Camera mode:    Shows the live image of your camera. As soon as you close the 
                live image window, the last frame gets saved and used for the program.
                Edit the DEVICE_ID variable if you cant open your desired Camera!

# CSV File
The recived datas get saved to the log.csv file.
Following data get collected for each recognised shape:
    - Time when the shape got recognised.
    - The specific shape.
    - The color of the shape.

# How to use poetry
Use poetry in your Project: "poetry init -n"
How to add Packages (Example with numpy): "poetry add numpy"
See installed Packages: "poetry show"
Use diffrent python version: "poetry env use C:\path\to\your\python.exe"

# cmd commands
Open path: "cmd.exe /K "cd /d D:\your\path""
See all installed Pythons: "py -0p"