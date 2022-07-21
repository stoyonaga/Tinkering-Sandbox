from tkinter import *
import pyautogui


def update_position() -> None:
    x = pyautogui.position().x
    y = pyautogui.position().y
    position.config(text="Mouse Position: (x, y) = ({}, {})".format(x, y))


try:
    root = Tk()
    root.title("Mouse Tracker")
    root.resizable(False, False)
    root.wm_overrideredirect(True)
    root.wm_minsize(285, 85)

    compact_label = Label(root, text="pyautogui Mouse Tracker")
    compact_label.pack()

    position = Label(root, text="")
    position.pack()

    while True:
        update_position()
        root.update()

except KeyboardInterrupt:
    print("Keyboard script has been disabled.")
    exit()
