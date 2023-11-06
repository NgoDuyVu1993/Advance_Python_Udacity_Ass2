from PIL import Image, ImageDraw, ImageFont
import os
import random

# Constants for the meme generation
DEFAULT_FONT_PATH = './font/LilitaOne-Regular.ttf'
FONT_SIZE_RATIO = 0.45
IMAGE_MARGIN = 20
RANDOM_FILENAME_RANGE = 1000000


class MemeEngine:
    def __init__(self, output_dir, font_path=DEFAULT_FONT_PATH):
        """
        Create a MemeEngine instance that stores memes in output_dir.

        :param output_dir: Directory to save generated memes.
        :param font_path: Path to the font file.
        """
        self.output_dir = output_dir
        self.font_path = font_path
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme with an image and quote.

        :param img_path: Path to the input image.
        :param text: Quote text to add to the image.
        :param author: Author of the quote.
        :param width: Desired width of the meme image.
        :return: Path to the generated meme image.
        """
        try:
            with Image.open(img_path) as img:
                # Initialize height with the current image height
                height = img.height

                # Resize the image if it's wider than the specified width
                if img.width > width:
                    ratio = width / float(img.width)
                    height = int(ratio * float(img.height))
                    img = img.resize((width, height), Image.NEAREST)

                # Add text to the image
                if text and author:
                    draw = ImageDraw.Draw(img)
                    font_size = int(height * FONT_SIZE_RATIO)  # Start with a larger font size
                    font = self.load_font(font_size)

                    full_text = f'{text} - {author}'
                    text_size = draw.textsize(full_text, font=font)
                    # Reduce font size until the text fits the image width
                    while text_size[0] > img.width - IMAGE_MARGIN:
                        font_size -= 1
                        font = self.load_font(font_size)
                        text_size = draw.textsize(full_text, font=font)

                    text_position = (10, self.get_random_y_position(height, font_size))
                    draw.text(text_position, full_text, font=font, fill='white')

                # Save the meme image
                out_path = os.path.join(
                    self.output_dir,
                    f'meme_{random.randint(0, RANDOM_FILENAME_RANGE)}.jpg'
                )
                img.save(out_path, format='JPEG')
                return out_path
        except IOError as e:
            print(f'An error occurred when opening the image: {e}')
            return ''
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return ''

    def load_font(self, font_size):
        """
        Load the font with the specified size.

        :param font_size: Size of the font to load.
        :return: Loaded font object.
        """
        try:
            return ImageFont.truetype(self.font_path, font_size)
        except IOError:
            print(f"Cannot open font file: {self.font_path}. Using default font.")
            return ImageFont.load_default()

    def get_random_y_position(self, height, font_size):
        """
        Return a random y-axis position for the text.

        :param height: Height of the image.
        :param font_size: Size of the font.
        :return: Random y position for the text.
        """
        y_min = 10
        y_max = height - font_size * 2
        return random.randint(y_min, y_max)
