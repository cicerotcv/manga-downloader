
class FilenameFactory:
    def __init__(self):
        self.counter = 0

    def get_filename(self):
        filenumber = str(self.counter).zfill(4)  # supports up to 9999
        filename = f'{filenumber}'
        self.counter += 1
        return filename
