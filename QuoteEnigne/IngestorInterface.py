from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """
    Abstract base class defining the interface for ingestors.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the file extension is one that can be ingested.

        :param path: The path to the file to check.
        :return: True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abstract method to parse a file and return a list of QuoteModel objects.

        :param path: The path to the file to parse.
        :return: A list of QuoteModel instances.
        """
        pass