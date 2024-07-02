# CIND820 Capstone Project

# Author
Harpreet Kang

# Dataset

The dataset used for this research project is an aggregation of Labour Force Surveys from between January 2024 and April 2024. This dataset is published monthly by Statistics Canada, and it can be downloaded by using the following link:

https://www150.statcan.gc.ca/n1/pub/71m0001x/71m0001x2021001-eng.htm

It can also be found in the 'Code' folder in the repository (along with the .ipny file).

# Problem Statement

What machine learning models can be used to predict an individuals wage with minimum error.

### Research Questions
1. Which classification model, with tuned hyper parameters, will have a high accuracy?

2. What do data mining techniques, specifically association rules, reveal about the data?

3. Which non-linear regression model, with tuned hyper parameters, will have a strong RMSE?

# Preparing the Dataset

### Feature Selection Techniques:
1. Addressing Missing Data
2. Addressing Low Variance
3. Addressing Correlation

### Normality
The response variable, hourly earnings, and two other other features used for machine learning were not normally distributed. To address the positively skewed dependent variable it was log transformed. 

### Assumptions of Linear Regression
Assumptions of Linear Regression were not up held. The Homoscedasticity test was the only that failed. 

### Outliers
The IQR was used to remove the outliers from quantitative features. 

# Approach

To answer the three research questions outlined. Three different methodologies were used. 
1. Classification Models
2. Association Rules
3. Non-Linear Regression Models

# Conclusion
