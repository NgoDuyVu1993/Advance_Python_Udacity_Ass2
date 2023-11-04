import subprocess
import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """
    Ingestor to parse quotes from PDF files.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the PDF file at the given path and return a list of QuoteModel objects.

        :param path: The path to the PDF file to parse.
        :return: A list of QuoteModel instances.
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest exception for file {path}")

        tmp = f'./tmp/{os.path.basename(path)}.txt'
        try:
            subprocess.run(['pdftotext', path, tmp], check=True)
            with open(tmp, 'r') as file:
                lines = file.readlines()
                quotes = [QuoteModel(*line.strip('\n\r').strip().split(' - '))
                          for line in lines if line.strip('\n\r').strip()]
        finally:
            os.remove(tmp)

        return quotes