import cv2
from PIL import Image
import barcode
from barcode import EAN13
from barcode.writer import ImageWriter   
from pyzbar.pyzbar import decode

def generate_barcode(data, filename):
    """Generate a barcode with the given data and save it to a file."""
    barcode = EAN13(data, writer=ImageWriter())
    barcode.save(filename)
    print(f"Barcode generated and saved as {filename}")



def read_barcode(image_path):
    """Read barcode from an image and return the extracted text."""
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Decode the barcode using pyzbar
    decoded_objects = decode(image)

    if decoded_objects:
        # Return the first decoded object (assuming there's only one barcode in the image)
        return decoded_objects[0].data.decode('utf-8')
    else:
        print("No barcode detected.")
        return None

def main():
    choice = input("Enter 'g' to create a barcode or 'r' to read a barcode: ")

    if choice == "g":
        data = input("Enter the data you want to encode: ")
        filename = input("Enter the filename to save the barcode: ")
        generate_barcode(data, filename)
    elif choice == "r":
        filename = input("Enter the filename of the image containing the barcode: ")
        barcode_data = read_barcode(filename)
        if barcode_data is not None:
            print(f"Barcode data: {barcode_data}")
        else:
            print("Barcode reading failed.")
    else:
        print("Invalid choice. Please enter 'g' or 'r'.")

if __name__ == "__main__":
    main()

