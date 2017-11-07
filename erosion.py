# Implement grayscale erosion with a square structuring element of a size 5x5.

import cv2
import sys
import numpy

filenameIn = sys.argv[1]
filenameOut = sys.argv[2]
img = cv2.imread(filenameIn, 0)

struct = numpy.ones((5,5), numpy.uint8)
origin = [3,3]
print(struct.shape[0]-origin[0])
img_eroded = numpy.zeros((img.shape[0],img.shape[1]), numpy.uint8)

# For each pixel of input image
for x in range(0, img.shape[1]):
	for y in range(0, img.shape[0]):
		# Fix the origin of the structuring element at x,y.
		# Then traverse each pixel of struct and work out what's beneath it.
		# And perform a reduce.
		verticalMove   = struct.shape[0]-origin[0]
		horizontalMove = struct.shape[1]-origin[1]
		firstPixelY    = y-verticalMove
		firstPixelX    = x-horizontalMove

		verticalRange   = range(y-verticalMove, y+1+verticalMove)
		horizontalRange = range(x-horizontalMove, x+1+horizontalMove)
		for a in horizontalRange:
			for b in verticalRange:
				#img_eroded[b,a] = 255
				g = 1


# A perfect erosion, performed by OpenCV's native method
#img = cv2.erode(img, struct, iterations=1)


# Normally save image, but for dev we just show it
#cv2.imwrite(filenameOut, img)
cv2.imshow('image', img_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
