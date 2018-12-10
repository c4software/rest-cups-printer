import logging
from flask import Flask
from flask import request

from helper.printer import print_image, get_printer_status

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/print/photo/<printer>/<height>/<width>', methods=["POST"])
def print_photo(printer, height, width):
    if 'file' in request.files:
        f = request.files['file']
        return print_image(printer, f.stream, int(height), int(width))
    else:
        return {"status": 1, "reason": 'Please provide a valid jpeg file (multipart/form-data).'}


@app.route("/status/<printer>")
def status(printer):
    return get_printer_status(printer)
