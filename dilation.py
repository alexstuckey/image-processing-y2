#####################################################################

# Implement grayscale dilation with a square structuring element of
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

def dilate(img):

  # Create a blank frame with the same dimensions as input image
  img_dilated = numpy.zeros((img.shape[0],img.shape[1]), numpy.uint8)

  # Apply padding to the input image, of a mirrored set of values,
  # this is to handle fitting in the structuring element on the
  # permimeter of the frame.
  # 
  # However, after this we must offset all co-ordinates by 2, and
  # use the original dimensions in the output frame.
  img = numpy.pad(img, ((2,2),(2,2)), mode='symmetric')

  struct = numpy.ones((5,5), numpy.uint8)
  origin = [((struct.shape[0]-1)/2)+1,((struct.shape[1]-1)/2)+1]
  verticalMove   = struct.shape[0]-origin[0]
  horizontalMove = struct.shape[1]-origin[1]

  # For each pixel of input image
  for x in range(0, img_dilated.shape[1]):
    for y in range(0, img_dilated.shape[0]):
      # Fix the origin of the structuring element at x,y
      # Then traverse each pixel of struct and find what's beneath it
      # And perform a reduce.
      verticalRange   = range(y-verticalMove, y+1+verticalMove)
      horizontalRange = range(x-horizontalMove, x+1+horizontalMove)
      supremum = 0
      for a in horizontalRange:
        for b in verticalRange:
          if img[b+2,a+2] > supremum:
            supremum = img[b+2,a+2]
      img_dilated[y,x] = supremum

  return img_dilated

#####################################################################
# Script implementation

def main():
  # Accessing the file
  filenameIn = sys.argv[1]
  filenameOut = sys.argv[2]
  readImage = cv2.imread(filenameIn, 0)

  # My erosion implementation
  img_dilated = dilate(readImage)

  # A perfect dilation, performed by OpenCV's native method
  #img_dilated2 = cv2.dilate(readImage, numpy.ones((5,5), numpy.uint8), iterations=1)


  # Normally save image, but for dev we just show it
  cv2.imwrite(filenameOut, img_dilated)
  
  #cv2.imshow('mine', img_dilated)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
   main()
