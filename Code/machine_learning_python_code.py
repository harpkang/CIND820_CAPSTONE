import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt


# Loading the data
data = pd.read_excel('dataset_lfs_2024.xlsx')

# Creating a profile report of the data
profile = ProfileReport(data, title="Profiling Report")

# Saving the profile report as an html file
profile.to_file("EDA of 100% of data.html")


print((data.head()))

print(data.info())

print(data.describe())

data.isnull().sum()
#there is no missing data in the dataset.

df=data.copy()

#df.info()

df.dropna(subset=["HRLYEARN"],inplace=True)
df['HRLYEARN']=df['HRLYEARN']/100
profile2 = ProfileReport(df, title="Profiling Report")
profile2.to_file("EDA after eliminating blanks of Usual Hourly Wages (HRLYEARN).html")

df['Usual hourly wages']=df['Usual hourly wages']/100

df["Bucket"]=df['Usual hourly wages'].apply(lambda x: '0-50' if x<=25.01 else  ('50-100' if x<=39.01  else '100+'))

df["Bucket"].value_counts(normalize=True)

df[['Usual hourly wages',"Bucket"]].head()