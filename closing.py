#####################################################################

# Implement grayscale closing with a square structuring element of
# size 5x5.
# Closing is defined as dilation followed by erosion with the same
# structuring element.
# This script relies on importing my exisiting implementations of
# dilation and erosion.

# Author : Alex Stuckey <alexander.e.stuckey@durham.ac.uk>
#                    or <alex@stuckey.org.uk>

# License : LGPL - http://www.gnu.org/licenses/lgpl.html

# version: 0.1

#####################################################################

import cv2
import sys
import numpy
import erosion
import dilation

#####################################################################
# Script implementation

# Accessing the file
filenameIn = sys.argv[1]
filenameOut = sys.argv[2]
readImage = cv2.imread(filenameIn, 0)

# My erosion implementation
img_dilated = dilation.dilate(readImage)
img_closed = erosion.erode(img_dilated)

# A perfect erosion, performed by OpenCV's native method
#img_closed2 = cv2.morphologyEx(readImage, cv2.MORPH_CLOSE, numpy.ones((5,5), numpy.uint8))

# Normally save image, but for dev we just show it
cv2.imwrite(filenameOut, img_closed)
#cv2.imwrite('lena_closing_perfect.png', img_closed2)
#cv2.imshow('mine', img_closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
