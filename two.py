import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd =  "C:/Program Files/Tesseract-OCR/tesseract.exe"
img = cv2.imread('fgfgf.jpg')
text = pytesseract.image_to_string(img, lang="ben")
print(text)