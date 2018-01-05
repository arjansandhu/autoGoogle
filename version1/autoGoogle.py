# - *- coding: utf- 8 - *-

import os
#import nltk
import pytesseract
import cv2
import string

from PIL import Image, ImageGrab
from google import google

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

#stop = set(nltk.corpus.stopwords.words("english"))

image = ImageGrab.grab(bbox=(30, 350, 900, 700))
#image.show()
image.save("screenshot.png")

image = cv2.imread('screenshot.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Image", gray)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
result = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
#print(result)

# Split up newlines until we have our question and answers
#parts = result.split("\n\n")
question = result.replace("\n", " ")
question = question.encode("utf-8")
question = ''.join([x for x in question if x in string.printable])


#print("\n" + question + "\n\n" + ", ".join(answers) + "\n\n")
print(question + "\n")

search_results = google.search(question)

if search_results:
    result1 = ''.join([x for x in search_results[0].description.encode("utf-8") if x in string.printable]) + "\n"
    result2 = ''.join([x for x in search_results[1].description.encode("utf-8") if x in string.printable]) + "\n"
    result3 = ''.join([x for x in search_results[2].description.encode("utf-8") if x in string.printable]) + "\n"
    result4 = ''.join([x for x in search_results[3].description.encode("utf-8") if x in string.printable]) + "\n"
    result5 = ''.join([x for x in search_results[4].description.encode("utf-8") if x in string.printable]) + "\n"

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
else:
    print("no google results")