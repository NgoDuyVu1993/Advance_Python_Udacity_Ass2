class QuoteModel:
    def __init__(self, body: str, author: str):
        """Create a new QuoteModel instance.

        :param body: The body of the quote (the actual quote text).
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return `str(self)`."""
        return f'"{self.body}" - {self.author}'

    def __str__(self):
        """Return a string representation of the QuoteModel."""
        return f'"{self.body}" - {self.author}'

    def __eq__(self, other):
        """Check if two QuoteModel instances are equal."""
        return self.body == other.body and self.author == other.author

    def __hash__(self):
        """Return the hash code for the quote."""
        return hash((self.body, self.author))
