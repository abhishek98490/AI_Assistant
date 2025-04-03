import os
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
from src.pdf_input.document_loader import Document_Loader
from src.pdf_input.document_parser import Chunking
from src.pdf_input.document_parser import Chroma_database


class Retrieval:
    def __init__(self):
        self.db = Chroma_database()

    def process_document(self, file_path, query):
        filename = os.path.basename(file_path)

        try:
            logging.info("Initializing document loader")
            doc = Document_Loader()
            text = doc.document_loader(file_path)
            logging.info("Text extracted from the document")
        except Exception as e:
            raise customexception(e, sys)

        try:
            chunking = Chunking(200, 30)
            chunks = chunking.sliding_window_chunking(text)
            logging.info("Chunked text received")
        except Exception as e:
            raise customexception(e, sys)
        
        # Step 3: Process and Retrieve from Database
        try:
            self.db.process_and_add_documents(chunks, filename)
            context, sources = self.db.retrive_text(query, filename, n_results=2)
            logging.info("Text retrieved from the document")
            return context, sources
        except Exception as e:
            raise customexception(e, sys)

if __name__=="__main__":
    retrieval = Retrieval()
    context, sources = retrieval.process_document('D:\\0MLOps\\RAG_Chatbot\\RAG_CHATBOT\\data\\text.txt', 'When did Dr. APJ Abdul Kalam pass away, and how?')
    print(context)
    print(":::::::::::::::::::::::::::::::::::::")
    print(sources)