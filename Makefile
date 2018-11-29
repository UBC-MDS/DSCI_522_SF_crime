# Makefile
# Ian Flores, Bety Zhou

data/san_francisco_clean.csv : src/01_clean_data.py
	python src/01_clean_data.py 1000 data/san_francisco_clean.csv

results/figures/ : src/02_EDA.py data/san_francisco_clean.csv
	python src/02_EDA.py data/san_francisco_clean.csv results/figures/

data/san_francisco_features.csv : src/03_feature_engineering.py data/san_francisco_clean.csv
	python src/03_feature_engineering.py data/san_francisco_clean.csv data/san_francisco_features.csv

data/feature_results.csv : src/04_decison_tree.py data/san_francisco_features.csv
	python src/04_decison_tree.py data/san_francisco_features.csv data/feature_results.csv

results/figures/SF_crime.png : src/03_Exploratory_SF_map.R data/san_francisco_clean.csv
	Rscript src/03_Exploratory_SF_map.R data/san_francisco_clean.csv results/figures/

docs/san_francisco_report.md : results/figures/ data/
	Rscript -e "rmarkdown::render('docs/san_francisco_report.Rmd')"
