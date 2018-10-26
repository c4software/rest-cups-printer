
## Run

```bash
FLASK_ENV=development flask run
```

## Test

```bash
curl -X POST \
  http://localhost:5000/print/photo/MyPrinterName/300/300 \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=./sample.jpeg
```