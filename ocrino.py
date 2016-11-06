import cv2
import numpy as np
import PIL
import os
from matplotlib import pyplot as plt
from PIL import Image


function ocrino(template, dictionary):
	#here goes the start of the for loop to iterate over all entries in the dictionary
	for key in dictionary:	
		img = cv2.imread(dictionary[key]["image location"],0)

	#template = cv2.imread('tapped.jpg',0)
		w, h = template.shape[::-1]

		card = ("error",)
		tapped = (0,)

	# All the 6 methods for comparison in a list
		methods = 'cv2.TM_SQDIFF_NORMED'

		if w < h:
			tapped = (1,)
	#rotate template here
			os.system("convert tapped.jpg -rotate 90 tmp.jpg")
			template = cv2.imread('tmp.jpg',0)
			w, h = template.shape[::-1]

		method = eval(methods)

	    # Apply template Matching
		res = cv2.matchTemplate(img,template,method)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	

 	   # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
		if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
			top_left = min_loc
		else:
			top_left = max_loc
	
		if top_left[1] < 20:
			#parse	
			card = (key,)

		tup_out = card + tapped

		return tup_out
