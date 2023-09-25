# Data Engineering Pipeline with PySpark(Sanuis Health Assesment)

## Table of Contents

-   [Overview](https://chat.openai.com/c/8168c398-4d5c-4f26-ab9b-cf7c9228898a#overview)
-   [Directory Structure](https://chat.openai.com/c/8168c398-4d5c-4f26-ab9b-cf7c9228898a#directory-structure)
-   [Modules Description](https://chat.openai.com/c/8168c398-4d5c-4f26-ab9b-cf7c9228898a#modules-description)
-   [Special Notes](https://chat.openai.com/c/8168c398-4d5c-4f26-ab9b-cf7c9228898a#special-notes)
-   [How to Run](https://chat.openai.com/c/8168c398-4d5c-4f26-ab9b-cf7c9228898a#how-to-run)

## Overview

This pipeline is designed to ingest, clean, aggregate, and visualize data. It calculates three Key Performance Indicators (KPIs) and generates a Visualization Report in PDF format. The code is written using PySpark, and an accompanying Jupyter Notebook (`*.ipynb`) is provided for further exploration and visualization.

## Directory Structure

    `.
    ├── business_logic
    │   ├── data_aggregation.py
    │   ├── data_cleaning.py
    │   ├── data_ingestion.py
    │   ├── data_output.py
    │   ├── data_visualisation.py
    │   └── feature_engineering.py
    ├── config.py
    ├── dataset2.csv
    ├── main.py
    ├── output
    │   ├── act_intensity
    │   │   └── act_intensity.csv
    │   ├── heart_rate_KPI
    │   │   └── heart_rate_KPI.csv
    │   └── temp_variability_KPI
    │       └── temp_variability.csv
    ├── Visualization_Report.pdf
    └── Jupyter_Notebook.ipynb  (Optional)` 

## Modules Description

### `business_logic`

-   `data_aggregation.py`: Contains functions for data aggregation.
-   `data_cleaning.py`: Contains functions for data cleaning.
-   `data_ingestion.py`: Contains functions for data ingestion.
-   `data_output.py`: Contains functions for outputting data.
-   `data_visualisation.py`: Contains functions for data visualization.
-   `feature_engineering.py`: Contains functions for feature engineering.

### `config.py`

-   Contains various configuration settings like file paths.

### `dataset2.csv`

-   Download this dataset from following link
- https://www.kaggle.com/datasets/diegosilvadefrana/fisical-activity-dataset

### `main.py`

-   The entry point for the pipeline.

### `output`

-   Directory where the output CSV files and KPIs are stored.

### `Visualization_Report.pdf`

-   A PDF report containing various visualizations.

### `Wearable_data_computations.ipynb`

-   A Jupyter Notebook for interactive data exploration and visualization.

## Special Notes

### Data Ingestion

-   The pipeline is currently set to ingest a subset of the data due to its large size. If you wish to load the entire dataset, you can uncomment the relevant line in `data_ingestion.py`.

### Jupyter Notebook

-   An optional Jupyter Notebook is provided where all KPIs and visualizations are calculated. This is useful for exploratory data analysis.

## How to Run

1.  Make sure PySpark is installed.
2.  Download Dataset and paste in the directory
3.  Navigate to the project directory.
4.  Run `main.py` to execute the pipeline.
5.  `spark-submit main.py`

### Note

 - Make sure you have pyspark and spark installed in order to run this
   project

