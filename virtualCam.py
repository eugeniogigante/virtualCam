import cv2
import pygetwindow as gw
import pyautogui
import numpy as np
import pyvirtualcam


# DroidCam IP and port
droidcam_ip = "10.58.8.20"  # Replace with your DroidCam IP address
droidcam_port = 4747

# DroidCam video feed URL
video_url = f"http://{droidcam_ip}:{droidcam_port}/video"

# Create VideoCapture object
cap = cv2.VideoCapture(video_url)

#cap = cv2.VideoCapture(0)
# Function to capture screen content
def capture_screen(cap=cap):
    success, frame = cap.read()
    frame = cv2.resize(frame,(1280,720))
    return frame

# Main function to create a virtual camera
def main():
    # Set the window title of the application you want to share
    window_title = "Your Application Window Title"

    # Create a virtual camera
    with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
        print(f"Virtual camera '{cam.device}' created. Press 'Ctrl+C' to exit.")

        while True:
            # Capture screen content
            frame = capture_screen(cap)

            # If the window is found, send the frame to the virtual camera
            if frame is not None:
                cam.send(frame)

            # Uncomment the following line if you want to display the captured frame locally
            # cv2.imshow("Virtual Camera Output", frame)

            # Break the loop on 'Ctrl+C'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Clean up OpenCV
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
