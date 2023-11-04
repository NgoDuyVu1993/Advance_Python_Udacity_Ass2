from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """
    Ingestor to parse quotes from text files.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the text file at the given path and return a list of QuoteModel objects.

        :param path: The path to the text file to parse.
        :return: A list of QuoteModel instances.
        """
        if not cls.can_ingest(path):
            raise Exception(f"Cannot ingest exception for file {path}")

        with open(path, 'r') as file:
            lines = file.readlines()
            quotes = [QuoteModel(*line.strip('\n\r').strip().split(' - '))
                      for line in lines if line.strip('\n\r').strip()]

        return quotes