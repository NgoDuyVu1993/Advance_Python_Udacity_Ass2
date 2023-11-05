from PIL import Image, ImageDraw, ImageFont
import os
import random

class MemeEngine:
    def __init__(self, output_dir, font_path='./font/LilitaOne-Regular.ttf'):
        """Create a MemeEngine instance that stores memes in output_dir."""
        self.output_dir = output_dir
        self.font_path = font_path
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme with an image and quote."""
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
                if text is not None and author is not None:
                    draw = ImageDraw.Draw(img)
                    # Start with a larger font size proportion, e.g., 45% of the image height for bigger text
                    font_size = int(height * 0.45)  # Start with a larger font size
                    try:
                        font = ImageFont.truetype(self.font_path, font_size)
                        # font = ImageFont.truetype('./font/LilitaOne-Regular.ttf', int(height/20))
                    except IOError:
                        print(f"Cannot open font file: {self.font_path}. Using default font.")
                        font = ImageFont.load_default()
                        # font = ImageFont.truetype('./font/LilitaOne-Regular.ttf', int(height/20))

                    full_text = f'{text} - {author}'
                    # Calculate text size
                    text_size = draw.textsize(full_text, font=font)
                    # Reduce font size until the text fits the image width
                    while text_size[0] > img.width - 20:  # 20 pixels margin
                        font_size -= 1
                        try:
                            font = ImageFont.truetype(self.font_path, font_size)
                        except IOError:
                            font = ImageFont.load_default()
                        text_size = draw.textsize(full_text, font=font)
                    text_position = (10, self.get_rand_y(height, font_size))
                    draw.text(text_position, full_text, font=font, fill='white')

                # Save the meme image
                out_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 1000000)}.jpg')
                img.save(out_path, format='JPEG')  # Specify the format explicitly
                return out_path
        except Exception as e:  # Consider catching specific exceptions
            print(f'An error occurred: {e}')
            return ''

    def get_rand_y(self, height, font_size):
        """Return a random y-axis position for the text."""
        y_min = 10
        y_max = height - font_size * 2  # Adjust y_max to account for text height
        return random.randint(y_min, y_max)