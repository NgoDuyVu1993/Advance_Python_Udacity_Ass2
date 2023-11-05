"""Custom PDFIngestor to parse quotes from PDF files."""

import os
import random
import subprocess
from typing import List
import tempfile

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Custom class to ingest quotes from PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse PDF files and extract quotes."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with unsupported format: {path}")

        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
            subprocess.run(['pdftotext', path, tmp.name], check=True)
            quotes = []
            with open(tmp.name, 'r') as file:
                for line in file.readlines():
                    line = line.strip().split(' - ')
                    if len(line) == 2:
                        quote_body = line[0].strip()
                        quote_author = line[1].strip()
                        quotes.append(QuoteModel(quote_body, quote_author))

        return quotes