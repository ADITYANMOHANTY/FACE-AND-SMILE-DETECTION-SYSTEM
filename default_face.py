import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# Read the input image
img = cv2.imread('image.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#Detect smiles
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
 
for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
# It will Display the output image
cv2.imshow('img', img)
cv2.waitKey()