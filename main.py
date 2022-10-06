from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd =  "C:/Program Files/Tesseract-OCR/tesseract.exe"
image = 'banglaText.png'
text = pytesseract.image_to_string(Image.open(image), lang="ben")
print(text)



#image = Image.open('img.png')
#print(image)