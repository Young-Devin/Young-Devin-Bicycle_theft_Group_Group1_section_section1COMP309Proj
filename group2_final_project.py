# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:20:10 2019

@author: group1
"""

## 1 Data Exploration

## 1a - Load and describe data elements (columns) provide descriptions & types with values of each element.-
##use pandas, numpy and any other python packages
import pandas as pd
import os
path = "C:/Users/devin/Documents/COMP309/Bicycle_theft_Group_Group1_section_section1COMP309Proj/data"
filename = 'Bicycle_Thefts.csv'
fullpath = os.path.join(path,filename)
data_group1_b = pd.read_csv(fullpath,sep=',')
print(data_group1_b.columns.values)
print(data_group1_b.shape)
print(data_group1_b.describe())
print(data_group1_b.dtypes) 

## Set pd to display all columns, as there is only 26 columns. 
pd.set_option('display.max_columns',26)

## Print the first 20 rows of the data_group1_b dataframe
print(data_group1_b.head(20))

## Print the first 30 and last 30 rows of the data_group1_b dataframe
print(data_group1_b.describe)


## 1b - Statistical assessments  including means, averages, correlations

##Check the basic statistic details of all numeric columns
print(data_group1_b.describe())

#Check the mean of all numeric columns grouped by Bike_Type
print(data_group1_b.groupby('Bike_Type').mean())



## 1c - Missing data evaluations–use pandas, numpy and any other python packages


print(data_group1_b.describe())

## Get the Cost_of_Bike average
print(data_group1_b['Cost_of_Bike'].mean())

## Replace missing values in the Cost_of_Bike column with its average
data_group1_b['Cost_of_Bike'].fillna(data_group1_b['Cost_of_Bike'].mean(),inplace=True)

##Print all rows from 100 to 149 of column Cost_of_Bike
data_group1_b['Cost_of_Bike'][100:150]


print(data_group1_b.describe())
data_group1_b.fillna("missing",inplace=True)
data_group1_b[100:150]





## 1d - Graphs and visualizations–use pandas, matplotlib, seaborn, numpy and any other python packages, 
## also you can use power BI desktop.

## Plotting the frequency of Bike Thefts in each month using a histogram
import matplotlib.pyplot as plt
data_group1_b.Occurrence_Month.hist()
plt.title('Histogram of Month Of Occurence')
plt.xlabel('Month Of Occurence')
plt.ylabel('Frequency')