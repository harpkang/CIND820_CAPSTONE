
# CIND820 Capstone Project

# Author
Harpreet Kang

# Contents of the Repository
The following summary is given for the repository folders. 

1. [Abstract](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Abstract) - Contains only the abstract from the first phase of the project. 
2. [Code](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Code) - Contains the an excel version of the dataset along with the python code in an .ipynb file. It also contains an html version of the .ipynb file. 
3. [Dataset](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Dataset) - Contains the data dictionary, list of variables, a link to the actual online dataset, and an excel version of the dataset. 
4. [Figures](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Figures) - Contains all the figures used in the report. 
5. [Initial Code](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Initial%20Code)- Contains the report from the third phase of the project, the GitHub link, and a link to the dataset online. 
6. [Literature Review, Data Description, and Approach](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Literature%20Review%2C%20Data%20Description%2C%20and%20Approach) - This contains the report that was written for the second phase of the project.
7. [Y Profile Reports](https://github.com/harpkang/CIND820_CAPSTONE/tree/main/Y%20Profling%20Reports) - Contains many profile reports for EDA. 

# Dataset

The dataset used for this research project is an aggregation of Labour Force Surveys from between January 2024 and April 2024. This dataset is published monthly by Statistics Canada, and it can be downloaded by using the following link:

https://www150.statcan.gc.ca/n1/pub/71m0001x/71m0001x2021001-eng.htm

It can also be found in the 'Code' folder in the repository (along with the .ipynb file).

# Problem Statement

What machine learning models can be used to predict an individual's wage with minimum error.

### Research Questions

1. Which [classification model](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Classification), with tuned hyper parameters, will have a high accuracy and f1-score, and balanced precision and recall?


2. What do data mining techniques, specifically [association rules](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Apriori-Algorithm), reveal about the link between a high education level and above average hourly earnings?


4. Which [non-linear regression model](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Non-Linear-Regression), with tuned hyper parameters, will have a strong RMSE in regard to the continuous response variable?


# Understanding the Dataset
The following are the Y Profile Reports, generated in PDF, in various stages of preparing the data. The HTML versions of the reports are in the Y Profling Reports Data. 

1.	[EDA - Profiling Report (As is)](https://github.com/harpkang/CIND820_CAPSTONE/blob/main/Y%20Profling%20Reports/Profiling%20Report%20(As%20is).pdf)
2. [EDA -  Profiling Report (After Removing Low Variance and Missing Values)](https://github.com/harpkang/CIND820_CAPSTONE/blob/main/Y%20Profling%20Reports/Profiling%20Report%20(After%20Removing%20Low%20Variance%20and%20Missing%20Values).pdf) 
3. [EDA - Profiling Report (After Removing Correlated Items)](https://github.com/harpkang/CIND820_CAPSTONE/blob/main/Y%20Profling%20Reports/Profiling%20Report%20(After%20Removing%20Correlated%20Items).pdf )

# Preparing the Dataset

### Training & Testing Set
The dataset was split into a [training and testing](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Splitting-the-Data-into-Training-and-Testing) set

### Feature Selection Techniques:
1. Addressing [Missing Data](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Feature-Selection:-Missing-Values-)
2. Addressing [Low Variance](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Feature-Selection:-Low-Variance-)
4. Addressing [Correlation](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Feature-Selection:-Correlation-Analysis)
### Normality
The response variable, hourly earnings, and two other other features used for machine learning were not [normally distributed](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Checking-for-Normality). To address the positively skewed dependent variable, it was [log transformed](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Log-Transform-the-Dependent-Value). 


### Assumptions of Linear Regression
[Assumptions of Linear Regression](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Linearity-Assumptions-Tested) were not upheld. The Homoscedasticity test was the only one that failed. 

### Outliers
The IQR was used to remove the [outliers](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Outlier-Detection-using-IQR) from quantitative features. 

### Log Transformation
The dependent variable was [log transformed](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Log-Transform-the-Dependent-Value). 

### Standardization
MinMaxScaler() was used to standardize the continuous independent variables using the column transformer ingested into the pipeline in both the classification and non-linear regression machine learning models. Please use the hyperlinks above to navigate to the the respective models. 

### Bins
Balanced [bins](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#--Apriori-Pre-Processing) of 5 were created, using a quantile strategy, for the continuous features for both the classification models and the apriori algorithm. In addition, for apriori algorithm only, the continuous target attribute was categorized into 5 balanced bins using the quantile strategy. 

### Sklearn Functions
A host of functions were used to manipulate the data and to make sure there was no data leakage. 
1. Hot Ones Encoding
2. Column Transformer
3. Pipeline

# Approach

To answer the three research questions outlined. Three different methodologies were used. 
1. Classification Models:
    1. Random Forest
    2. Decision Tree
    3. XGBoost
    4. SVC
    5. Logistic Regression
    6. MultinomialNB
    
2. Association Rules: Apriori 

3. Non-Linear Regression Models:
    1. Random Forest
    2. Support Vector
    3. XGBoost
    4. KNN
    5. Regression Tree
     

## Initial Results
Initial results using default settings indicated that Random Forest for both [classification](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#--Classification-Base-Models) and [non-linear regression](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Non-Linear-Base-Models-without-Hyper-Tuning) had the best score. 

Education is the most positively associated feature that generates above average earnings in terms of association rules. 

# Statistical Tools

1. [Friedman Test](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#--Friedman-Test-for-Classification) is used to evaluate classification models
2. [Kruskal-Wallis Test](https://nbviewer.org/github/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#--Kruskal-Wallis-Test-for-Non-Linear-Regression) is used to evaluate non-linear regression models. 

# Hyper Tuning
A Randomized Grid Search will be used to fine tune the model, and will also use K-Folds. 

# Conclusion
