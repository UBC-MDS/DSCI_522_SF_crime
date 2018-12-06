# Pull from anaconda3 Docker base image
FROM continuumio/anaconda3

# Install python dependencies
RUN pip install pendulum

# Reinstall matplotlib and upgrade pip
RUN pip uninstall -y matplotlib && \
  python -m pip install --upgrade pip && \
  pip install matplotlib

# Install R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN conda install libiconv

# Install R dependencies
RUN conda install --quiet --yes -c conda-forge r-rmarkdown r-knitr r-tidyverse r-ggmap r-maps r-here

# Install Make
RUN apt-get update && apt-get install make
