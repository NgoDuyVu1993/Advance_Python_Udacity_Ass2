"""Module for generating memes by adding quotes to images."""

from PIL import Image, ImageDraw, ImageFont
import random
import os

class MemeEngine:
    """
    A class to encapsulate the meme generation logic.
    """

    def __init__(self, output_dir):
        """
        Create a new 'MemeEngine' instance.

        :param output_dir: The directory where generated memes should be stored.
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme with a quote.

        :param img_path: The file location for the input image.
        :param text: The text of the quote.
        :param author: The author of the quote.
        :param width: The width of the meme image.
        :return: The file path to the created meme.
        """
        try:
            img = Image.open(img_path)
            if width is not None and img.width > width:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Image.ANTIALIAS)

            draw = ImageDraw.Draw(img)
            font_path = os.path.join('fonts', 'LilitaOne-Regular.ttf')
            font = ImageFont.truetype(font_path, size=int(height / 10))

            text = text + ' - ' + author
            draw.text((10, 10), text, font=font, fill='white')

            out_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 1000000)}.jpg')
            img.save(out_path)

        except Exception as e:
            print(f'An error occurred: {e}')
            return ''

        return out_path