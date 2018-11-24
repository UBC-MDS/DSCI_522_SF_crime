# San Francisco Crime Data
Collaborators:

|Name| github.com |
|---|---|
|Betty Zhou |[@bettybhzhou](https://github.com/bettybhzhou)|
|Ian Flores |[@ian-flores](https://github.com/ian-flores)|

# Project Overview

## Objective  
The goal of this project is to implement a classification of the San Francisco crime data with a decision tree to predict the resolution of a crime instance. The resolution of a crime instance can be either "processed" or "non-processed". Processed indicates that a crime instance resulted in a subject being processed into the police system.

This project will address the following predictive question:  
What are the strongest predictors for whether a crime instance in San Francisco resulted in an arrest?

# Dataset

The dataset contains San Francisco crime data from 2003 to May 2018 with each crime instance having the following features: incident ID, category of crime, description of crime, day of week of incident, date of incident, time of incident, police district, resolution of incident, address, longitude, latitude and location of incident.

The dataset can be found at the following link:  
- [Link to San Francisco crime data website](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry)

The dataset can be loaded using this [R script](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.R)
or this [Python script](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.py). The following is a preview of the dataset in R:



# Objective

The goal of our project is to implement a classification of the San Francisco crime data with a decision tree. 


The final target response variable is resolution, which consist of 2 classes: "arrested" and "not arrested".

# Analysis Plan

1. Since our dataset is very skewed towards one of the classes, we will recode our target response variables from 17 classes to only 2 classes to obtain a 2:1 imbalance in our final target classes. The final target response variables will be "processed" and "non-processed".

2. The following table outlines the features that will be used as predictors to build the classifier:

| Feature | Feature Type |
|---|---|
| Category | Categorical |
| Description | Categorical |
| Day of week | Categorical |
| Time | Continuous|
| Police District | Categorical |
| Longitude | Continuous |
| Latitude | Continuous |

The categorical predictors will be pre-processed using 2 method. The category, day of week and police district predictors will be converted into dummy variables using `pandas.get_dummies`. The description predictor will be pre-processed using `sklearn.feature_extraction.text.CountVectorizer` to extract the 50 most common descriptions, which will be used as predictors to build the classifier. 

3. Since we have over 2 million observations in our dataset, we will randomly split our dataset into training and validation sets at a 50:50 ratio using `sklearn.model_selection.train_test_split.

3. `sklearn.tree.DecisionTreeClassifier` will be used to train the model. To combat the imbalance in our target classes, we will use the argument `class_weight = 'balanced` within the DecisionTreeClassifier. We will use 10-fold cross-validation on our training set to find the optimal max_depth and min_samples_split to train our model. The optimal max_depth and min_samples_split hyperparameters will be used to build the final model. Finally, the accuracy of the model will be determined using the validation set.

4. The Scikit learn `feature_importances_` attribute returns the Gini importance of each feature and will be used to determine the strongest predictors for the target classes. The strongest predictors are the predictors with the highest feature_importance.

# Summary of Results

We will summarize our data by reporting a table of the strongest predictors for whether a crime instance in San Francisco resulted in a processed or non-processed resolution. The summary table will include the top predictors and their feature importance values. Finally, the report will include the validation accuracy of our model.

# Analysis Pipeline. 
## Usage:

## Dependencies:
- R $ R libraries
  - `rmarkdown`  
  - `knitr`  
  - `tidyverse`  
  - `ggmap`  
  - `maps`  

- Python & Python libraries:
  - `matplotlib`
  - `numpy`
  - `seaborn`
  - `pandas`
  - `argparse`

