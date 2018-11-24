San Francisco Report
================
Authors: Ian Flores Siaca & Betty Zhou

-   [1.0 Introduction](#introduction)
-   [2.0 Dataset](#dataset)
-   [3.0 Exploratory Data Analysis](#exploratory-data-analysis)
-   [4.0 Analysis & Results](#analysis-results)
-   [5.0 Assumptions](#assumptions)
-   [6.0 Limitations and Future Directions](#limitations-and-future-directions)
-   [7.0 References](#references)

1.0 Introduction
----------------

With the past Midterms elections in San Francisco, we could observe the debate between candidates of the Republican Party and the Democratic Party about how the city should handle crime. Based on this debates that not only influence San Francisco, we decided to ask, what are the strongest predictors for whether a crime instance in San Francisco resulted in being processed by the justice system or not? For this we used the San Francisco crime dataset provided by the city of San Francisco. This dataset includes incidents reported to the San Francisco Police Department. There were two ways of submitting an incident report, either a police officer submitted one or one individual could do it as well. The dataset contains incidents reported from 2003 to 2018. To access it, we need it to submit a query to the API and as such decided to only request 100,000 cases. Each incident contains information about the category of the crime being reported, the description of the crime, the day of the week (i.e Monday, Tuesday, etc.), the date, the time, the police district as of July 18, 2015, the crime resolution and the latitude and longitude of where the incident occured. From the datestamp, we extracted the month and the day as features, but not the year, to see if there were any seasonal patterns ocurring. From the text description provided, we extracted 50 features (i.e words) to be used as well.

#### 1.1 Project Objective

The goal of this project is to implement a classification of the San Francisco crime data with a decision tree to predict the resolution of a crime instance. The resolution of a crime instance can be either "processed" or "non-processed". Processed indicates that a crime instance resulted in a subject being processed into the justice system.

This project will address the following predictive question: What are the strongest predictors for whether a crime instance in San Francisco resulted in an a "processed or non-processed" resolution?

2.0 Dataset
-----------

The San Francisco crime dataset used in this projects contains 10 features. A preview of the dataset is shown below:

| category      | dayofweek | descript                             | pddistrict | resolution     |  time|          x|         y|  report\_month|  report\_day|
|:--------------|:----------|:-------------------------------------|:-----------|:---------------|-----:|----------:|---------:|--------------:|------------:|
| ASSAULT       | Monday    | THREATS AGAINST LIFE                 | TARAVAL    | non\_processed |   860|  -122.4750|  37.73246|              6|           20|
| BURGLARY      | Tuesday   | BURGLARY, FORCIBLE ENTRY             | SOUTHERN   | non\_processed |  1260|  -122.3656|  37.80967|             10|           17|
| NON-CRIMINAL  | Thursday  | COURTESY REPORT                      | NORTHERN   | non\_processed |   720|  -122.4203|  37.78845|              9|            1|
| LARCENY/THEFT | Tuesday   | GRAND THEFT FROM PERSON              | NORTHERN   | non\_processed |  1072|  -122.4310|  37.78303|             11|           14|
| VEHICLE THEFT | Saturday  | STOLEN MOTORCYCLE                    | CENTRAL    | non\_processed |    30|  -122.4179|  37.79368|              4|            7|
| VANDALISM     | Thursday  | MALICIOUS MISCHIEF, BREAKING WINDOWS | CENTRAL    | non\_processed |   120|  -122.3997|  37.79737|              2|           15|

*Table 1. Preview of San Francisco crime dataset.*

3.0 Exploratory Data Analysis
-----------------------------

Exploratory analysis was performed on the cleaned dataset to better understand the trends of different variables in our dataset.

First, we checked the overall ratio of the resolution classes, which is the target classes for our classifer:

<img src="/Users/bettyzhou/Documents/Block_3_labs/DSCI_522_SF_crime/results/figures/target_plot.png" width="640" style="display: block; margin: auto;" /> *Figure 1. An Overall check of the number of examples for each target class in resolution.*

The bar graph indicates a 2:1 imbalance in our target class between non-processed and processed. We plan to mitigate this imbalance in target classes by setting `class_weight = "balanced"`when building our model with `DecisionTreeClassifier` in scikit-learn. Therefore, we will keep this imbalance in mind for the remaining exploratory analysis where a 2 to 1 difference between non-processed and processed may be due to the class imbalance in the initial dataset and may not be indicative of trends in the dataset.

Next, we investigated all the predictors in the data set in relation to our target class for 100,000 crime instances. The features that were explored include: category, day of week, description, police district, time, longitude, latitude, month of report and day of report, in respect to whether the resolution of the crime instance was processed or non-processed. The features that were demonstrated to be good predictors for segregrating processed from non-processed crime resolutions are shown below.

A map of the density distribution of resolution for San Francisco crime instances was plotted below. <img src="/Users/bettyzhou/Documents/Block_3_labs/DSCI_522_SF_crime/results/figures/SF_crime.png" width="1800" style="display: block; margin: auto;" /> *Figure 2. Density distribution of the resolution for crime incidents reported in San Francisco. *

The density distribution for non-processed and processed resolved crime instances appear to be segregrated based on longitude and latitude. The non-processed and processed crime instances occurred in locations of close proximity, but the map clearly shows the 2 resolutions to be concentrated at different longitudes and latitudes. Therefore, latitude and longitude may be strong predictors for the resolution of a crime instance in San Francisco.

<img src="/Users/bettyzhou/Documents/Block_3_labs/DSCI_522_SF_crime/results/figures/category_plot.png" width="640" style="display: block; margin: auto;" /> *Figure 3. Bar graph of category distribution for San Francisco crime instances that resulted in a processed and non-processed resolution. *

If category is not a strong predictor for resolution, then we should see a 2:1 ratio between non-processed and processed for each class in category due to the 2:1 class imbalance in the resolution feature. From the bar graph above, there are many classes within category that do not demonstrate the 2:1 ratio between non-processed and processed, such as larceny/theft, vehicle theft, Drug/narcotic etc. Therefore, these classes within the category feature may be good predictors for whether a crime instance will result in a "processed or non-processed" resolution.

<img src="/Users/bettyzhou/Documents/Block_3_labs/DSCI_522_SF_crime/results/figures/time_plot.png" width="1000" style="display: block; margin: auto;" /> *Figure 4. Time distribution for San Francisco crime instances that resulted in a processed and non-processed resolution.*

From the histogram above, there is approximately a 2:1 ratio between non-processed and processed for each interval of time, except from approximated 200 to 300 minutes from midnight (i.e. 3AM to 5 AM). Therefore, this indicates that time may be a good predictor for the resolution of a crime instance in San Francisco.

------------------------------------------------------------------------

4.0 Analysis & Results
----------------------

After fitting the decision tree classifier, we observe that the main features for predicting whether a person will be processed or not by the justice system in San Francisco, are the description, the crime category, the time and the location. To calculate this importance we are using the Gini importance.

#### Top Features

| Feature                   |  Importance|
|:--------------------------|-----------:|
| auto                      |      0.1563|
| property                  |      0.1083|
| category\_VEHICLE THEFT   |      0.0970|
| category\_VANDALISM       |      0.0673|
| category\_BURGLARY        |      0.0611|
| category\_SUSPICIOUS OCC  |      0.0542|
| category\_NON-CRIMINAL    |      0.0393|
| category\_ROBBERY         |      0.0392|
| stolen                    |      0.0386|
| x                         |      0.0364|
| category\_ASSAULT         |      0.0357|
| building                  |      0.0336|
| time                      |      0.0327|
| y                         |      0.0325|
| category\_STOLEN PROPERTY |      0.0218|
| vehicle                   |      0.0148|
| person                    |      0.0140|

*Table 2. Top features of the decision tree classifier for San Francisco Crime Data. *

If we evaluate the performance of our model we can see that it has an accuracy of around 8 out of 10. This means that for every 10 people we predict, we are going to predict correctly for 8 individuals.

|                  |         |
|:-----------------|--------:|
| Testing Accuracy |  80.756%|

5.0 Assumptions
---------------

The resolution target response variable initially had 17 classes in the orginal raw dataset. We recoded resolution into "processed" and "non-processed" based on the description provided by the [San Francisco Police Department](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry). The recoding of the resolution target response could be different based on the interpretation of the descriptions provided by the police department. The resolution variable was recoded as demonstrated in the table below:

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

*Table 3. Recoding of Resolution target response variable.*

6.0 Limitations and Future Directions
-------------------------------------

Due to the time constraint of this project, we randomly subset 100,000 crime instances from the 2 million San Francisco crime dataset to train and validate our model. We also limited the analysis to include only the top 50 most frequent words in the description feature. This could have eliminated rare words that could have been good predictors in classifying the resolution of a crime instance in San Francisco.

Therefore, in order to improve our analysis, we would build our classifier on all 2 million San Francisco crime instances and look at addition classes within the description feature to better generalize our model and increase the validation score. We could also pool additional features related to crime instances, such as income information or employment rate, to determine whether there are other predictors, not in the current San Francisco dataset, that may be strong predictors for the resolution of a crime instance.

7.0 References
--------------

[Data](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry)

[San Francisco Debates](https://www.nytimes.com/2018/06/06/us/-homelessness-housing-san-francisco.html)

[Basic Models for Supervised Learning](https://artint.info/2e/html/ArtInt2e.Ch7.S3.SS1.html)
