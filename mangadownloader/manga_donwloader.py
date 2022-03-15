import os
import time

import bs4
from itsdangerous import json
import requests

from .image import Image
from .logger import Logger
from .utils import ensure_dir_exists, get_full_path, get_name


class MangaDownloader:

    def __init__(self, src: str, name: str = None, interval=2, verbose=False, auto_skip=False):
        if name is None:
            name = get_name(src)

        self.src = src
        self.name = name
        self.interval = interval
        self.logger = Logger(verbose)
        self.auto_skip = auto_skip

    def download(self):
        html = MangaDownloader.download_page_html(self.src)
        self.logger.log(f"HTML parsed for '{self.src}'")
        img_array = MangaDownloader.get_img_array(html)
        print(json.dumps(img_array, indent=4))
        self.logger.log(f"Total pages {len(img_array)}")
        for number, img_src in enumerate(img_array):
            img = self._create_image(number, img_src)

            if self.should_skip(img.name):
                continue

            fp = MangaDownloader.store_image(self.name, img)
            self.logger.log(f"Image '{img.filename}' stored at '{fp}'")
            time.sleep(self.interval)

    def should_skip(self, img_name) -> bool:
        if not self.auto_skip:
            return False

        output_dir = os.path.join('.', self.name)
        if not os.path.exists(output_dir):
            return False

        for file in os.listdir(os.path.join('.', self.name)):
            filename = file.split('.')[0]
            if filename == img_name:
                self.logger.log(
                    f"Skipping image '{img_name}' for it's already downloaded")
                return True

        return False

    def _create_image(self, number, src) -> Image:
        return Image(number, src)

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
    def store_image(output_dir, img: Image):
        ensure_dir_exists(output_dir)
        img.download()
        full_path = get_full_path(output_dir, img.filename)
        with open(full_path, 'wb+') as file:
            file.write(img.blob)
        return full_path
