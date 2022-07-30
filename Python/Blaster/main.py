import io
import keyboard
import time
import os


def blast(message: io.TextIOWrapper) -> None:
    for i in range(5, 0, -1):
        print("Program will begin in {} seconds...".format(i))
        time.sleep(1)
        # Line 12 may have to be adapted, depending on your OS. If you are running Linux, replace it with:
        # clear
        os.system("cls")
    for line in message.readlines():
        if keyboard.is_pressed("Escape"):
            print("Process has been terminated...")
            message.close()
            quit(0)
        keyboard.write(line)
        time.sleep(1)
    message.close()


print("========== Welcome to Blaster Version 1.0.0 ==========")
if not os.path.isfile("lyrics.txt"):
    # Line 25 may have to be adapted, depending on your OS. If you are running Linux, replace it with:
    # touch lyrics.txt
    os.system("echo.> lyrics.txt")
    raise Exception("Error: File input does not exist..")
else:
    boo_yeah = open("lyrics.txt", "r")
    print("Press and hold down the  Escape key to terminate the script")
    blast(boo_yeah)
    quit(0)
