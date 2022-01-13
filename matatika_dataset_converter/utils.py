"""Module containing utility functions for matatika-dataset-converter"""

from pathlib import Path


def make_dir_path_absolute(dir_path):
    dir_path = Path(dir_path).absolute()
    return dir_path


def clean_up_md_whitespace(file):
    data = None
    with open(file + ".md", "r") as file_in:
        data = file_in.read().splitlines(True)
    with open(file + ".md", "w") as file_out:
        file_out.writelines(data[3:])
