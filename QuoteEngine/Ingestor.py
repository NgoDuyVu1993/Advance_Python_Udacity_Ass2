"""Ingestor to manage different file ingestors."""

from typing import List
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """Ingestor class that encapsulates all the ingestors."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate ingestor for the file extension and parse the file."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception(f'No suitable ingestor found for the file {path}')
