import subprocess
import time
import pyautogui

class IntelliJManager:
    def __init__(self, input_manager):
        self.input_manager = input_manager

    # Method for checking if the frontmost window is IntelliJ
    def is_window_intellij_idea(self):
        try:
            output = subprocess.check_output(["app-frontmost", "--bundleid"]).decode("utf-8").strip()
            print(output)
            time.sleep(0.1)
            return output == "com.jetbrains.intellij"
        except subprocess.CalledProcessError:
            return False

    # Method for opening IntelliJ with a certain project
    def open_intellij_with_project(self, project_name):
        path_to_intellij = "/Applications/IntelliJ IDEA.app"
        path_to_project = f"{project_name}"
        subprocess.run(["open", "-a", path_to_intellij, path_to_project])
        while not self.is_window_intellij_idea():
            time.sleep(0.5)
        return True

    # Method for running a debug configuration in IntelliJ
    def run_intellij_debug_config(self, project_name):
        if self.open_intellij_with_project(project_name):
            time.sleep(6)
            self.input_manager.move_mouse_to_middle_of_screen()
            pyautogui.click()
            self.input_manager.ctrl_plus('d')

# Class for running commands
