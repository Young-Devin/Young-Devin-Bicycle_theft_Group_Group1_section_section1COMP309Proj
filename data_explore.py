# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:20:10 2019

@author: group1
"""

# 1 Data Exploration

# 1a - Load and describe data elements (columns) provide descriptions & types with values of each element.-
# use pandas, numpy and any other python packages
import pandas as pd
import os
from utils import save_print


def load_data():
    # path = "C:/Users/devin/Documents/COMP309/Bicycle_theft_Group_Group1_section_section1COMP309Proj/data"
    path = "D:/3. GitHubMirrorReps/Young-Devin-Bicycle_theft_Group_Group1_section_section1COMP309Proj/data"
    file_name = 'Bicycle_Thefts.csv'
    full_path = os.path.join(path, file_name)
    data_group1_b = pd.read_csv(full_path, sep=',')
    save_print('column values are:')
    save_print(data_group1_b.columns.values)
