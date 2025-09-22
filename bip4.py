import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
  # Read frame from webcam
  ret, frame = cap.read()
  if not ret:
    print("Error! Cannot capture frame")
    break

  # Convert frame to grayscale for barcode processing
  filename = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def read_barcode(image_path):
  image = cv2.imread(image_path)
  decoded_objects = decode(image)
  if decoded_objects:
    return decoded_objects[0].data.decode('utf-8')
  else:
    print("No barcode detected.")
    return None

class wow:
  def __init__(self, filename):
    self.filename = filename
    # Read barcode data within the class (assuming read_barcode is a global function)
    self.decoded_data = read_barcode(self.filename)
    if self.decoded_data[:3] == "729":
      self.israel = "It is an Israeli Product"
    else:
      self.israel = "It is Not an Israeli Product"

def main():
        w = wow(filename)
        print(w.israel)
        

if __name__ == "__main__":
    main()

