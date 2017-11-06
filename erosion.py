# Implement grayscale erosion with a square structuring element of a size 5x5.

import cv2
import sys
import numpy

filenameIn = sys.argv[1]
filenameOut = sys.argv[2]
img = cv2.imread(filenameIn, 0)

struct = numpy.ones((5,5), numpy.uint8)

# A perfect erosion, performed by OpenCV's native method
#img = cv2.erode(img, struct, iterations=1)


# Normally save image, but for dev we just show it
#cv2.imwrite(filenameOut, img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
