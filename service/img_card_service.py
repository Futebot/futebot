from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from discord import File
import logging as puts

from exception.exceptions import TooManyCharsException, FutebotException


def generate_card(string: str, img_path: str, filename: str, font_size: int, x: int, y: int, color, char_limit):
    try:

        if len(string) >= char_limit:  # 23 or bigger string would cut the text out, for now just avoid it.
            raise TooManyCharsException("Diminue esse textão aí, pfv.")

        else:
            position = (x, y)
            img = Image.open(img_path)
            drawer = ImageDraw.Draw(img)
            drawer.text(position, string,
                        font=ImageFont.truetype(font='templates/fonts/OpenSans-Bold.ttf', size=font_size),
                        fill=color)
            img.save(filename+".png")
            return File(open(filename+".png", "rb"))

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)
