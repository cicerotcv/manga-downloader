
import argparse


def parse_args():
    parser = argparse.ArgumentParser("Manga Downloader")
    parser.add_argument(dest='src', type=str)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--pdf', dest='to_pdf', action='store_true')
    parser.add_argument('--auto-rotate', dest='auto_rotate', default=False, action='store_true')
    return parser.parse_args()

def converter_parser():
    parser = argparse.ArgumentParser("Manga Downloader - Converter")
    parser.add_argument(dest='base_dir', default='.')
    parser.add_argument('-o', '--output', dest='output', default='.')
    parser.add_argument('--prefix', dest='dir_prefix', required=True)
    parser.add_argument('--auto-rotate', dest='auto_rotate', default=False, action='store_true')
    return parser.parse_args()
