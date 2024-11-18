import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def ocr(img):
    text=pytesseract.image_to_string(img)
    return text

img=cv2.imread('img_3.png')

#getting a grayscale image
def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# noise removal-- to deal with distorted images or less pixelated images
def remove_noise(image):
    return cv2.medianBlur(image,5)

# thresholding for colors
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

img=grayscale(img)
img=thresholding(img)
img=remove_noise(img)

print(ocr(img))