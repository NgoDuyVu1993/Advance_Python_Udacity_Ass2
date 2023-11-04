import random
import os
import requests
from flask import Flask, render_template, abort, request

app = Flask(__name__)

# Configure the MemeEngine with the path to the static directory
meme_engine = MemeEngine('./static')


@app.route('/')
def meme_rand():
    """Generate and display a random meme.

    Selects a random image and a random quote, generates a meme,
    and renders it on the homepage.
    """
    try:
        # Assuming there's a function to get a random image path
        img_path = get_random_image_path()
        # Assuming there's a function to get a random quote
        quote = get_random_quote()
        # Generate meme with the MemeEngine
        path = meme_engine.make_meme(img_path, quote.body, quote.author)
        return render_template('meme.html', path=path)
    except Exception as e:
        print(f"An error occurred: {e}")
        abort(500)


@app.route('/create', methods=['GET'])
def meme_form():
    """Render form for users to input their own quotes and select an image."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme.

    Takes input from the form, generates a meme with the provided image
    and quote, and renders the meme for the user.
    """
    try:
        # Fetch form data
        img_path = request.form['image_path']
        body = request.form['body']
        author = request.form['author']

        # Generate meme with the MemeEngine
        path = meme_engine.make_meme(img_path, body, author)
        return render_template('meme.html', path=path)
    except Exception as e:
        print(f"An error occurred: {e}")
        abort(500)


def get_random_image_path() -> str:
    """Retrieve a random image path from the images directory."""
    images_path = './_data/photos/dog/'
    images = os.listdir(images_path)
    return os.path.join(images_path, random.choice(images))


def get_random_quote():
    """Retrieve a random quote using the QuoteEngine module."""
    # Assuming there's a function in the Ingestor class to load all quotes
    quotes = Ingestor.load_quotes('./_data/quotes')
    return random.choice(quotes)


if __name__ == '__main__':
    app.run()