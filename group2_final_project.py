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

## explore all the suspicious columns that may seem unique, all identified unique columns will be dropped from dataframe
print(data_group1_b['Index_'][0:50].value_counts())
print(data_group1_b['Hood_ID'][0:50].value_counts())
print(data_group1_b['ObjectId'][0:50].value_counts())
print(data_group1_b['event_unique_id'][0:50].value_counts())


##Get the count of all unique values for the Primary_Offence column
print(data_group1_b['Primary_Offence'].value_counts())

##Get the count of all unique values for the Bike_Type column
print(data_group1_b['Bike_Type'].value_counts())

##Get the count of all unique values for the Location_Type column
print(data_group1_b['Location_Type'].value_counts())

##Get the count of all unique values for the Division column
print(data_group1_b['Division'].value_counts())


## Checking the unique value counts for the Neighbourhood column
## Note for Group: there is 141 different values for this column, should we keep it 
print(data_group1_b['Neighbourhood'].value_counts())

##Get the count of all unique values for the Hood_ID column
print(data_group1_b['Hood_ID'].value_counts())




## Dropping all unique and repetitive variables that are useless for predictive analysis
data_group1_b = data_group1_b.drop(['X','Y','Index_', 'ObjectId', 'event_unique_id','Occurence_Date', 'City', 'Bike_Model', 'Bike_Make', 'Neighbourhood'], axis=1)
print(data_group1_b.shape)





## 1b - Statistical assessments  including means, averages, correlations

##Check the basic statistic details of all numeric columns
print(data_group1_b.describe())

## Print just the mean of all numeric values
print(data_group1_b.mean())

## Print the correlation of the entire dataframe
print(data_group1_b.corr())


#Check the mean of all numeric columns grouped by Bike_Type
print(data_group1_b.groupby('Bike_Type').mean())






## 1c - Missing data evaluations–use pandas, numpy and any other python packages

##examine the count statistic of all numeric variables
print(data_group1_b.count())

## Missing data evaluation using the isnull method
print(data_group1_b.isnull().sum())






## 1d - Graphs and visualizations–use pandas, matplotlib, seaborn, numpy and any other python packages, 
## also you can use power BI desktop.

## Plotting the frequency of Bike Thefts in each month using a histogram
import matplotlib.pyplot as plt
data_group1_b.Occurrence_Month.hist()
plt.title('Histogram of Month Of Occurence')
plt.xlabel('Month Of Occurence')
plt.ylabel('Frequency')

## Visualization using Seaborn
import seaborn as sns
sns.distplot(data_group1_b['Occurrence_Month'], rug=True, hist=False)

##sns.pairplot(data_group1_b)


## 2a - Data transformations includes missing data handling, categorical data management, 
## data normalization and standardizations as needed.

##missing data handling

##Get the count of all unique values for the Status column
print(data_group1_b['Status'].value_counts())

##delete all UNKNOWN values from the Status column
data_group1_b = data_group1_b[data_group1_b.Status != 'UNKNOWN']


##Print all rows from 100 to 149 of column Cost_of_Bike
data_group1_b['Cost_of_Bike'][100:150]

## Get the Cost_of_Bike average
print(data_group1_b['Cost_of_Bike'].mean())

## Get the mean of the Cost_of_Bike based on its Bike_Type
data_group1_b.groupby('Bike_Type').mean().Cost_of_Bike

## Replace missing values in the Cost_of_Bike column with its average based on Bike_Type
data_group1_b['Cost_of_Bike'] = data_group1_b['Cost_of_Bike'].fillna(data_group1_b.groupby('Bike_Type')['Cost_of_Bike'].transform('mean').round(2))

## Print all rows from 100 to 149 of column Cost_of_Bike after filling in the missing results
data_group1_b['Cost_of_Bike'][100:150]


print(data_group1_b['Bike_Model'].unique())

## Replace all categorical missing values with the value 'missing'.
print(data_group1_b.describe())
data_group1_b.fillna("missing",inplace=True)
data_group1_b[100:150]

##if we want to resort to deleting rows with missing values, use the following code

##data_group1_b.dropna(inplace=True)


##categorical data management
cat_vars=['']
for group1 in cat_vars:
    cat_list_group1='group1'+'_'+group1
    print(cat_list_group1)
    cat_list = pd.get_dummies(data_group1_b[group1], prefix=group1)
    data_group1_b_dummies = data_group1_b.join(cat_list_group1)
    data_group1_b = data_group1_b_dummies
    
# Remove the original columns
cat_vars=['']
data_group1_b_vars=data_group1_b.columns.values.tolist()
to_keep=[i for i in data_group1_b_vars if i not in cat_vars]
data_group1_b_final=data_group1_b[to_keep]
data_group1_b_final.columns.values

## Prepare for model build
data_group1_b_final_vars=data_group1_b_final.columns.values.tolist()
Y=['Our classifier'] ## I am thinking Bike_Type
X=[i for i in data_group1_b_final_vars if i not in Y ]
type(Y)
type(X)

## data normalization and standardizations
    
## 2b - Feature selection–use pandas and sci-kit learn.
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
## select 7 features from the RFE model
rfe = RFE(model, 7)
rfe = rfe.fit(data_group1_b_final[X],data_group1_b_final[Y] )
print(rfe.support_)
print(rfe.ranking_)

## Added selected features to X and classifier to Y
cols=[] 
X=data_group1_b[cols]
Y=data_group1_b['Our classifier'] ## I am thinking Bike_Type

## 2c - Training and testing data splits–use numpy, sci-kit learn

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
