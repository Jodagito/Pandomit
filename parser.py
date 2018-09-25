import argparse

import pandas as pd


def arguments_parser():
    """Gets arguments passed by command line"""
    write_methods = [method for method in dir(
        pd.DataFrame) if method[:3] == 'to_' and method != 'to_clipboard']
    parser = argparse.ArgumentParser(description="File conversion")
    parser.add_argument('filename',
                        help='full name of the file to convert', action='store')
    parser.add_argument('expectedformat', choices=write_methods,
                        help='format to convert', action='store')
    args = parser.parse_args()
    return args
