
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# 03_clean_data.py
# Ian Flores Siaca November 23, 2018
#
# This script extracts and formats the features necessary for the Decision Tree Classifier.
# This script takes the input file path, and the output file path.
#
# Dependencies: pandas, sklearn, argparse
#
# Usage: python 03_clean_data.py "data/san_francisco_clean.csv" "data/san_francisco_features.csv"


# In[11]:


# Loading the libraries to be used

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

import argparse


# In[ ]:


# Adding support to use script from the CLI

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


# In[ ]:


# Parsing the CLI input to use it on Python

input_file = args.input_file
output_file = args.output_file


# In[13]:


# One Hot Encoding the cateogrical variables

sf_data = pd.read_csv(input_file)
sf_data = pd.get_dummies(
    sf_data,
    columns=[
        'category', 'dayofweek', 'pddistrict', 'report_month', 'report_day'
    ])


# In[15]:


# Extracting the words in the descript column to be used as features

cv = CountVectorizer(max_features=50, stop_words='english')
description_features = cv.fit_transform(sf_data.descript).toarray()

description_features_df = pd.DataFrame(
    description_features, columns=sorted(cv.vocabulary_), index=sf_data.index)


# In[17]:


sf_data = pd.merge(
    sf_data, description_features_df, left_index=True, right_index=True)


# In[18]:


sf_data = sf_data.drop('descript', axis=1)


# In[20]:


sf_data.to_csv(output_file, index_label=False, index=False)

