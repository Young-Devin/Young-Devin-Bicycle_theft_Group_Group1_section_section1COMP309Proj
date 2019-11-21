# functions for common usage
# from matplotlib import pyplot as plt
import os
import shutil
from os.path import dirname, join


project_root = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


def save_print(cmd, filename="output/text.txt"):
    with open(filename, "a") as f:
        print(cmd, file=f)


def save_plt(plt_obj, filename):
    # tbd: not sure yet
    plt_obj.savefig(filename)


def del_output():
    output_path = join(project_root, 'output')
    print("dbg output_path: " + output_path)
    for the_file in os.listdir(output_path):
        file_path = os.path.join(output_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def get_csv_full_path():
    file_name = 'Bicycle_Thefts.csv'
    data_path = join(project_root, 'data')
    return join(data_path, file_name)

