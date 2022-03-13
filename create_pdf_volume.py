from mangadownloader.cli import converter_parser
from mangadownloader.utils import create_pdf_volume


def main():
    args = converter_parser()
    base_dir = args.base_dir
    dir_prefix = args.dir_prefix
    auto_rotate = args.auto_rotate
    output = args.output
    create_pdf_volume(base_dir, dir_prefix, output, auto_rotate)


if __name__ == '__main__':
    main()
