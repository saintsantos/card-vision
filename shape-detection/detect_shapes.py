# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt

# construct the argument parse and parse the arguments
"""ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-d", "--dict", required=True,
	help="path to dictionary file")

args = vars(ap.parse_args())"""

function boardParser(image, dictionary):
	# load the image and resize it to a smaller factor so that
	# the shapes can be approximated better
	image = cv2.imread(image)
	dictionary = args[dictionary]
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])

	# convert the resized image to grayscale, blur it slightly,
	# and threshold it
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# find contours in the thresholded image and initialize the
	# shape detector
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	sd = ShapeDetector()

	# loop over the contours
	for c in cnts:
		# compute the center of the contour, then detect the name of the
		# shape using only the contour
		M = cv2.moments(c)
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
		shape = sd.detect(c)

		# multiply the contour (x, y)-coordinates by the resize ratio,
		# then draw the contours and the name of the shape on the image
		c = c.astype("float")
		c *= ratio
		c = c.astype("int")

		#get ready to crop
		x,y,w,h = cv2.boundingRect(c)

		# crop & show the output image
		crop = image[y:y+h, x:x+w]
		cv2.imshow("Image", crop)
		cv2.waitKey(0)
