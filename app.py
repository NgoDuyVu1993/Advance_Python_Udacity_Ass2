# app.py

import os
import random
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

# Initialize MemeEngine with the path to the static directory
meme = MemeEngine('./static')

def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []
    for f in quote_files:
        try:
            quotes.extend(Ingestor.parse(f))
        except Exception as e:
            print(f"Error parsing {f}: {e}")
    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, f) for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))]
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')

@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    img = None
    if image_url:
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            img = f'./static/{random.randint(0, 1000000)}.jpg'
            with open(img, 'wb') as img_file:
                img_file.write(img_response.content)
        else:
            print(f"Could not download image from {image_url}")
            img = random.choice(imgs)  # Fallback to a random image
    else:
        img = random.choice(imgs)

    path = meme.make_meme(img, body, author)
    if image_url:
        os.remove(img)  # Clean up the downloaded image

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run()