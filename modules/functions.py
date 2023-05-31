import os
import pathlib

workdir = os.path.abspath(os.getcwd())
data_path = pathlib.Path(workdir, "todos.txt")


def get_data(filepath: str = data_path):
    """
    Read a text file and return the list of to-do items.
    :param filepath: Path to a file to read from
    :return: list object
    """
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items


def update_data(items: list, filepath: str = data_path):
    """
    Write the to-do items list in the text file.
    :param filepath: str
    :param items: list
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(items)
