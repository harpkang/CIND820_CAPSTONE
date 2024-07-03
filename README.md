
# CIND820 Capstone Project

# Author
Harpreet Kang

# Contents of the Repository
The following summary is given for the repository folders. 

1. Abstract - Contains only the abstract from the first phase of the project. 
2. Code - Contains the an excel version of the dataset along with the python code in an .ipynb file. It also contains an html version of the .ipynb file. 
3. Dataset - Contains the data dictionary, list of variables, a link to the actual online dataset, and an excel version of the dataset. 
4. Figures - Contains all the figures used in the report. 
5. Initial Code- Contains the report from the third phase of the project, the GitHub link, and a link to the dataset online. 
6. Literature Review, Data Description, and Approach - This contains the report that was written for the second phase of the project.
7. Y Profile Reports - Contains many profile reports for EDA. 

# Dataset

The dataset used for this research project is an aggregation of Labour Force Surveys from between January 2024 and April 2024. This dataset is published monthly by Statistics Canada, and it can be downloaded by using the following link:

https://www150.statcan.gc.ca/n1/pub/71m0001x/71m0001x2021001-eng.htm

It can also be found in the 'Code' folder in the repository (along with the .ipynb file).

# Problem Statement

What machine learning models can be used to predict an individual's wage with minimum error.

### Research Questions

1. Which classification model, with tuned hyper parameters, will have a high accuracy and f1-score, and balanced precision and recall?

    [Example Notebook - Classification](https://github.com/harpkang/CIND820_CAPSTONE/blob/main/Code/kang_harpreet_code_cind820.ipynb#Classification)

2. What do data mining techniques, specifically association rules, reveal about the link between a high education level and above average hourly earnings?

3. Which non-linear regression model, with tuned hyper parameters, will have a strong RMSE in regard to the continuous response variable?

# Preparing the Dataset

### Training & Testing Set
The dataset was split into a training and testing set

### Feature Selection Techniques:
1. Addressing Missing Data
2. Addressing Low Variance
3. Addressing Correlation

### Normality
The response variable, hourly earnings, and two other other features used for machine learning were not normally distributed. To address the positively skewed dependent variable it was log transformed. 

### Assumptions of Linear Regression
Assumptions of Linear Regression were not upheld. The Homoscedasticity test was the only one that failed. 

### Outliers
The IQR was used to remove the outliers from quantitative features. 

### Log Transformation
The dependent variable was log transformed. 

### Standardization
MinMaxScaler() was used to standardize the continuous independent variables.

### Bins
Balanced bins of 5 were created, using a quantile strategy, for the continuous features for both the classification models and the apriori algorithm. In addition, for apriori algorithm only, the continuous target attribute was categorized into 5 balanced bins using the quantile strategy. 

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
Initial results using default settings indicated that Random Forest for both classification and non-linear regression had the best score. 

Education is the most positively associated feature that generates above average earnings in terms of association rules. 

# Statistical Tools

1. Friedman Test is used to evaluate classification models
2. Kruskal-Wallis Test is used to evaluate non-linear regression models. 

# Hyper Tuning
A Randomized Grid Search will be used to fine tune the model, and will also use K-Folds. 

# Conclusion
