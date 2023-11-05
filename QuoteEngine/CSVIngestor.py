"""This parses CSV files and creates quote objects."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Class to parse CSV files and create quote objects."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the CSV file at the path and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with unsupported extension for {path}")

        quotes = pd.read_csv(path).apply(
            lambda x: QuoteModel(body=x['body'], author=x['author']), axis=1
        ).to_list()

        return quotes
