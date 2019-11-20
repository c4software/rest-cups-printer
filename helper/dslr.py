import subprocess
from flask import send_file


def take_shot():
    try:
        subprocess.check_output("gphoto2 --force-overwrite --quiet --capture-image-and-download --filename /tmp/photobooth.jpg", shell=True)
        return send_file("/tmp/photobooth.jpg")
    except:
        return ""

def get_summary():
    try:
        return subprocess.check_output("gphoto2 --summary", shell=True)
    except:
        return ""