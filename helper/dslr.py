import subprocess

def take_shot():
    try:
        return subprocess.check_output("gphoto2 --stdout", shell=True)
    except:
        return ""