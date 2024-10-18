import cv2
import numpy as np
import pytesseract
from PIL import Image
class OCR_TES():
	def __init(self):
		pytesseract.pytesseract.tesseract_cmd = r"C:\Users\DELL\Tesseract-OCR\tesseract.exe"
	def result(self,instance,btn_name):
		# 1. Load the image
		img = cv2.imread(instance)
		
		# 2. Resize the image
		#img = cv2.resize(img, None, fx=0.5, fy=0.5)
		# 3. Convert image to grayscale
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# 4. Convert image to black and white (using adaptive threshold)
		if btn_name == 'OCR(B)':
			ret, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV) 
			ret, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
		else:
			ret, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
		#gray = cv2.medianBlur(gray, 3)#2.less partial
		filename = "{}.jpeg".format("temp")
		cv2.imwrite(filename, gray)
		im=Image.open(filename)
		text = pytesseract.image_to_string(im,lang='eng+tel+hin+tam+ori')
		return text
#print(ocr_obj.result(r"C:\Users\DELL\Tesseract-OCR\Images\bigsleep.jpg",'OCR(B)')) 