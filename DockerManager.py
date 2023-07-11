import subprocess
import docker
import os

class DockerManager:
    def __init__(self):
        # Ensure Docker is running if not then RUN docker
        self.ensure_docker_running()
        # Create a Docker client
        self.client = docker.from_env()

    # Method for ensuring Docker is running
    def ensure_docker_running(self):
        try:
            # Try to get Docker info
            subprocess.check_output("docker info".split())
        except subprocess.CalledProcessError:
            # If Docker is not running, start Docker minmized
            print("Docker is not running. Starting Docker...")
            os.system("osascript -e 'tell application \"Docker\" to activate' -e 'tell application \"System Events\" to click (first button of (every window of (application process \"Docker\")) whose role description is \"minimize button\")'")
            print("Waiting for Docker to start...")
            while True:
                try:
                    # Try to get Docker info until Docker starts
                    subprocess.check_output("docker info".split())
                    break
                except subprocess.CalledProcessError:
                    continue
            print("Docker started successfully.")

    # Method for starting a Docker container
    def start_container(self, container_name):
        # Get the container
        container = self.client.containers.get(container_name)
        # If the container does not exist, raise an error
        if container is None:
            raise FileNotFoundError(f"Container: '{container_name}' does not exist")
        # Start the container
        container.start()
        print(f"{container_name} docker container started")

    # Method for stopping a Docker container
    def stop_container(self, container_name):
        # Get the container
        container = self.client.containers.get(container_name)
        # If the container does not exist, raise an error
        if container is None:
            raise FileNotFoundError(f"Container '{container_name}' does not exist")
        # Stop the container
        container.stop()
        print(f"{container_name} docker container stopped")


    # Method for starting a Docker container
    def start_container(self, container_name):
        # Get the container
        container = self.client.containers.get(container_name)
        # If the container does not exist, raise an error
        if container is None:
            raise FileNotFoundError(f"Container '{container_name}' does not exist")
        # Start the container
        container.start()
        print(f"{container_name} docker container started")
