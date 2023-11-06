"""Module for ingesting quotes from PDF files."""

import os
import subprocess
from typing import List
import tempfile

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingestor for parsing quotes from PDF files.

    This class inherits from IngestorInterface and implements the parse method
    for PDF files.
    """

    allowed_extensions = ['pdf']
    """List of allowed file extensions for this ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a PDF file and create a list of QuoteModel objects.

        This method uses the `pdftotext` command-line utility to convert PDF
        content to text and then extracts quotes and authors.

        Parameters:
            path (str): The file path to the PDF file to be ingested.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with unsupported format: {path}")

        try:
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
                subprocess.run(['pdftotext', path, tmp.name], check=True)
                tmp_path = tmp.name

            quotes = []
            with open(tmp_path, 'r') as file:
                for line in file.readlines():
                    line = line.strip().split(' - ')
                    if len(line) == 2:
                        quote_body = line[0].strip()
                        quote_author = line[1].strip()
                        quotes.append(QuoteModel(quote_body, quote_author))

            os.unlink(tmp_path)  # Clean up the temporary file
            return quotes
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error during PDF to text conversion: {e}")
