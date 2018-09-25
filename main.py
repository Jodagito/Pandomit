import os
import parser

import pandas as pd


def file_converter(filename, expected_format):
    """Given a file returns a converted file to a preferred format"""
    read_methods = [method for method in dir(pd) if method[:4] == 'read']
    i = 0
    while os.path.exists("converted filename {}.".format(i) + expected_format.replace("to_", "") + ""):
        i += 1
    try:
        for method in read_methods[1:]:
            try:
                df = getattr(pd, method)(filename)
                df_converted = getattr(pd.DataFrame, expected_format)(df)
                if df_converted:
                    with open("converted filename {}.".format(i) + expected_format.replace("to_", "") + "", 'w') as converted_file:
                        converted_file.write(df_converted)
                    break
            except:
                continue
    except ValueError:
        print("This format can't be converted.")


if __name__ == "__main__":
    args = parser.arguments_parser()
    file_converter(args.filename, args.expectedformat)
