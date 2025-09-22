import cv2
from pyzbar.pyzbar import decode
import qrcode

def main():
    choice = input("Enter 'g' to create a QR code or 'd' to scan an existing QR code: ")

    if choice == "g":
        data = input("Enter the data you want to encode: ")
        filename = input("Enter the filename to save the QR code: ")
        generate_qr_code(data, filename)
    elif choice == "d":
        filename = input("Enter the filename of the QR code to decode: ")
        decoded_text = decode_qr_code(filename)
        if decoded_text is not None:
            print(f"Decoded text: {decoded_text}")
        else:
            print("QR code decoding failed.")
    else:
        print("Invalid choice. Please enter 'generate' or 'decode'.")

def generate_qr_code(data, filename):
    """Generate a QR code with the given data and save it to a file."""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")
    
def decode_qr_code(image_path):
    """Decode QR code from an image and return the extracted text."""
    image = cv2.imread(image_path)
    decoded_objects = decode(image)

    if decoded_objects:
        for obj in decoded_objects:
            return obj.data.decode('utf-8')  # Return the decoded text
    else:
        return None  # Indicate failure by returning None



if __name__ == "__main__":
    main()
