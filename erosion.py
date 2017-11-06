import cv2
import sys

filenameIn = sys.argv[1]
filenameOut = sys.argv[2]

print("filename is", filenameIn)

img = cv2.imread(filenameIn, 0)



# Normally save image, but for dev we just show it
#cv2.imwrite(filenameOut, img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
