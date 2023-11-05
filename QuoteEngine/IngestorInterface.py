"""Module to define the Ingestor Interface for quote parsing."""

from abc import ABC, abstractmethod
from typing import List
from itertools import chain
import re
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class outlining the structure of an ingestor."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file can be ingested based on its extension."""
        ext = cls.ext_from_path(path)
        return ext in cls.allowed_extensions

    @classmethod
    def ext_from_path(cls, path: str) -> str:
        """Return a file extension from path string."""
        return path.split('.')[-1]

    @classmethod
    def extension_support(cls) -> List[str]:
        """Return a list of all supported parse extension formats from subclasses."""
        return list(chain(*[c.allowed_extensions for c in cls.__subclasses__()]))

    @classmethod
    def clean_text(cls, text: str) -> str:
        """Return text free of unwanted and non-printable characters."""
        remove_chars = r"[()\"#/@;<>{}`+=~|.!?,]"
        return ''.join(filter(str.isprintable, re.sub(remove_chars, "", text).strip()))

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to parse a file and return a list of QuoteModel objects."""
        raise NotImplementedError("Subclasses must implement the parse method.")
