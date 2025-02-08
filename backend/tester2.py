import cv2
import os

if not os.path.exists('D:/golfai/videos/testerimage1.jpg'):
    print("Image file not found!")
else:
    img = cv2.imread('D:/golfai/videos/testerimage1.jpg')
    cv2.imshow('Test Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()