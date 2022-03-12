from tabnanny import verbose
import requests
import bs4
import time

from .utils import ensure_dir_exists, get_full_path
from .filename_factory import FilenameFactory
from .logger import Logger


class MangaDownloader:

    def __init__(self, src: str, name: str, interval=2, verbose=False):
        self.src = src
        self.name = name
        self.interval = interval
        self.ff = FilenameFactory()
        self.logger = Logger(verbose)

    def download(self):
        html = MangaDownloader.download_page_html(self.src, self.logger)
        img_array = MangaDownloader.get_img_array(html, self.logger)
        for img_src in img_array:
            blob = MangaDownloader.download_image(img_src)
            fn = self.ff.get_filename()
            MangaDownloader.store_image(blob, self.name, fn, self.logger)
            time.sleep(self.interval)

    @staticmethod
    def download_page_html(src, logger):
        response = requests.get(src)
        raw_html = response.text
        logger.log(f"HTML parsed for '{src}'")
        return bs4.BeautifulSoup(raw_html, features="lxml")

    @staticmethod
    def get_img_array(parsed_html, logger):
        img_src_tag = parsed_html.find('p', {"id": "arraydata"})
        img_src_array = img_src_tag.text.split(',')
        logger.log(f"Total pages: {len(img_src_array)}")
        return img_src_array

    @staticmethod
    def download_image(src):
        response = requests.get(src)
        blob = response.content
        return blob

    @staticmethod
    def store_image(blob, output_dir, filename, logger):
        ensure_dir_exists(output_dir)
        f_path = get_full_path(output_dir, filename)
        logger.log(f"Image stored at {f_path}")
        with open(f_path, 'wb+') as file:
            file.write(blob)
