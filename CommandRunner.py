import subprocess

class CommandRunner:
    def __init__(self):
        pass

    # Method for running a command
    def run_command(self, command):
        subprocess.run(command, shell=True)

    # Method for running a command in a certain directory
    def run_command_in_directory(self, command, directory):
        command_to_run = ['cd', directory] + command
        full_command = ' '.join(command_to_run)
        self.run_command(full_command)


    def run_command_in_directory_with_terminal(self, command, directory):
        # Define an AppleScript that opens a new Terminal window and runs the command
        applescript = f"""
        tell application "Terminal"
            activate
            do script "cd {directory} && {' '.join(command)}"
        end tell
        """

        # Run the AppleScript
        subprocess.run(['osascript', '-e', applescript])
