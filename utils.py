# functions for common usage
from matplotlib import pyplot as plt


def save_print(msg, filename="output/text.txt"):
    with open(filename, "a") as f:
        print(msg, file=f)


def save_plt(plt_obj, filename):
    # not sure yet
    plt_obj.savefig(filename)



