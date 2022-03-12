import time

import bs4
import requests

from .filename_factory import FilenameFactory
from .image import Image
from .logger import Logger
from .utils import ensure_dir_exists, get_full_path, get_name


class MangaDownloader:

    def __init__(self, src: str, name: str = None, interval=2, verbose=False):
        if name is None:
            name = get_name(src)

        self.src = src
        self.name = name
        self.interval = interval
        self.ff = FilenameFactory()
        self.logger = Logger(verbose)

    def download(self):
        html = MangaDownloader.download_page_html(self.src)
        self.logger.log(f"HTML parsed for '{self.src}'")
        img_array = MangaDownloader.get_img_array(html)
        self.logger.log(f"Total pages {len(img_array)}")
        for number, img_src in enumerate(img_array):
            img = self._get_image(number, img_src)
            fp = MangaDownloader.store_image(self.name, img.filename, img.blob)
            self.logger.log(f"Image '{img.filename}' stored at '{fp}'")
            time.sleep(self.interval)

    def _get_image(self, number, src) -> Image:
        response = requests.get(src)
        image = Image(number, response)
        return image

    @staticmethod
    def download_page_html(src):
        response = requests.get(src)
        raw_html = response.text
        return bs4.BeautifulSoup(raw_html, features="lxml")

    @staticmethod
    def get_img_array(parsed_html):
        img_src_tag = parsed_html.find('p', {"id": "arraydata"})
        img_src_array = img_src_tag.text.split(',')
        return img_src_array

    @staticmethod
    def store_image(output_dir, filename, blob):
        ensure_dir_exists(output_dir)
        full_path = get_full_path(output_dir, filename)
        with open(full_path, 'wb+') as file:
            file.write(blob)
        return full_path
