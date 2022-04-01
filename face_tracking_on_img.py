######## Face Tracking (Img) using OpenCV #########

# Author: George
# Youtube Channel : https://www.youtube.com/channel/UC-j647KCqjQKE50Npx9TZsg

# Description: 
# This code uses OpenCV to do Face Tracking on a Img.

# Importing OpenCV.

import cv2

# Path to Img.

img = cv2.imread('img.jpg')

# Path to Cascade Classifier.

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Converting BGR to GRAY.
    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Getting the faces.

faces = cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
        
    # Drawing a rectangle around the face.
        
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)
    
# Displaing the Img.

cv2.imshow('Face Tracking', img)

# Infinite loop.

cv2.waitKey(0)

# Destroying all the windows.

cv2.destroyAllWindows()
