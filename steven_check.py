import cv2
import numpy

def check(lena, eroded, dilated, opened, closed):
    kernel = numpy.ones((5,5), numpy.uint8)
    lenaImg = cv2.imread(lena)

    myLenaEroded = cv2.imread(eroded)
    myLenaDilated = cv2.imread(dilated)
    myLenaOpened = cv2.imread(opened)
    myLenaClosed = cv2.imread(closed)

    cvLenaEroded = cv2.erode(lenaImg, kernel, iterations=1)
    cvLenaDilated = cv2.dilate(lenaImg, kernel, iterations=1)
    cvLenaOpened = cv2.morphologyEx(lenaImg, cv2.MORPH_OPEN, kernel)
    cvLenaClosed = cv2.morphologyEx(lenaImg, cv2.MORPH_CLOSE, kernel)

    if numpy.array_equal(myLenaEroded, cvLenaEroded):
        print("Erosion Correct")
    else:
        print("Erosion Not Correct")

    if numpy.array_equal(myLenaDilated, cvLenaDilated):
        print("Dilation Correct")
    else:
        print("Dilation Not Correct")

    if numpy.array_equal(myLenaOpened, cvLenaOpened):
        print("Opening Correct")
    else:
        print("Opening Not Correct")

    if numpy.array_equal(myLenaEroded, cvLenaEroded):
        print("Closing Correct")
    else:
        print("Closing Not Correct")

check("lena.png", "lena_erosion.png", "lena_dilation.png", "lena_opening.png", "lena_closing.png")

