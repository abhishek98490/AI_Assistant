import os
import docx
import PyPDF2
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
from dataclasses import dataclass
from pathlib import Path


class Document_Loader():
 
    def read_txt(self,file_path:str) ->str :
        with open(file_path,"r",encoding ="utf-8") as file:
            return file.read()
        
    def read_doc(self,file_path:str):
        doc = docx.Document(file_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])

    def read_pdf(self,file_path:str):
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text

    def document_loader(self,file_path:str):
        
        file_name = os.path.basename(file_path)
        try:
            if file_name[-4:] ==".txt":
                logging.info("Input File is a .txt file")
                data = self.read_txt(file_path)
                logging.info("text extracted from .txt file")
                return data
            
            elif file_name[-4:] ==".pdf":
                logging.info("Input File is a .pdf file")
                data = self.read_pdf(file_path)
                logging.info("text extracted from .pdf file")
                return data
                
            
            elif file_name[-5:] ==".docx":
                logging.info("Input File is a .docx file")
                data = self.read_doc(file_path)
                logging.info("text extracted from .docx file")
                return data
                
        
        except Exception as e:
            logging.info("Exception occured in document loading")

            raise customexception(e,sys)

    
if __name__=="__main__":
    document = Document_Loader()
    print(document.document_loader("D:\\0MLOps\\RAG_Chatbot\\RAG_CHATBOT\\data\\text.txt"))