import os


def ensure_dir_exists(dir_name: str):
    if dir_name not in os.listdir('.'):
        os.mkdir(dir_name)


def get_full_path(output_dir, filename):
    return os.path.join(output_dir, filename)
