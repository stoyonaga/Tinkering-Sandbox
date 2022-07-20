import os 

"""
A simpler youtube-dl interface that works between Windows and WSL2 

Requirements:
1) WSL2: Windows Powershell > wsl --install
   (After installation, run Powershell > wsl -l -v to ensure that you're running on Version 2)
   (Version 2 will require that your CPU supports Virtualization capabilities! For more details, consult the documentation at https://docs.microsoft.com/en-us/windows/wsl/)
   (Do note that after installing wsl, additional setup will be required. You will have to first run: 
   a) sudo apt update
   b) sudo apt install build-essential
2) You need to modify the host_directory variable in order for the program to work sufficiently. 
3) Dependencies: youtube-dl, ffmpeg
4) Others: Python 3 Source // Interpreter 

Note:
Before using the following program, you are adhering and agreeing to the following dependencies:
1) This tool is strictly for education purposes.
2) By using this tool, the developer of this interfacing script is not held responsible for any implications 
"""

# Illustration: /mnt/c/Users/MrRogers/Desktop
host_directory = "YOUR PATH GOES HERE"

print("========== Welcome to my simplified Youtube-DL Interface ==========")
print("Please select an action: ")
print("1) Install Environment and Dependencies")
print("2) Download Playlist (mp3) with Thumbnails")
print("3) Uninstall")

try:
    controller = int(input(">"))

    if controller == 1:
        if os.path.isdir("{}/youtube-dl_simplified".format(host_directory)):
            print("\nThe environment has already been set up!")
        else:
            print("Updating Ubuntu.....")
            os.system("sudo apt-get upgrade")
            print("\nThe environment has not been set up.")
            print("Generating Music Files Environment...")
            os.system("mkdir Music_Cache")
            os.system("cd {} && mkdir youtube-dl_simplified".format(host_directory))
            print("\nInstalling the youtube-dl dependencies...")
            os.system("sudo apt install ffmpeg")
            os.system("sudo apt install python3-pip")
            os.system("sudo pip3 install youtube-dl")
            os.system("hash youtube-dl")
    elif controller == 2:
        url = input("Enter a Youtube URL: \n")
        os.system("cd Music_Cache && youtube-dl --extract-audio --audio-format mp3 --embed-thumbnail -i -o \"%(title)s.%(ext)s\" {}".format(url))
        os.system("cd Music_Cache && mv *.mp3 {}/youtube-dl_simplified".format(host_directory))
    elif controller == 3:
        print("\n The environment is being uninstalled...")
        os.system("rmdir Music_Cache")
        os.system("sudo pip uninstall youtube-dl")
        os.system("sudo apt remove ffmpeg")
        os.system("cd {} && rmdir youtube-dl_simplified".format(host_directory))
    quit(0)

except ValueError:
    raise Exception("Error: An incorrect control sequence has been provided. Try again")
