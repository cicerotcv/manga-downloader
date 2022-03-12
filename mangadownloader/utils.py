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


def convert_to_pdf(input_dir, auto_rotate=False):
    image_list = []

    for filename in os.listdir(input_dir):
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        im_width = image.size[0]
        im_height = image.size[1]
        img_aspect = im_width / im_height

        if auto_rotate and img_aspect > 1:
            image = image.rotate(90, expand=True)

        image.convert('RGB')
        image_list.append(image)

    image_list[0].save(f'{input_dir}.pdf', save_all=True,
                       append_images=image_list[1:])
