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

  # Methods for running modifier_plus key
    def run_modifier_plus(self, modifier, arg):
        with self.keyboard.pressed(modifier):
            self.keyboard.press(arg)
            self.keyboard.release(arg)

    def ctrl_plus(self, arg):
        self.run_modifier_plus(Key.ctrl, arg)

    def shift_plus(self, arg):
        self.run_modifier_plus(Key.shift, arg)

    def alt_plus(self, arg):
        self.run_modifier_plus(Key.alt, arg)

    def cmd_plus(self, arg):
        self.run_modifier_plus(Key.cmd, arg)
