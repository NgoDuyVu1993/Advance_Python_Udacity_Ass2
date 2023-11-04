import os
import random
import argparse

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an image path and a quote.

    If any argument is not defined, a random selection is used.

    :param path: str - the file location for the input image.
    :param body: str - the body of the quote.
    :param author: str - the author of the quote.
    :return: str - the file path to the output image.
    """
    img = None
    quote = None

    if path is None:
        imgs = "./_data/photos/dog/"
        imgs = [os.path.join(imgs, name) for name in os.listdir(imgs)]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author required if body is provided')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./static')
    path = meme.make_meme(img, quote.body, quote.author)
    return path

def main():
    """Command-line interface for the meme generator script."""
    parser = argparse.ArgumentParser(description='Generate a Meme')
    parser.add_argument('--path', type=str, default=None,
                        help='path to an image file')
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image')
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))

if __name__ == "__main__":
    main()
