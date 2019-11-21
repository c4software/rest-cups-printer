import subprocess
from flask import send_file


def take_shot():
    subprocess.check_output("gphoto2 --force-overwrite --quiet --capture-image-and-download --filename /tmp/photobooth.jpg", shell=True)
    return send_file("/tmp/photobooth.jpg")

def take_capture():
    subprocess.check_output("gphoto2 --force-overwrite --quiet --trigger-capture --filename /tmp/photobooth.jpg", shell=True)
    return send_file("/tmp/photobooth.jpg")

def get_summary():
    data = subprocess.check_output("gphoto2 --summary", shell=True)
    if not data:
        raise Exception('No device found')
    else:
        return data