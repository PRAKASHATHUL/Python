import cv2 as cv
img = cv.imread("20240903_135636.jpg")
cv.imshow("Display window",img)
k = cv.waitKey(5000)

