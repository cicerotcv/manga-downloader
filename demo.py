from mangadownloader import MangaDownloader
from mangadownloader.cli import parse_args
from mangadownloader.utils import convert_to_pdf


def main():
    args = parse_args()
    # src is 'http://manganatos.com/manga-name-chapter'
    src = args.src
    verbose = args.verbose
    should_convert = args.to_pdf
    md = MangaDownloader(src=src, interval=1, verbose=verbose)
    md.download()
    if should_convert:
        convert_to_pdf(md.name)
        md.logger.log(f"PDF saved as '{md.name}.pdf'")


if __name__ == '__main__':
    main()
