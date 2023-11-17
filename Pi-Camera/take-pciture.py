import time
import picamera

def take_picture(output_path):
    with picamera.PiCamera() as camera:
        # Adjust camera settings if needed
        # camera.resolution = (width, height)
        # camera.rotation = degrees

        # Wait for the camera to warm up
        time.sleep(2)

        # Capture a picture
        camera.capture(output_path)
        print(f"Picture saved: {output_path}")

if __name__ == "__main__":
    # Set the output path for the picture
    output_path = "image.jpg"  # Change the file name or path if needed

    # Call the function to take a picture
    take_picture(output_path)