from io import BytesIO

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont
from PIL import ImageOps
from discord import File
import logging as puts

from exception.exceptions import TooManyCharsException, FutebotException


def generate_card(string: str, img_path: str, filename: str, font_size: int, x: int, y: int, color, char_limit,
                  font="opensans"):
    try:

        if len(string) >= char_limit:  # 23 or bigger string would cut the text out, for now just avoid it.
            raise TooManyCharsException("Diminue esse textão aí, pfv.")

        else:
            position = (x, y)
            img = Image.open(img_path)
            drawer = ImageDraw.Draw(img)
            drawer.text(position, string,
                        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
                        fill=color)

            img.save(filename+".png")
            return File(open(filename+".png", "rb"))

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def generate_card_img(string: str, img_path: str, filename: str, font_size: int, x: int, y: int, color, char_limit,
                      img_url, img_x, img_y, img_width, img_height, font="opensans"):
    try:

        if len(string) >= char_limit:  # 23 or bigger string would cut the text out, for now just avoid it.
            raise TooManyCharsException("Diminue esse textão aí, pfv.")

        else:
            position = (x, y)
            img = Image.open(img_path)
            drawer = ImageDraw.Draw(img)
            drawer.text(position, string,
                        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
                        fill=color)

            response = requests.get(img_url, stream=True)
            img2 = Image.open(BytesIO(response.content))
            img2.thumbnail((img_width, img_height), Image.ANTIALIAS)
            img.paste(img2, (img_x, img_y))

            img.save(filename+".png")
            return File(open(filename+".png", "rb"))

    except Exception as e:
        puts.info(e)
        return None


def generate_card_img_title_description(string: str, img_path: str, filename: str, font_size: int, x: int, y: int,
                                        color, char_limit, img_url, img_x, img_y, img_width, img_height,
                                        description: str, desc_x: int, desc_y: int, desc_font_size: int,
                                        font="opensans"):
    try:

        if len(string) >= char_limit:  # 23 or bigger string would cut the text out, for now just avoid it.
            raise TooManyCharsException("Diminue esse textão aí, pfv.")

        else:
            position = (x, y)
            img = Image.open(img_path)
            drawer = ImageDraw.Draw(img)
            drawer.text(position, string,
                        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
                        fill=color)

            drawer.text((desc_x, desc_y), description,
                        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=desc_font_size),
                        fill=color)

            response = requests.get(img_url, stream=True)
            img2 = Image.open(BytesIO(response.content))
            img2.thumbnail((img_width, img_height), Image.ANTIALIAS)
            img.paste(img2, (img_x, img_y))

            img.save(filename + ".png")
            return File(open(filename + ".png", "rb"))

    except Exception as e:
        puts.info(e)
        return None

def generate_card_twit(name: str, display_name: str, img_path: str, filename: str, img_url, description: str):
    try:

        if len(description) >= 50:
            raise TooManyCharsException("Diminue esse textão aí, pfv.")

        else:

            img = Image.open(img_path)
            drawer = ImageDraw.Draw(img)
            drawer.text((95, 30), name,
                        font=ImageFont.truetype(font='templates/fonts/helvetica.ttf', size=20),
                        fill=(0, 0, 0))

            drawer.text((90, 55), display_name,
                        font=ImageFont.truetype(font='templates/fonts/helvetica.ttf', size=18),
                        fill=(150, 150, 150))


            drawer.text((20, 100), description,
                        font=ImageFont.truetype(font='templates/fonts/helvetica.ttf', size=35),
                        fill=(0, 0, 0))

            response = requests.get(img_url, stream=True)

            img2 = Image.open(BytesIO(response.content))
            img2 = mask_circle_transparent(img2, 0)
            img2.thumbnail((60, 60), Image.ANTIALIAS)


            img.paste(img2, (20, 20), img2)

            img.save(filename + ".png")
            return File(open(filename + ".png", "rb"))

    except Exception as e:
        puts.info(e)
        return None

def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result
