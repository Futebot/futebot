import requests

from commands.config import (
    IMGUR_CLIENT_ID,
    IMGUR_CLIENT_SECRET,
)


class Imgur:
    def __init__(self):
        self.headers = {
            'Authorization': 'Client-ID {}'.format(IMGUR_CLIENT_ID)
        }
        self.upload_endpoint = 'https://api.imgur.com/3/image'

    def upload(self, image):
        payload = {
            'image': image
        }
        response = requests.request(
            'POST',
            self.upload_endpoint,
            headers=self.headers,
            data=payload
        )
        print(response.json())
        return response.json()['data']['link']
