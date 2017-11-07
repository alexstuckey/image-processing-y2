#####################################################################

# Implement grayscale opening with a square structuring element of
# size 5x5.
# Opening is defined as erosion followed by dilation with the same
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

def main():
  # Accessing the file
  filenameIn = sys.argv[1]
  filenameOut = sys.argv[2]
  readImage = cv2.imread(filenameIn, 0)

  # My erosion implementation
  img_eroded = erosion.erode(readImage)
  img_opened = dilation.dilate(img_eroded)

  # A perfect erosion, performed by OpenCV's native method
  #img_opened2 = cv2.morphologyEx(readImage, cv2.MORPH_OPEN, numpy.ones((5,5), numpy.uint8))

  # Normally save image, but for dev we just show it
  cv2.imwrite(filenameOut, img_opened)
  #cv2.imwrite('lena_opening_perfect.png', img_opened2)

  #cv2.imshow('mine', img_opened)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
   main()
