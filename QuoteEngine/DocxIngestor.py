"""Module for ingesting quotes from DOCX files."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingestor for parsing quotes from DOCX files.

    This class inherits from IngestorInterface and implements the parse method
    for DOCX files.
    """

    allowed_extensions = ['docx']
    """List of allowed file extensions for this ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a DOCX file and create a list of QuoteModel objects.

        This method reads the DOCX file, extracts the quote and author, and
        returns a list of QuoteModel instances.

        Parameters:
            path (str): The file path to the DOCX file to be ingested.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with path: {path}")

        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text.strip() != "":
                parts = paragraph.text.strip().split(' - ')
                if len(parts) >= 2:
                    quote_body = parts[0].strip()
                    quote_author = parts[1].strip()
                    quotes.append(QuoteModel(quote_body, quote_author))

        return quotes

    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text by removing extraneous whitespace and formatting.

        Parameters:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        # Implement any necessary text cleaning here
        return text.strip()
