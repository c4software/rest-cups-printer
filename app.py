import logging
import os

from flask import Flask, jsonify, request, Response
from waitress import serve

from helper.printer import print_image, get_printer_status, cancel_all_jobs
from helper.dslr import take_shot, get_summary, take_capture, quick_shot

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


@app.route("/clear/<printer>")
def cancel(printer):
    return jsonify(cancel_all_jobs(printer))

@app.route("/dslr/shot")
def dslr_shot():
    return take_shot()

@app.route("/dslr/capture")
def dslr_capture():
    return take_capture()

@app.route("/dslr/summary")
def dslr_summary():
    return jsonify(get_summary())

@app.route("/dslr/preview")
def dslr_preview():
    return Response(quick_shot(), mimetype='image/jpeg')

@app.route("/reboot/now")
def reboot():
    os.system("sudo reboot")
    return jsonify({"status": 1})


if __name__ == "__main__":
    serve(app, listen='*:8888')
