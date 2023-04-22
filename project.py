import cv2
import numpy as np

def find_red_circle_location(img, x_cent, y_cent):
    little_img = img[y_cent-2:y_cent+1, x_cent-2: x_cent+1]
    if little_img[:, :, 2].mean() > 200 and little_img[:, :, 1].mean() < 60 and little_img[:, :, 0].mean() < 60:
        print(f"Red circle center location(x, y) is: ({x_cent}, {y_cent})")

img = cv2.imread("res/image.jpg")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2GRAY)

circles_detected = []
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT_ALT, dp=1, minDist=10, param1=1.5, param2=0.7, minRadius=10, maxRadius=25)

if circles is not None:
    circles_detected = circles[0].astype(np.uint32)
    for circle in circles_detected:
        x_cent = circle[0]
        y_cent = circle[1]
        cv2.circle(img, (x_cent, y_cent), circle[2], (0, 0, 255), 1)
        find_red_circle_location(img, x_cent, y_cent)

print(f"Detected Circles Count: {circles_detected.__len__()}")

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
