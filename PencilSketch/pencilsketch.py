import cv2
im=cv2.imread("arno.jpg")
gray_im=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
invert_im=255-gray_im
blur_im=cv2.GaussianBlur(invert_im, (21, 21), 0)
invert_blur=255-blur_im
ps=cv2.divide(gray_im, invert_blur, scale=256.0)
cv2.imshow("Real Image", im)
cv2.imshow("Sketch Image", ps)
cv2.waitKey(0)
