## QR and Barcode Utilities (bip1–bip4)

A small collection of Python scripts for generating and decoding QR codes and barcodes, plus simple product-origin checking based on EAN-13 prefixes.

### Scripts
- **bip1.py**: Create and decode QR codes (file-based).
- **bip2.py**: Create and read EAN-13 barcodes (file-based).
- **bip3.py**: Read a barcode from an image file and report whether it starts with prefix `729` (Israel) or not.
- **bip4.py**: Experimental webcam flow paired with the same `729`-prefix check. See notes below.

---

## Requirements

- Python 3.8+
- Packages:
  - `opencv-python`
  - `pyzbar`
  - `qrcode`
  - `Pillow`
  - `python-barcode`

Note about `pyzbar`: It depends on the ZBar library. On many systems you must install ZBar separately. On Windows, prebuilt wheels often bundle the DLL, but if you encounter "Unable to find zbar shared library" errors, install ZBar and ensure it is on your PATH.

### Install dependencies

PowerShell (Windows):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
pip install opencv-python pyzbar qrcode Pillow python-barcode
```

bash (macOS/Linux):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install opencv-python pyzbar qrcode Pillow python-barcode
```

If ZBar is required on your OS:
- macOS: `brew install zbar`
- Ubuntu/Debian: `sudo apt-get install libzbar0`
- Windows: If needed, install a ZBar build and add its DLL directory to PATH.

---

## Usage

All commands assume you are in the project directory and your virtual environment is active.

### bip1.py — QR codes
Generate a QR code image:
```powershell
python bip1.py
# Enter 'g' when prompted, then provide data and output filename (e.g., qr.png)
```

Decode a QR code image:
```powershell
python bip1.py
# Enter 'd' when prompted, then provide the image filename (e.g., qr.png)
```

Notes:
- Output is typically PNG; supply a filename like `my_qr.png`.

### bip2.py — EAN-13 barcodes
Generate an EAN-13 barcode image:
```powershell
python bip2.py
# Enter 'g' and provide 12 digits of data (the 13th checksum is auto-computed),
# then provide an output filename (without extension). The library will add the extension.
```

Read a barcode from an image file:
```powershell
python bip2.py
# Enter 'r' and provide the image filename containing the barcode
```

Important:
- EAN-13 requires exactly 12 input digits (the library computes the final checksum digit). Non-digit input or wrong length will fail.

### bip3.py — File-based "729" prefix check
Check if a product (by barcode image) starts with prefix `729`:
```powershell
python bip3.py
# Provide the path to an image containing a readable EAN-13 barcode
```

Output indicates whether the decoded barcode begins with `729` (interpreted here as Israeli product code).

### bip4.py — Experimental webcam + prefix check
`bip4.py` opens the default webcam and attempts to integrate with the same `729` prefix logic. As written, it does not yet pass the live frame correctly to the decoder (it sets a variable named `filename` to a grayscale frame but then calls a function that expects a file path). Treat this as a starting point if you want to implement live scanning.

Suggested direction to make it work:
- Replace file-based decoding with decoding directly on the captured frame (no `cv2.imread`), e.g., pass `frame` to `decode`.
- Overlay decoded text on the video frame and display via `cv2.imshow`.
- Exit cleanly on key press and `cap.release()` / `cv2.destroyAllWindows()`.

---

## Tips and Troubleshooting

- If decoding fails, ensure the image is in focus, well-lit, and the code occupies a reasonable portion of the frame.
- For EAN-13, ensure the barcode is not truncated and has quiet zones.
- If you hit `pyzbar`/ZBar errors, verify ZBar installation and that the shared library is discoverable.

---

