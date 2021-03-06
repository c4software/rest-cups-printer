import subprocess
from PIL import Image
import io
from flask import send_file



def take_shot():
    return crop_image(subprocess.check_output("gphoto2 --force-overwrite --quiet --capture-image-and-download --stdout", shell=True))

def take_capture():
    return crop_image(subprocess.check_output("gphoto2 --force-overwrite --quiet --trigger-capture --stdout", shell=True))

def quick_shot():
    return crop_image(subprocess.check_output("gphoto2 --capture-movie --frames=1 --stdout", shell=True))

def get_summary():
    try:
        data = subprocess.check_output("gphoto2 --summary 2> /dev/null", shell=True)
        if not data:
            return None
        else:
            return data
    except:
        return None

def crop_image(image):
    image  = Image.open(io.BytesIO(image))
    width  = image.size[0]
    height = image.size[1]

    if 'exif' in image.info:
        exif = image.info['exif']
    else:
        exif = None

    aspect = width / float(height)

    ideal_width = 1280
    ideal_height = 960

    ideal_aspect = ideal_width / float(ideal_height)

    if aspect > ideal_aspect:
        # Then crop the left and right edges:
        new_width = int(ideal_aspect * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
    else:
        # ... crop the top and bottom:
        new_height = int(width / ideal_aspect)
        offset = (height - new_height) / 2
        resize = (0, offset, width, height - offset)

    resized = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)
    output = io.BytesIO()
    resized.save(output, 'JPEG', quality=100, exif=exif)
    output.seek(0)
    return send_file(output, mimetype="image/jpeg")