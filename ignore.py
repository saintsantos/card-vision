import cv2
import numpy as np
from matplotlib import pyplot as plt

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import tesserocr
from asprise_ocr_api import *

def fuck_asprise():
    Ocr.set_up() # one time setup
    ocrEngine = Ocr()
    ocrEngine.start_engine("eng", START_PROP_DICT_CUSTOM_DICT_FILE="dict.txt")
    s = ocrEngine.recognize("images/necro2.jpg", -1, -1, -1, -1, -1,\
                  OCR_RECOGNIZE_TYPE_TEXT, OCR_OUTPUT_FORMAT_PLAINTEXT)
    print ("Result: " + s)
    # recognizes more images here ..
    ocrEngine.stop_engine()

def fuck():
    #img1 = cv2.imread("images/necro_test.jpg")
    img2 = cv2.imread("images/necro2.jpg")
    img2  = np.array(img2, np.uint8)
    gray = cv2.imread('images/gg_old_crop.jpg', cv2.IMREAD_GRAYSCALE)
    gray = cv2.resize(gray, (0,0), fx=3, fy=3)
    cv2.bitwise_not ( gray, gray )
    height, width, channels = img2.shape
    #th3 , gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,8)
    ret2,th2 = cv2.threshold(gray ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret3,th4 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.imshow('hullo', th3)
    key = cv2.waitKey()
    print("Result: ", pytesseract.image_to_string(Image.fromarray(th3), lang='eng', config='tess.config'))
    image = Image.open('images/ally.png')
    #print (tesserocr.image_to_text(img2))
fuck()
