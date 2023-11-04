from typing import List
from docx import Document
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """
    Ingestor to parse quotes from DOCX files.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the DOCX file at the given path and return a list of QuoteModel objects.

        :param path: The path to the DOCX file to parse.
        :return: A list of QuoteModel instances.
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest exception for file {path}")

        quotes = []
        doc = Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parts = para.text.split(' - ')
                if len(parts) == 2:
                    new_quote = QuoteModel(parts[0], parts[1])
                    quotes.append(new_quote)

        return quotes