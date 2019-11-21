# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:20:10 2019

@author: group1
"""
# 1 Data Exploration
import pandas as pd
from utils import save_print, del_output, get_csv_full_path


def print_basic_info(df):
    save_print('\n****column values are:****')
    save_print(df.columns.values)
    save_print('\n****column shape are:****')
    save_print(df.shape)
    save_print('\n****column describe are:****')
    save_print(df.describe())
    save_print('\n****column type are:****')
    save_print(df.dtypes)
    save_print('\n****top 5 rows are:****')
    save_print(df.head(5))


def load_data():
    # prepare env
    del_output()
    pd.set_option('display.max_columns', 26)

    # 1a - Load and describe data elements (columns) provide descriptions & types with values of each element
    save_print('****1a output:****')
    # read from csv
    full_path = get_csv_full_path()
    data_group1_b = pd.read_csv(full_path, sep=',')

    # print basic info to file
    print_basic_info(data_group1_b)

    # 1b - Statistical assessments including means, averages, correlations
    # 1c - Missing data evaluations
    # 1d - Graphs and visualizations
    # return final df
    data_group1_after_step1 = data_group1_b  # this dummy line needs replaced by previous pipeline results
    return data_group1_after_step1
