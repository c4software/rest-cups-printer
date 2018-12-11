
## Run

```bash
FLASK_ENV=development flask run
```

## Installation Systemd

```bash
sudo cp rest-cups-print.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rest-cups-print
sudo systemctl start rest-cups-print
```

## Format DNP

MediaSize (Can be specified in URL during print)

- w288h432 (10x15) 
- w432h576 (20x15)

## Test

```bash
curl -X POST \
  http://localhost:5000/print/photo/MyPrinterName/300/300 \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=./sample.jpeg
```