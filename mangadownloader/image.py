import requests


class Image:
    def __init__(self, number, src):
        self.name = str(number).zfill(4)
        self.src = src
        self.type = None  # Image.get_type(response)
        self.blob = None  # response.content

    def download(self):
        response = requests.get(self.src)
        self.blob = response.content
        self.type = Image.get_type(response)

    @property
    def filename(self):
        return f'{self.name}.{self.type}'

    @staticmethod
    def get_type(response):
        content_type = response.headers['Content-Type']
        image_format = content_type.split('/')[1]
        return image_format
