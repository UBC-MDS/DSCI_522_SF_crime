#! /usr/bin/env Rscript
# Exploratory_SF_map.R
# Betty Zhou & Ian Flores Siaca, November 23, 2018
#
# This script generates a map of San Francisco with crime density overlayed on top as a png output. This # script takes in a .csv and the output path as the variable arguments.
#
# Dependencies: tidyverse, ggmap, maps
#
# Usage:
# Rscript Exploratory_SF_map.R <input file> <output path>
# <input file> is the input CSV.
# <output path> is the path for which the png will be written to.
# Example: Rscript Exploratory_SF_map.R clean_sf_data_100k.csv results/figures/


library(tidyverse)
suppressPackageStartupMessages(library(ggmap))
suppressPackageStartupMessages(library(maps))

# read in command line arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]
output_path <- args[2]

# define main function
main <- function(){
  # load data
    sf_data <- read_csv(input_file)

  processed <- sf_data %>%
    filter(resolution == "processed")
  non_processed <- sf_data %>%
    filter(resolution == "non_processed")

  # Retrieve base map of San Francisco and plot SF crime density
  basemap <- c(-122.48, 37.720, -122.378, 37.815) %>%
    get_stamenmap(maptype = "toner", zoom=12) %>%
    ggmap()

  SF_crime_map <- basemap +
   geom_density2d(aes(x, y, colour = 'blue'),
                 data = non_processed) +
    geom_density2d(aes(x, y, colour = 'red'),
                 data = processed) +
    scale_color_manual("Resolution of the Incident",
                       values = c(blue = 'blue', red = 'red'),
                       labels = c('Non Processed', 'Processed')) +
    xlab("Longitude") +
    ylab("Latitude")

  # Save SF crime map
  ggsave("SF_crime.png", plot = SF_crime_map, path = output_path, width = 6, height = 4)
}

# call main function
main()
