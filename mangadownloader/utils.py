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

        if auto_rotate:
            im_width = image.size[0]
            im_height = image.size[1]
            img_aspect = im_width / im_height
            if img_aspect > 1:
                image = image.rotate(90, expand=True)

        image.convert('RGB')
        image_list.append(image)

    image_list[0].save(f'{input_dir}.pdf', save_all=True,
                       append_images=image_list[1:])


def create_pdf_volume(base_dir, dir_prefix, output_name, auto_rotate=False):
    images_list = []

    folders = [folder for folder in os.listdir(
        base_dir) if folder.startswith(dir_prefix) and os.path.isdir(os.path.join(base_dir, folder))]

    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        for filename in os.listdir(folder_path):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            if auto_rotate:
                im_width = img.size[0]
                im_height = img.size[1]
                img_aspect = im_width / im_height
                if img_aspect > 1:
                    img = img.rotate(90, expand=True)
            img.convert("RGB")
            images_list.append(img)

    images_list[0].save(f'{output_name}.pdf', save_all=True,
                        append_images=images_list[1:])
