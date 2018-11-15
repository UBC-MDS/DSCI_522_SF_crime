##############################
# File Name: 01_load-data.R
# Author: Ian Flores
# Date: November 15, 2018
#
# This script loads into R the 
# San Francisco Crime dataset.
###############################

library(tidyverse)

app_token <- 'Z4iZ6NVV0wNPCeGxCLQVMEYMI'
api_limit <- 20000

base_url <- 'https://data.sfgov.org/resource/cuks-n6tp.csv?$$app_token='
sf_url <- paste0(base_url, app_token, '&$limit=', api_limit)
sf_data <- read_csv(sf_url)