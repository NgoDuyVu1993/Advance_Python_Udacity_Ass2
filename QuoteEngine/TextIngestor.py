"""Module to ingest quotes from .txt files."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor for extracting quotes from .txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Extract quotes from a .txt file located at the given path.

        Args:
            path: The file system path to the .txt file.

        Returns:
            A list of QuoteModel instances extracted from the .txt file.

        Raises:
            ValueError: If the file type is not .txt or cannot be ingested.
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file type of {path}")

        quotes = []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(' - ')
                    if len(parts) == 2:
                        body, author = parts
                        quotes.append(QuoteModel(body.strip(), author.strip()))

        return quotes
