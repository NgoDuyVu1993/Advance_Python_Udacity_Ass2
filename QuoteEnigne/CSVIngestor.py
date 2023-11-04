import pandas as pd
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """
    Ingestor to parse quotes from CSV files.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the CSV file at the given path and return a list of QuoteModel objects.

        :param path: The path to the CSV file to parse.
        :return: A list of QuoteModel instances.
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest exception for file {path}")

        quotes = []
        df = pd.read_csv(path, header=0)
        for _, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes