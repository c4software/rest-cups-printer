import cups
import threading

from PIL import Image
from tempfile import mktemp
from time import sleep
from os import unlink


def set_printer_user():
    cups.setUser('rest-cups-printer')


def get_printer_status(printer_name):
    conn = cups.Connection()
    printers = conn.getPrinters()
    set_printer_user()
    if printer_name in printers:
        printer = printers[printer_name].copy()
        printer["status"] = 0
        return printer
    else:
        return {"status": 1, "reason": "Printer '{}' not found".format(printer_name)}


def print_image(printer_name, file_stream, height=600, width=900, media_size=None):
    conn = cups.Connection()
    printers = conn.getPrinters()
    set_printer_user()

    if printer_name in printers:
        im = Image.open(file_stream).resize((height, width))

        output = mktemp(prefix='jpg')
        im.save(output, format='jpeg')

        job_parameters = {}
        if media_size:
            # MediaSize DNP => w288h432 (10x15) w432h576 (20x15)
            job_parameters["media"] = media_size

        job_id = conn.printFile(printer_name, output, "HappyBorne Job", job_parameters)
        wait_for_cleanup_job(job_id, output)

        return {"status": 0}
    else:
        return {"status": 1, "reason": "Printer '{}' not found".format(printer_name)}


def cancel_all_jobs(printer_name):
    conn = cups.Connection()
    printers = conn.getPrinters()
    set_printer_user()

    if printer_name in printers:
        conn.cancelAllJobs(printer_name)
        return {"status": 0}
    else:
        return {"status": 1, "reason": "Printer '{}' not found".format(printer_name)}


def wait_for_cleanup_job(job_id, output):
    unlink(output)
