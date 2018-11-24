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
   geom_density2d(aes(x, y),
                 data = non_processed,
                 colour = 'blue') +
    geom_density2d(aes(x, y),
                 data = processed,
                 colour = 'red') +
    xlab("longitude") + 
    ylab("latitude")

  # Save SF crime map 
  ggsave("SF_crime.png", plot = SF_crime_map, path = output_path, width = 3, height = 3)
}

# call main function
main()
