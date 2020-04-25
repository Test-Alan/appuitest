import os

import yaml


def read_yaml(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
       return yaml.full_load(f)


if __name__ == '__main__':
    from settings import CAPS_DIR

    caps_path = os.path.join(CAPS_DIR, 'caps.yaml')
    a = read_yaml(CAPS_DIR)
    print(a)
    print(type(a))