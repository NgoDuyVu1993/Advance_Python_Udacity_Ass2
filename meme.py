# meme.py

import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an image path and a quote.

    Args:
        path (str): Path to an image file.
        body (str): Quote body to add to the image.
        author (str): Quote author to add to the image.

    Returns:
        str: The file path to the generated meme.
    """
    img = None

    if path is None:
        images_path = "./_data/photos/dog/"
        imgs = [
            os.path.join(images_path, name) for name in os.listdir(images_path)
            if os.path.splitext(name)[1] in ('.jpg', '.png')
        ]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for file_path in quote_files:
            try:
                quotes.extend(Ingestor.parse(file_path))
            except ValueError as e:
                print(f"Could not parse file {file_path}: {e}")
        quote = random.choice(quotes)
        body = quote.body
        author = quote.author

    if body and not author:
        raise ValueError("Author is required if body is provided.")

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, body, author)
    return path

def main():
    """Process command-line arguments and generate a meme."""
    parser = argparse.ArgumentParser(description="Meme Generator CLI")
    parser.add_argument('--path', type=str, help="Path to an image file.")
    parser.add_argument('--body', type=str, help="Quote body to add to the image.")
    parser.add_argument('--author', type=str, help="Quote author to add to the image.")

    args = parser.parse_args()
    if args.body and not args.author:
        parser.error("--author is required when --body is provided.")
    meme_path = generate_meme(args.path, args.body, args.author)
    print(f"Meme created at: {meme_path}")

if __name__ == "__main__":
    main()
