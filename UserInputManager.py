from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController
import pyautogui
class UserInputManager:
    def __init__(self):
        self.keyboard = Controller()

    # Method for moving the mouse to the middle of the screen
    def move_mouse_to_middle_of_screen(self):
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width / 2, screen_height / 2
        pyautogui.moveTo(center_x, center_y)

    # Method for simulating a Ctrl+Key press
    def ctrl_plus(self, arg):
        with self.keyboard.pressed(Key.ctrl):
            self.keyboard.press(arg)
            self.keyboard.release(arg)

# Class for managing IntelliJ
