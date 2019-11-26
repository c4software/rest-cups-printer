import subprocess
from flask import send_file


def take_shot():
    return subprocess.check_output("gphoto2 --force-overwrite --quiet --capture-image-and-download --stdout", shell=True)

def take_capture():
    return subprocess.check_output("gphoto2 --force-overwrite --quiet --trigger-capture --stdout", shell=True)

def quick_shot():
    return subprocess.check_output("gphoto2 --capture-movie --frames=1 --stdout", shell=True)

def get_summary():
    data = subprocess.check_output("gphoto2 --summary", shell=True)
    if not data:
        raise Exception('No device found')
    else:
        return data