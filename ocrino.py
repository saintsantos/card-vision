import cv2
import numpy as np
from matplotlib import pyplot as plt

def ocrino(template, dictionary):

	for x in dictionary:

		MIN_MATCH_COUNT = 10
		img = cv2.imread(''.join(["cards", "/", dictionary[x]["image_location"]]),1)
		#w, h = template.shape[::-1]
		#print(''.join(["cards", "/", dictionary[x]["image_location"]]))
		"""sift = cv2.xfeatures2d.SIFT_create()

		kp1, des1 = sift.detectAndCompute(img, None)
		kp2, des2 = sift.detectAndCompute(template, None)
		#bf = cv2.BFMatcher()

		FLANN_INDEX_KDTREE = 0
		index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
		search_params = dict(checks = 50)
		flann = cv2.FlannBasedMatcher(index_params, search_params)
		matches = flann.knnMatch(des1, des2, k=2)

		good = []
		for m, n in matches:
			if m.distance < 0.7*n.distance:
				good.append([m])

		print(good)"""
		card = ("error",)
		tapped = (0,)
		# account for tapping

		# Apply template Matching
		res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		if (min_val < 0.005):
			#name of card goes here
			#print(min_val)
			#print(x)
			card = (x,)
			return card + tapped
		#print(min_val)
