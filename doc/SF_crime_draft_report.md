San Francisco Crime Classifier
================
Betty Zhou and Ian Flores
November 24, 2018

Table of Contents
=================

1.  Introduction
2.  Usage

-   Dependencies

1.  Dataset
2.  Exploratory Analysis
3.  Analysis
4.  Assumptions
5.  Limitations and Future Directions

3.0 Exploratory Data Analysis
=============================

Exploratory analysis was performed on the cleaned dataset to better understand the trends of different variables in our dataset.

First, we checked the overall ratio of our target classes:

<img src="/Users/bettyzhou/Documents/Block_3_labs/DSCI_522_SF_crime/results/figures/target_plot.png" width="640" style="display: block; margin: auto;" />
<center>
Figure ... . Bar graph to check the balance in the target class.
</center>
Next, we investigated all the predictors in the data set in relation to our target class for 100,000 crime instances. The features that were explored include: category, day of week, description, police district, time, longitude, latitude, month of report and day of report, in respect to whether the resolution of the crime instance was processed or non-processed. The features that demonstrated to be good predictors for segregrating processed from non-processed crime resolutions are shown below.

|    X| category      | dayofweek | descript                             | pddistrict | resolution     |  time|          x|         y|  report\_month|  report\_day|
|----:|:--------------|:----------|:-------------------------------------|:-----------|:---------------|-----:|----------:|---------:|--------------:|------------:|
|    0| ASSAULT       | Monday    | THREATS AGAINST LIFE                 | TARAVAL    | non\_processed |   860|  -122.4750|  37.73246|              6|           20|
|    1| BURGLARY      | Tuesday   | BURGLARY, FORCIBLE ENTRY             | SOUTHERN   | non\_processed |  1260|  -122.3656|  37.80967|             10|           17|
|    2| NON-CRIMINAL  | Thursday  | COURTESY REPORT                      | NORTHERN   | non\_processed |   720|  -122.4203|  37.78845|              9|            1|
|    3| LARCENY/THEFT | Tuesday   | GRAND THEFT FROM PERSON              | NORTHERN   | non\_processed |  1072|  -122.4310|  37.78303|             11|           14|
|    4| VEHICLE THEFT | Saturday  | STOLEN MOTORCYCLE                    | CENTRAL    | non\_processed |    30|  -122.4179|  37.79368|              4|            7|
|    5| VANDALISM     | Thursday  | MALICIOUS MISCHIEF, BREAKING WINDOWS | CENTRAL    | non\_processed |   120|  -122.3997|  37.79737|              2|           15|

Including Plots
---------------

You can also embed plots, for example:

![](SF_crime_draft_report_files/figure-markdown_github/pressure-1.png)

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
