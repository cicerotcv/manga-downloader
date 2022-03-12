
import argparse


def parse_args():
    parser = argparse.ArgumentParser("Manga Downloader")
    parser.add_argument(dest='src', type=str)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--pdf', dest='to_pdf', action='store_true')
    parser.add_argument('--auto-rotate', dest='auto_rotate',
                        default=False, action='store_true')
    return parser.parse_args()
