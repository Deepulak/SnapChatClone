import cv2 as cv
import  cvzone
cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv.imread('cool.png', cv.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
    cv.imshow('Snap Dude', frame)
    if cv.waitKey(10) == ord('q'):
        break
