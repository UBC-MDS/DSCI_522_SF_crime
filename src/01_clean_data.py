
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# 01_clean_data.py
# Ian Flores Siaca November 23, 2018
#
# This script downloads the data from the SF portal API, cleans it, and saves it as a CSV file.
# This script takes the number of cases to be requested, and the output file path.
#
# Dependencies: pandas, numpy, argparse, pendulum
#
# Usage: python 01_clean_data.py "300000" "data/san_francisco_clean.csv"


# In[10]:


# Loading the libraries to be used

import pandas as pd
import numpy as np
import pendulum

import argparse


# In[11]:


# Adding support to use script from the CLI

parser = argparse.ArgumentParser()
parser.add_argument('api_limit')
parser.add_argument('output_file')
args = parser.parse_args()


# In[ ]:


# Parsing the CLI input to use it on Python
api_limit = int(args.api_limit)
out_file = args.output_file


# In[3]:


# Downloading the data from the SF portal API

app_token = 'Z4iZ6NVV0wNPCeGxCLQVMEYMI'

base_url = 'https://data.sfgov.org/resource/cuks-n6tp.csv?$$app_token='
sf_url = base_url + app_token + '&$limit=' + str(api_limit)

sf_data = pd.read_csv(sf_url)

sf_data = sf_data[['category', 'date', 'dayofweek', 'descript',
                    'pddistrict',
                    'resolution', 'time', 'x', 'y']]


# In[4]:


# Extracting month and day of incident to be used as features

parse_dates = np.vectorize(pendulum.parse)
sf_dates = parse_dates(sf_data.date)

months = []
days = []

for date in sf_dates:
    months.append(date.month)
    days.append(date.day)
    
sf_data['report_month'] = months
sf_data['report_day'] = days


# In[5]:


# Extracting time as minutes from midnight to have a continous feature. 

sf_times = parse_dates(sf_data.time)

times = []

for time in sf_times:
    times.append(time.hour*60 + time.minute)

sf_data['time'] = times

sf_data = sf_data[['category', 'dayofweek', 
         'descript','pddistrict',
         'resolution', 'time', 
         'x', 'y', 'report_month', 'report_day']]


# In[6]:


# Recoding our labels

sf_data = sf_data.replace({'resolution': 
                 ['NONE', 'CLEARED-CONTACT JUVENILE FOR MORE INFO',
                  'UNFOUNDED', 'JUVENILE ADMONISHED','EXCEPTIONAL CLEARANCE', 
                  'JUVENILE DIVERTED']}, 'non_processed')

sf_data = sf_data.replace({'resolution': 
                 ['ARREST, BOOKED', 'ARREST, CITED', 'NOT PROSECUTED', 
                  'PSYCHOPATHIC CASE', 'JUVENILE CITED', 'JUVENILE BOOKED', 'LOCATED',
                  'PROSECUTED BY OUTSIDE AGENCY', 'COMPLAINANT REFUSES TO PROSECUTE',
                  'DISTRICT ATTORNEY REFUSES TO PROSECUTE', 'PROSECUTED FOR LESSER OFFENSE']}, 'processed')


# In[9]:


sf_data.to_csv(out_file, index_label=False, index=False)

