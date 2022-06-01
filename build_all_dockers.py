import pathlib
from re import sub
import os
import subprocess

if __name__ == '__main__':
    print('🐳 Building Docker images')
    print("✋ Stopping all containers...")
    subprocess.run('docker stop $(docker ps -aq)', shell=True)

    path = pathlib.Path('.')

    files = path.glob("Dockerfile.*")

    for file in files:
        print(f"I found: {file}")
        file_name = file.name
        _, ver = file_name.split('.')

        java_image_name = f"java-{ver}-test"

        print(f"🚮 Deleting image for {java_image_name} ")
        subprocess.run(f'docker image rm {java_image_name}', shell=True)

        print(f"👷‍♂️ Building image for {java_image_name}")
        subprocess.run(f'docker build -f {file_name} . -t {java_image_name}', shell=True)
