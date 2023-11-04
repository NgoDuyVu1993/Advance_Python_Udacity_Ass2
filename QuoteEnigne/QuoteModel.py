class QuoteModel:
    """
    A class that encapsulates the body and author of a quote.
    """

    def __init__(self, body, author):
        """
        Create a new 'QuoteModel' instance.

        :param body: The main text of the quote.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Return `str` representation of the `QuoteModel` instance.
        """
        return f'"{self.body}" - {self.author}'