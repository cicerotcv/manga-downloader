class Image:
    def __init__(self, number, response):
        self.name = str(number).zfill(4)
        self.type = Image.get_type(response)
        self.blob = response.content
        self.filename = f'{self.name}.{self.type}'

    @staticmethod
    def get_type(response):
        content_type = response.headers['Content-Type']
        image_format = content_type.split('/')[1]
        return image_format
