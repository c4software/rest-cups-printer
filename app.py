import logging
from flask import Flask, jsonify
from flask import request
from waitress import serve

from helper.printer import print_image, get_printer_status

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/print/photo/<printer>/<height>/<width>', methods=["POST"])
@app.route("/print/photo/<printer>/<height>/<width>/<media_size>", methods=["POST"])
def print_photo(printer, height, width, media_size=None):
    if 'file' in request.files:
        f = request.files['file']
        return jsonify(print_image(printer, f.stream, int(height), int(width), media_size))
    else:
        return jsonify({"status": 1, "reason": 'Please provide a valid jpeg file (multipart/form-data).'})


@app.route("/status/<printer>")
def status(printer):
    return jsonify(get_printer_status(printer))


if __name__ == "__main__":
    serve(app, listen='*:8888')
