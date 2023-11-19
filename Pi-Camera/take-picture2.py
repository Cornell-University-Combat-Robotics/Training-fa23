import picamera
import time

# Create an instance of the PiCamera
camera = picamera.PiCamera()

try:
    # Set up the camera settings (optional, can be customized)
    camera.resolution = (1024, 768)
    camera.start_preview()

    # Camera warm-up time
    time.sleep(2)

    # Capture and save an image
    camera.capture('/home/pi/Desktop/image.jpg')
    print("Image captured and saved.")

finally:
    # Ensure the camera is safely closed
    camera.close()
