# San Francisco Crime Data
Collaborators:

|Name| github.com |
|---|---|
|Betty Zhou |[@bettybhzhou](https://github.com/bettybhzhou)|
|Ian Flores |[@ian-flores](https://github.com/ian-flores)|

# Project Overview

## Objective  
The goal of this project is to implement a classification of the San Francisco crime data with a decision tree to predict the resolution of a crime instance. The resolution of a crime instance can be either "processed" or "non-processed". Processed indicates that a crime instance resulted in a subject being processed into the justice system. The following table outlines crime resolutions that were classified as processed or non-processed:

| Non-Processed                          | Processed                              |
|----------------------------------------|----------------------------------------|
| NONE                                   | ARREST, BOOKED                         |
| CLEARED-CONTACT JUVENILE FOR MORE INFO | ARREST, CITED                          |
| UNFOUNDED                              | NOT PROSECUTED                         |
| JUVENILE ADMONISHED                    | PSYCHOPATHIC CASE                      |
| EXCEPTIONAL CLEARANCE                  | JUVENILE CITED                         |
| JUVENILE DIVERTED                      | JUVENILE BOOKED                        |
|                                        | LOCATED                                |
|                                        | PROSECUTED BY OUTSIDE AGENCY           |
|                                        | COMPLAINANT REFUSES TO PROSECUTE       |
|                                        | DISTRICT ATTORNEY REFUSES TO PROSECUTE |
|                                        | PROSECUTED FOR LESSER OFFENSE          |

This project will address the following predictive question:  
What are the strongest predictors for whether a crime instance in San Francisco resulted in someone being "processed" or "not processed" into the justice system?

# Dataset

The dataset contains San Francisco crime data from 2003 to May 2018 with each crime instance having the following features: incident ID, category of crime, description of crime, day of week of incident, date of incident, time of incident, police district, resolution of incident, address, longitude, latitude and location of incident.

The dataset can be found at the following link:  
- [Link to San Francisco crime data website](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry)

The dataset can be loaded using this [R script](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.R)
or this [Python script](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.py). The following is a preview of the dataset in R:

![](https://github.com/bettybhzhou/DSCI_522_SF_crime/blob/master/data/imgs/Raw_data_preview.png)

# Analysis and Results
The final report of the project can be found [here](https://github.com/bettybhzhou/DSCI_522_SF_crime/blob/master/docs/san_francisco_report.md)

# Analysis Pipeline

## Usage:

1. Clone this repository

2. From the root of the project, run the following commands:

```bash
python src/01_clean_data.py 1000 data/san_francisco_clean.csv
python src/02_EDA.py data/san_francisco_clean.csv results/figures/
python src/03_feature_engineering.py data/san_francisco_clean.csv data/san_francisco_features.csv
python src/04_decison_tree.py data/san_francisco_features.csv data/feature_results.csv
Rscript src/03_Exploratory_SF_map.R data/san_francisco_clean.csv results/figures/
Rscript -e "rmarkdown::render('docs/san_francisco_report.Rmd')"
```
Or, run all scripts from the root using the following command:

```bash
make all
```

To run this analysis using Docker, execute the following steps:

1. Clone this repository
2. Pull the Docker image from Docker Hub using the follwing command:
   ```
   docker pull bettybhz/san_francisco_crime_resolution_model
   ```
2. Navigate to the root of this project on your computer using the command line.
3. Execute the following command by filling in <PATH_ON_YOUR_COMPUTER> with the absolute path to the root of this project on your computer).

    ```
    docker run --rm -v PATH_ON_YOUR_COMPUTER:/home/San_Francisco_Crime_Resolution_Model bettybhz/san_francisco_crime_resolution_model make -C 'home/San_Francisco_Crime_Resolution_Model' all
    ```
    Execute the following command to clean up the analysis:
    
    ```
    docker run --rm -v PATH_ON_YOUR_COMPUTER:/home/San_Francisco_Crime_Resolution_Model bettybhz/san_francisco_crime_resolution_model make -C 'home/San_Francisco_Crime_Resolution_Model' clean
    
## Dependencies:
- R v1.1.456 & R libraries
  - `rmarkdown` v1.10  
  - `knitr` v1.20  
  - `tidyverse`v 1.2.1  
  - `ggmap` v2.6.1 
  - `maps` v3.3.0

- Python 3 & Python libraries:
  - `matplotlib` v2.2.2
  - `numpy` v1.14.3
  - `seaborn` v0.9.0
  - `pandas` v.23.0
  - `argparse` v1.1
  - `sklearn` v0.19.1
  - `pendulum` v2.0.4

