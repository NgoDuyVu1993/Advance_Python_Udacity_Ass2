"""Module for ingesting quotes from CSV files."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor for parsing quotes from CSV files.

    This class inherits from IngestorInterface and implements the parse method
    for CSV files.
    """

    allowed_extensions = ['csv']
    """List of allowed file extensions for this ingestor."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CSV file and create a list of QuoteModel objects.

        This method reads the CSV file, extracts the quote and author, and
        returns a list of QuoteModel instances.

        Parameters:
            path (str): The file path to the CSV file to be ingested.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file with unsupported extension: {path}")

        quotes_df = pd.read_csv(path)
        quotes = quotes_df.apply(
            lambda x: QuoteModel(x['body'], x['author']), axis=1
        ).tolist()

        return quotes
