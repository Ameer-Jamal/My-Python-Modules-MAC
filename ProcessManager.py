import subprocess
import os


class ProcessManager:
    def __init__(self):
        pass

    # Kills all processes that are listening on the specified port.
    def kill_port(self, port):
        # Get the list of processes that are listening on the specified port.
        processes = f"sudo lsof -t -i tcp:{port} | xargs kill -9"
        if processes:
            for process in processes:
                try:
                    # Run the command to kill the process
                    subprocess.run(processes, shell=True)
                except subprocess.CalledProcessError:
                    print("You do not have permission to kill the process {}.".format(process))
        else:
            print("No processes are listening on port {}.".format(port))

    # Method for killing a process with a certain PID
    def kill_process(self, pid):
        if pid is None:
            raise ValueError("No process ID")
        try:
            # Run the command to kill the process
            subprocess.run(f"sudo kill -TERM {pid}", shell=True)
        except subprocess.CalledProcessError as e:
            print(e.output)
            raise e

    # Method for getting the PID of a certain process
    def get_process_identifier_from_name(self, process_name):
        output = subprocess.check_output(["jps", "-l"])
        pid = None
        for line in output.decode("utf-8").splitlines():
            if f"{process_name}" in line:
                pid = line.split()[0]
        return pid

    # Method for killing a process by its name
    def kill_process_by_name(self, process_name):
        PID = self.get_process_identifier_from_name(process_name)
        if PID is not None:
            try:
                self.kill_process(PID)
                print(f"Process with PID:{PID} killed successfully.")
            except Exception as e:
                print(e)
        else:
            print(f"No process found with name: {process_name}")
