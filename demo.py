from mangadownloader import MangaDownloader
from mangadownloader.cli import parse_args
from mangadownloader.utils import convert_to_pdf


def main():
    args = parse_args()
    # src is 'http://manganatos.com/manga-name-chapter'
    src = args.src
    verbose = args.verbose
    should_convert = args.to_pdf
    auto_rotate = args.auto_rotate
    interval = args.interval
    auto_skip = args.auto_skip

    md = MangaDownloader(src=src, interval=interval, verbose=verbose, auto_skip=auto_skip)
    md.download()

    if should_convert:
        convert_to_pdf(md.name, auto_rotate=auto_rotate)
        md.logger.log(f"PDF saved as '{md.name}.pdf'")


if __name__ == '__main__':
    main()
