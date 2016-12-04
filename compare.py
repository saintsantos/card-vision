# USAGE
# python compare.py

# import the necessary packages

from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])

	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare(template, dictionary):

	for x in dictionary:

		MIN_MATCH_COUNT = 10
		img = cv2.imread(''.join(["cards", "/", dictionary[x]["image_location"]]),1)
		#w, h = template.shape[::-1]
		#print(''.join(["cards", "/", dictionary[x]["image_location"]]))

		card = ("error",)
		tapped = (0,)
		# account for tapping

		#cv2.imshow('template',template)
		#cv2.waitKey(0)
		try:
			height, width = img.shape[:2]
		except AttributeError:
			return card + tapped

		print (width,",",height)

		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		newtemp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

		# Apply template Matching
		#res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
		#ss, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		s = ssim(img, cv2.resize(newtemp, (width, height)))
		m = mse(img, cv2.resize(newtemp, (width, height)))
		print (s)
		print (m)
		print(dictionary[x])
		if (s > 0.2):
			#name of card goes here
			#print(min_val)
			#print(x)
			card = (x,)
			print('EETS A MATCH')
			print(dictionary[x])
			return card + tapped
			#print('EETS A MATCH')
		#print(min_val)
