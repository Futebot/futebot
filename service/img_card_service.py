from io import BytesIO

import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont
import logging as puts

from exception.exceptions import TooManyCharsException, FutebotException

from util.helpers import (
    create_discord_file_object,
    image_to_byte_array,
    save_image_to_imgur,
    validate_image,
)
from util.validators import validate_chars_limit


def generate_card(string: str, img_path: str, filename: str, font_size: int, x: int, y: int, color, char_limit,
                  font="opensans"):
    try:
        validate_chars_limit(string, char_limit)
        img = draw_text_on_image(color, font, font_size, img_path, string, x, y)
        return parse_to_slack_file(img)

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def draw_text_on_image(color, font, font_size, img_path, string, x, y):
    position = (x, y)
    img = Image.open(img_path)
    drawer = ImageDraw.Draw(img)
    drawer.text(
        position,
        string,
        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
        fill=color
    )
    return img


def generate_card_multiple_texts(img_path: str, filename: str, *texts: tuple):
    try:

        img = Image.open(img_path)
        drawer = ImageDraw.Draw(img)

        for text in texts:
            string = text[0]
            font_size = text[1]
            x = text[2]
            y = text[3]
            color = text[4]
            char_limit = text[5]
            font = text[6]

            validate_chars_limit(string, char_limit)

            position = (x, y)

            drawer.text(position, string,
                        font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
                        fill=color)

        return parse_to_slack_file(img)

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def generate_card_img(string: str, img_path: str, filename: str, font_size: int, x: int, y: int, color, char_limit,
                      img_url, img_x, img_y, img_width, img_height, font="opensans"):
    try:
        validate_chars_limit(string, char_limit)
        img = draw_text_on_image(color, font, font_size, img_path, string, x, y)
        add_thumbnail_to_img(img, img_height, img_url, img_width, img_x, img_y)

        return parse_to_slack_file(img)

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def generate_card_img_title_description(string: str, img_path: str, filename: str, font_size: int, x: int, y: int,
                                        color, char_limit, img_url, img_x, img_y, img_width, img_height,
                                        description: str, desc_x: int, desc_y: int, desc_font_size: int,
                                        font="opensans"):
    try:
        validate_chars_limit(string, char_limit)

        position = (x, y)
        img = Image.open(img_path)
        drawer = ImageDraw.Draw(img)
        drawer.text(position, string,
                    font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=font_size),
                    fill=color)

        drawer.text((desc_x, desc_y), description,
                    font=ImageFont.truetype(font='templates/fonts/' + font + '.ttf', size=desc_font_size),
                    fill=color)

        add_thumbnail_to_img(img, img_height, img_url, img_width, img_x, img_y)

        return parse_to_slack_file(img)

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def add_thumbnail_to_img(img, img_height, img_url, img_width, img_x, img_y):
    response = requests.get(img_url, stream=True)
    img2 = Image.open(BytesIO(response.content))
    img2.thumbnail((img_width, img_height))
    img.paste(img2, (img_x, img_y))


def generate_card_twit(name: str, display_name: str, img_path: str, filename: str, img_url, description: str):
    try:
        validate_chars_limit(description, 50)

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

        return parse_to_slack_file(img)

    except Exception as e:
        puts.info(e)
        raise FutebotException(e)


def parse_to_slack_file(img):
    img_url = save_image_to_imgur(image_to_byte_array(img))
    print("img url: " + img_url)
    return img_url


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result
