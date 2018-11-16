# SF_crime
Team Members:

- Betty Zhou (bettybhz)
- Ian Flores (ian-flores)

1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. Prove to us that you can load the data set into R or Python (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).

- [Link to San Francisco crime data website](https://data.sfgov.org/resource/cuks-n6tp)
- [Link to R script for downloading dataset](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.R)
- [Link to Python script for downloading dataset](https://github.com/UBC-MDS/DSCI_522_SF_crime/blob/master/src/01_load-data.py)

2 . With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).
> What are the strongest predictors for whether a crime instance in San Francisco resulted in an arrest?
> This question is a predictive question.

3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you know how to do (report an estimate and confidence intervals, a two-group hypothesis), or will learn how to do in the first week of block 3 (ANOVA, classification with a decision tree).

> We will implement a classification of the San Francisco crime data with a decision tree. The following table outlines the features we will be using to build the classifier:

| Feature | Feature Type |
|---|---|
| Category | Categorical |
| Description | Categorical |
| Day of week | Categorical |
| Time | Continuous|
| Police District | Categorical |
| Longitude | Continuous |
| Latitude | Continuous |

We will use scikit-learn to pre-process the features and train the model.

> Since our dataset is very skewed towards one of the classes, we will recode our target response variables from 17 classes to only 2 classes. The final target response variables will be "arrested" and "not arrested".

4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

> We will summarize our data by reporting a table of the strongest predictor for whether a crime instance in San Francisco resulted in an arrest. The strongest predictors are the predictors that show up earlier in our decision tree as this indicates that these predictors will have the lowest gini scores and are the best predictors for the dataset. We will also report a graphviz plot of our decision tree. 

