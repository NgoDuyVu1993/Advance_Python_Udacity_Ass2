"""Custom DocxIngestor to parse quotes from .docx files."""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Custom class to ingest quotes from .docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .docx files and extract quotes."""
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
        """Clean text by removing unwanted characters or formatting."""
        # Implement any necessary text cleaning here
        return text.strip()