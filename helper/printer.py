import cups
from PIL import Image
from tempfile import mktemp
from time import sleep
from os import unlink


def print_image(printer_name, file_stream, height=600, width=900):
    conn = cups.Connection()
    printers = conn.getPrinters()
    cups.setUser('rest-cups-printer')

    print(printers.keys())

    if printer_name in printers:
        im = Image.open(file_stream).resize((height, width))

        output = mktemp(prefix='jpg')
        im.save(output, format='jpeg')

        print_id = conn.printFile(printer_name, output, "HappyBorne Job", {})
        while conn.getJobs().get(print_id, None):
            sleep(1)

        unlink(output)
        return "done"
    else:
        return "Printer '{}' not found".format(printer_name)
