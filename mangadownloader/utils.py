import os

from PIL import Image


def ensure_dir_exists(dir_name: str):
    if dir_name not in os.listdir('.'):
        os.mkdir(dir_name)


def get_full_path(output_dir, filename):
    return os.path.join(output_dir, filename)


def get_name(url: str):
    # url is  http://manganatos.com/manga-chapter-number
    parts = url.split('/')
    return parts[-1]


def convert_to_pdf(input_dir):
    image_list = []

    for filename in os.listdir(input_dir):
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)
        image.convert('RGB')
        image_list.append(image)

    image_list[0].save(f'{input_dir}.pdf', save_all=True,
                       append_images=image_list[1:])
