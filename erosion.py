#####################################################################

# Implement grayscale erosion with a square structuring element of
# size 5x5.

# Author : Alex Stuckey <alexander.e.stuckey@durham.ac.uk>
#                    or <alex@stuckey.org.uk>

# License : LGPL - http://www.gnu.org/licenses/lgpl.html

# version: 0.1

#####################################################################

import cv2
import sys
import numpy

#####################################################################
# Defining functions

def erode(img):

  img_eroded = numpy.zeros((img.shape[0],img.shape[1]), numpy.uint8)

  struct = numpy.ones((5,5), numpy.uint8)
  origin = [((struct.shape[0]-1)/2)+1,((struct.shape[1]-1)/2)+1]
  verticalMove   = struct.shape[0]-origin[0]
  horizontalMove = struct.shape[1]-origin[1]

	# For each pixel of input image
  for x in range(0, img.shape[1]):
	  for y in range(0, img.shape[0]):
		  # Fix the origin of the structuring element at x,y
		  # Then traverse each pixel of struct and find what's beneath it
		  # And perform a reduce.
		  verticalRange   = range(y-verticalMove, y+1+verticalMove)
		  horizontalRange = range(x-horizontalMove, x+1+horizontalMove)
		  infimum = 255
		  for a in horizontalRange:
			  for b in verticalRange:
				  if img[b,a] < infimum:
					  infimum = img[b,a]
		  img_eroded[y,x] = infimum



#####################################################################
# Script implementation

# Accessing the file
filenameIn = sys.argv[1]
filenameOut = sys.argv[2]
readImage = cv2.imread(filenameIn, 0)

# My erosion implementation
img_eroded = erode(readImage)

# A perfect erosion, performed by OpenCV's native method
#img_eroded = cv2.erode(img, struct, iterations=1)


# Normally save image, but for dev we just show it
#cv2.imwrite(filenameOut, img)
cv2.imshow('image', img_eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
