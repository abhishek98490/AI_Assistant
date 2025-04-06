import pytesseract
from PIL import Image
import io
import sys
from src.logger.logging import logging
from src.exception.exception import customexception

class Image_loader:

    def text_detector(self, image):
        try:
            ocr_text = pytesseract.image_to_string(image)
            return ocr_text
        except Exception as e:
            logging.info("Exception occurred in text_detector")
            raise customexception(e, sys)

    def img_loader(self, file_path):
        try:
            image = Image.open(file_path)
            text = self.text_detector(image)

            if text and len(text.strip()) > 10:
                return text
            else:
                return image  # In case OCR fails, return the image itself
        except Exception as e:
            logging.info("Exception occurred in img_loader")
            raise customexception(e, sys)
        

if __name__=="__main__":
    im = Image_loader()
    print(im.img_loader("/Users/abhishek/Codes/AI_Assistant/DSC_1092-removebg-preview.png"))
