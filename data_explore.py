# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:20:10 2019

@author: group1
"""
# 1 Data Exploration
import pandas as pd
import numpy as np
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


# find duplicate columns or useless id column
def screen_cols(df):
    exclude_cols = []
    # check X -- Long is identical
    bool_x_long = df['X'].round(4).equals(df['Long'].round(4))
    save_print("Is col X and col Long identical? " + str(bool_x_long))
    if bool_x_long:
        save_print("Therefore remove col X")
        exclude_cols.append('X')

    # check Y -- Lat
    bool_y_lat = df['Y'].round(4).equals(df['Lat'].round(4))
    save_print("Is col Y and col Lat identical? " + str(bool_y_lat))
    if bool_y_lat:
        save_print("Therefore remove col Y")
        exclude_cols.append('Y')

    # check col Index is just id
    bool_is_index_id = df['Index_'].nunique() == len(df)
    save_print("Is col Index_ an id col? " + str(bool_is_index_id))
    if bool_is_index_id:
        save_print("Therefore remove col Index")
        exclude_cols.append('Index_')

    # check col event_unique_id is just id
    bool_is_event_uid_id = df['event_unique_id'].nunique() >= len(df) * 0.8
    save_print("Is col event_unique_id an id col? " + str(bool_is_event_uid_id))
    if bool_is_event_uid_id:
        save_print("Therefore remove col event_unique_id")
        exclude_cols.append('event_unique_id')

    # check col ObjectId is just id
    bool_is_obj_id = df['ObjectId'].nunique() == len(df)
    save_print("Is col ObjectId an id col? " + str(bool_is_obj_id))
    if bool_is_obj_id:
        save_print("Therefore remove col ObjectId")
        exclude_cols.append('ObjectId')

    # check City is all Toronto
    bool_is_city_all_toronto = df['City'].nunique() == 1
    save_print("Is col City only one value Toronto? " + str(bool_is_city_all_toronto))
    if bool_is_city_all_toronto:
        save_print("Therefore remove col City")
        exclude_cols.append('City')

    # check Bike_Make unique value
    bool_is_too_many_unique = df['Bike_Make'].nunique() >= 30
    save_print("Is col Bike_Make impossible to get dummy? " + str(bool_is_too_many_unique))
    if bool_is_too_many_unique:
        save_print("Therefore remove col Bike_Make")
        exclude_cols.append('Bike_Make')

    # check Bike_Model unique value
    bool_is_too_many_unique = df['Bike_Model'].nunique() >= 30
    save_print("Is col Bike_Model impossible to get dummy? " + str(bool_is_too_many_unique))
    if bool_is_too_many_unique:
        save_print("Therefore remove col Bike_Model")
        exclude_cols.append('Bike_Model')

    # check Bike_Colour unique value
    bool_is_too_many_unique = df['Bike_Colour'].nunique() >= 30
    save_print("Is col Bike_Colour impossible to get dummy? " + str(bool_is_too_many_unique))
    if bool_is_too_many_unique:
        save_print("Therefore remove col Bike_Colour")
        exclude_cols.append('Bike_Colour')

    # check Neighbourhood is one to one with Hood_ID
    bool_is_121 = len(df.groupby('Neighbourhood')['Hood_ID'].nunique().drop_duplicates()) == 1
    save_print('Is col Neighbourhood one to one with Hood_ID? ' + str(bool_is_121))
    if bool_is_121:
        save_print("Therefore remove col Neighbourhood")
        exclude_cols.append('Neighbourhood')

    # print all the removed columns
    save_print('\n***The columns will be removed are: ***')
    save_print(exclude_cols)
    return df[df.columns.difference(exclude_cols)]


def load_data():
    # prepare env
    del_output()
    pd.set_option('display.max_columns', 26)

    # 1a - Load and describe data elements (columns) provide descriptions & types with values of each element
    save_print('****1a output:****')
    # read from csv
    full_path = get_csv_full_path()
    data_group1_1a = pd.read_csv(full_path, sep=',')
    # col screen
    data_group1_1a = screen_cols(data_group1_1a)
    # print basic info to file
    print_basic_info(data_group1_1a)

    # 1b - Statistical assessments including means, averages, correlations

    # 1c - Missing data evaluations
    # 1d - Graphs and visualizations
    # return final df
    data_group1_after_step1 = data_group1_1a  # this dummy line needs replaced by previous pipeline results
    return data_group1_after_step1
