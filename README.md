# San Francisco Crime Data
# Collaborators:

- [Betty Zhou](https://github.com/bettybhzhou)
- [Ian Flores](https://github.com/ian-flores)

# Dataset

- [Link to San Francisco crime data website](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry)
- [Link to R script for downloading dataset](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.R)
- [Link to Python script for downloading dataset](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.py)

# Research Question

What are the strongest predictors for whether a crime instance in San Francisco resulted in an arrest?

This question is a predictive question.

# Objective

The goal of our project is to implement a classification of the San Francisco crime data with a decision tree. 

The following table outlines the features we will be using to build the classifier:

<center>
  
| Feature | Feature Type |
|---|---|
| Category | Categorical |
| Description | Categorical |
| Day of week | Categorical |
| Time | Continuous|
| Police District | Categorical |
| Longitude | Continuous |
| Latitude | Continuous |

</center>

The final target response variable is resolution, which consist of 2 classes: "arrested" and "not arrested".

# Analysis Plan

1. Since our dataset is very skewed towards one of the classes, we will recode our target response variables from 17 classes to only 2 classes to obtain a 2:1 imbalance in our final classes. The final target response variables will be "arrested" and "not arrested".

2. We will use scikit-learn LabelEncoder and CountVectorizer to pre-process the categorical features. CountVectorizer will be used to create frequencies of words in the `Description` feature of crime instances and LabelEncoder to encode class levels for the `Category`, `Day of week` and `Police District` categorical features.

3. Since we have over 2 million observations in our dataset, we will split our dataset into training and validation sets at a 50:50 ratio.

3. scikit-learn will be used to train the model.

# Summary of results

We will summarize our data by reporting a table of the strongest predictors for whether a crime instance in San Francisco resulted in an arrest. The strongest predictors are the predictors that show up earlier in our decision tree as these predictors are chosen by the algorithm as the best predictors for the target classes. We will also report a classification error of our model. Finally, the report will include a graphviz plot of our decision tree. 

