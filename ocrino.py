import cv2
import numpy as np
from matplotlib import pyplot as plt

def ocrino(template, dictionary):
	for x in dictionary:

		img = cv2.imread(''.join(["cards", "/", dictionary[x]["image_location"]]),0)
		#w, h = template.shape[::-1]
		card = ("error",)
		tapped = (0,)
		# account for tapping

		# Apply template Matching
		res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		top_left = min_loc

		if top_left > 19 and top_left < 31:
			#name of card goes here
			card = (x,)
			return card + tapped
