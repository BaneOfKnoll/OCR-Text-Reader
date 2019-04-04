import pytesseract
import PIL

im = PIL.Image.open("testImg.jpeg")



text = pytesseract.image_to_string(im, lang = 'eng')

print(text)
