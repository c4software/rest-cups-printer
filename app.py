import logging
from flask import Flask
from flask import request

from helper.printer import print_image

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/print/photo/<printer>/<height>/<width>', methods=["POST"])
def print_photo(printer, height, width):
    print(request.files)
    if 'file' in request.files:
        f = request.files['file']
        return print_image(printer, f.stream, int(height), int(width))
    else:
        return "{'error': 'Please provide a valid jpeg file (multipart/form-data).'}"

