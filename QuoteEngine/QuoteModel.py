class QuoteModel:
    """A class representing a quote with a body and an author."""

    def __init__(self, body: str, author: str):
        """Initialize a new QuoteModel instance.

        Args:
            body: The body of the quote (the actual quote text).
            author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a string that would recreate the object if passed to eval()."""
        return f'QuoteModel(body="{self.body}", author="{self.author}")'

    def __str__(self):
        """Return a string representation of the QuoteModel."""
        return f'"{self.body}" - {self.author}'

    def __eq__(self, other):
        """Check if two QuoteModel instances are equal.

        Args:
            other: The other QuoteModel instance to compare with.

        Returns:
            True if both QuoteModel instances have the same body and author, False otherwise.
        """
        if not isinstance(other, QuoteModel):
            return NotImplemented
        return self.body == other.body and self.author == other.author

    def __hash__(self):
        """Return the hash code for the quote.

        Returns:
            An integer hash code for the quote.
        """
        return hash((self.body, self.author))
