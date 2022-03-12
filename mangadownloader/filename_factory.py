
class FilenameFactory:
    def __init__(self, ext='png'):
        self.ext = ext
        self.counter = 0

    def get_filename(self):
        filenumber = str(self.counter).zfill(4)  # supports up to 9999
        filename = f'{filenumber}.{self.ext}'
        self.counter += 1
        return filename
