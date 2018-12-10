import cups
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
        printer = printers[printer_name]
        print (printer)
    else:
        return {"status": 1, "reason": "Printer '{}' not found".format(printer_name)}


def print_image(printer_name, file_stream, height=600, width=900):
    conn = cups.Connection()
    printers = conn.getPrinters()
    set_printer_user()

    if printer_name in printers:
        im = Image.open(file_stream).resize((height, width))

        output = mktemp(prefix='jpg')
        im.save(output, format='jpeg')

        print_id = conn.printFile(printer_name, output, "HappyBorne Job", {})
        while conn.getJobs().get(print_id, None):
            sleep(1)

        unlink(output)
        return {"status": 0}
    else:
        return {"status": 1, "reason": "Printer '{}' not found".format(printer_name)}
