######## Face Tracking (Webcam/Video) using OpenCV #########

# Author: George
# Youtube Channel : https://www.youtube.com/channel/UC-j647KCqjQKE50Npx9TZsg

# Description: 
# This code uses OpenCV to do Face Tracking on Webcam/Video.

# Importing OpenCV.

import cv2

# Defining webcam.

cap = cv2.VideoCapture(0)

# Path to Cascade Classifier.

cascade = cv2.CascadeClassifier('/home/pi/george/coding_place/python/projects/face_tracking/haarcascade_frontalface_default.xml')

# height and width.

height = 400
width = 500

# Infinite loop.

while True:
    
    # Reading a frame from the webcam.
    
    ret, frame = cap.read()
    
    # Converting BGR to GRAY.
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Getting the faces.

    faces = cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        
        # Drawing a rectangle around the face.
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        
    # Resizing the frame.  

    resize = cv2.resize(frame, (width, height))
    
    # Displaing the Img.

    cv2.imshow('Face Tracking', resize)
    
    # If Esc is pressed then exit out of the loop.

    if cv2.waitKey(1) == 27:
        break

# Releaseing the camara.

cap.release()

# Destroying all the windows.

cv2.destroyAllWindows()