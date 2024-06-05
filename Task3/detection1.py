# Face detection

# Importing modules
import os
import cv2

def detect(image_path, output_folder):
    """
    Detect faces in an image and save the output with rectangles around faces.

    :param image_path: Path to the input image file.
    :param output_folder: Folder to save the output image with detected faces.
    """
    # Load the pre-trained Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        aspect_ratio = w / h
        if 0.5 < aspect_ratio < 1.5:  # Checking for approximately square faces
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save the result in the output folder
    result_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(result_path, image)

    # Display the result
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to your testing images folder
    input_folder = r'C:\Users\ASUS\CODSoft\faces'
    # Output folder for saving the results
    output_folder = r'C:\Users\ASUS\CODSoft\output_faces'

    # Iterate through images in the input folder
    for image_file in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_file)

        # Perform face detection on each image and save the result
        detect(image_path, output_folder)
