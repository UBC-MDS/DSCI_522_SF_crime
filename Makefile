# Makefile
# Ian Flores, Betty Zhou
#
# This Makefile generates all data files, figures and report of the San Francisco
# Crime Resolution Model Project.
#
# Usage:
# To run all sripts: make all
# To clean all outputs: make clean

# run all scripts
all : docs/san_francisco_report.md

# downloads data from the SF portal API, cleans it, and saves it as a CSV file.
data/san_francisco_clean.csv : src/01_clean_data.py
	python src/01_clean_data.py 100000 data/san_francisco_clean.csv

# generates exploratory data analysis figures
results/figures/category_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/category_plot.png

results/figures/dayofweek_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/dayofweek_plot.png

results/figures/pddistrict_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/pddistrict_plot.png

results/figures/report_day_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/report_day_plot.png

results/figures/report_month_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/report_month_plot.png

results/figures/target_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/target_plot.png

results/figures/time_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/time_plot.png

results/figures/x_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/x_plot.png

results/figures/y_plot.png : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/y_plot.png

# generates a map of San Francisco with crime density overlayed on top as a png output
results/figures/SF_crime.png : src/03_Exploratory_SF_map.R data/san_francisco_clean.csv
	Rscript src/03_Exploratory_SF_map.R data/san_francisco_clean.csv results/figures/SF_crime.png

# extracts and formats the features necessary for the Decision Tree Classifier
data/san_francisco_features.csv : src/03_feature_engineering.py data/san_francisco_clean.csv
	python src/03_feature_engineering.py data/san_francisco_clean.csv data/san_francisco_features.csv

# trains the Decision Tree Classifier.
data/feature_results.csv : src/04_decison_tree.py data/san_francisco_features.csv
	python src/04_decison_tree.py data/san_francisco_features.csv data/feature_results.csv

# generates the final report
docs/san_francisco_report.md : results/figures/category_plot.png results/figures/dayofweek_plot.png results/figures/pddistrict_plot.png results/figures/report_day_plot.png results/figures/report_month_plot.png results/figures/SF_crime.png results/figures/target_plot.png results/figures/time_plot.png results/figures/x_plot.png results/figures/y_plot.png data/feature_results.csv data/san_francisco_clean.csv data/san_francisco_features.csv
	Rscript -e "rmarkdown::render('docs/san_francisco_report.Rmd')"

# clean all output of makefile
clean :
	rm -f results/figures/*.png
	rm -f data/*.csv
	rm docs/san_francisco_report.md
