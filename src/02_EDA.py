
# coding: utf-8

# In[48]:


#!/usr/bin/env python
# EDA.py
# Betty Zhou, November 23, 2018
#
# This script generates exploratory data analysis figures such as bar graphs for 
# categorical variables and histograms for continuous variables. This script takes 
# a clean .csv file and an output file path as the variable arguments. 
#
# Dependencies: argparse, pandas, numpy, seaborn, matplotlib
#
# Usage: python EDA.py "clean_sf_data.csv" "results/figures/"

import argparse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[57]:


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    
    #read input file
    sf_data = pd.read_csv(args.input_file)
    
    # Checking imbalances in target classes
    sns.countplot(data=sf_data, x='resolution')
    plt.savefig(args.output_file + str('target') + "_plot.png")
    plt.close()
    
    # Create plot for categorical features
    X_features = {'category': 'Category',
                  'pddistrict': 'Police District', 
                  'dayofweek' : "Day of week",
                  'report_month' : 'Month of Incident Report',
                  'report_day' : 'Day of Incident Report'}
    for i in X_features:
        cat_plot(sf_data, i)
        plt.xlabel(X_features[i])
        plt.tight_layout()
        plt.savefig(args.output_file + str(i) + "_plot.png")
        plt.close()
    
    # Histogram for longitude
    plot_his_bins(sf_data, 'x', 'longitude', 200)
    # Histogram for latitude
    plot_his_bins(sf_data, 'y', 'latitude', 30)
    # Histogram for time
    plot_his_bins(sf_data, 'time', 'time (mins from midnight)', 40)

def cat_plot(sf_data, feature):
    '''
    Create bar plot for categorical features
    '''
    graph = sns.countplot(data=sf_data, x= feature , hue='resolution', order = sf_data[feature].value_counts().index)
    graph.set_xticklabels(graph.get_xticklabels(), rotation=90)
    sns.set(rc={'figure.figsize':(10,5)})
    plt.legend(loc="upper right")

def plot_his_bins(sf_data, feature, xlabel, binsize):
    fig = plt.figure(figsize=(10,5))
    NP = sf_data[sf_data['resolution']=='non_processed'][feature]
    P = sf_data[sf_data['resolution']=='processed'][feature]
    NP.hist(alpha = 0.70, bins = binsize, label='non_processed')
    P.hist(alpha = 0.70, bins = binsize, label='processed')
    plt.legend(loc="upper right")
    plt.xlabel(xlabel)
    plt.ylabel("count")
    plt.tight_layout()
    plt.savefig(args.output_file + str(feature) + "_plot.png")
    plt.close()

if __name__ == "__main__":
    main()

