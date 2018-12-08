
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# 04_clean_data.py
# Ian Flores Siaca & Betty Zhou November 23, 2018
#
# This script trains the Decision Tree Classifier.
# This script takes the input file path, and the output file path.
#
# Dependencies: pandas, sklearn, argparse, numpy
#
# Usage:
# python 04_clean_data.py <input file> <output file>
# <input file> is the input csv.
# <output file> is the file name of the output csv.
# python 04_clean_data.py "data/san_francisco_features.csv" "data/feature_results.csv"


# In[5]:


# Loading the libraries to be used

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

import argparse


# In[3]:


# Adding support to use script from the CLI

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


# In[4]:


# Parsing the CLI input to use it on Python

input_file = args.input_file
output_file = args.output_file


# In[7]:

def main():
    sf_data = pd.read_csv(input_file)
    y = sf_data[['resolution']]
    X = sf_data.drop('resolution', axis = 1)


    # In[8]:


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.50)


    # In[9]:


    # Iterating thorugh different depths to find the optimal

    parameters = {'max_depth': np.arange(1, 30, 5)}

    tree = DecisionTreeClassifier(class_weight='balanced')
    clf = GridSearchCV(tree, parameters, cv=3)
    clf.fit(X_train, y_train)


    # In[10]:


    best_parameters = clf.best_params_


    # In[11]:


    # Training our model

    tree = DecisionTreeClassifier(
        class_weight='balanced', max_depth=best_parameters['max_depth'])

    tree.fit(X_train, y_train)


    # In[26]:


    accuracy = tree.score(X_test, y_test)


    # In[12]:


    feature_results = pd.DataFrame({
        'features': X.columns.tolist(),
        'feature_importance': tree.feature_importances_
    })

    feature_results = feature_results.sort_values(
        'feature_importance', ascending=False)
    feature_results = feature_results.query('feature_importance > 0.01')


    # In[27]:


    feature_results = pd.concat([pd.DataFrame({'features':['TEST_ACCURACY'],
                            'feature_importance' : [accuracy]}),
              feature_results])


    # In[ ]:


    feature_results.to_csv(output_file)

if __name__ == "__main__":
    main()