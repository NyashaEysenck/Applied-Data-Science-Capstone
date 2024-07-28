# Applied-Data-Science-Capstone


This repository contains the notebooks and code for the Applied Data Science Capstone project completed as part of the Coursera specialization. The project demonstrates a comprehensive application of data science skills, including data collection, cleaning, exploration, visualization, and machine learning, to analyze SpaceX launch data.

## Skills Learned

Throughout this project, the following skills were developed and applied:

- **Data Collection**: Leveraged APIs and web scraping techniques to gather data from multiple sources.
- **Data Wrangling**: Cleaned and prepared raw data for analysis, addressing missing values and inconsistencies.
- **Exploratory Data Analysis (EDA)**: Conducted in-depth analysis to uncover patterns, trends, and insights.
- **Data Visualization**: Created visual representations of data to effectively communicate findings.
- **SQL for Data Analysis**: Utilized SQL queries to extract and analyze data from structured databases.
- **Machine Learning**: Built and evaluated predictive models to determine the likelihood of SpaceX launch successes.
- **Interactive Visualizations**: Developed an interactive dashboard using Dash to visualize and explore SpaceX launch data.
- **Mapping with Folium**: Created interactive maps to visualize geographical data related to SpaceX launch sites.

## Project Structure

The repository is organized as follows:

- `notebooks/`: Contains Jupyter notebooks used throughout the project.
  - `Build-an-Interactive-Map-with-Folium.ipynb`: Demonstrates creating an interactive map using Folium to visualize SpaceX launch sites.
  - `Data Collection - Scraping.ipynb`: Covers scraping additional data from Wikipedia.
  - `Data-Collection – SpaceX-API.ipynb`: Details collecting data from the SpaceX API.
  - `Data-Wrangling.ipynb`: Focuses on cleaning and preparing the collected data.
  - `EDA-with-Data-Visualization.ipynb`: Performs exploratory data analysis with various data visualization techniques.
  - `EDA-with-SQL.ipynb`: Uses SQL queries to perform EDA on the cleaned dataset.
  - `SpaceX_Machine Learning Prediction_Part_5.ipynb`: Builds and evaluates machine learning models to predict launch outcomes.
- `data/`: Contains raw and processed data files.
  - `spacex_launch_dash.csv`: CSV file containing SpaceX launch data for the Dash application.
- `app/`: Contains the Dash application files.
  - `spacex_dash_app.py`: Python script for the Dash application.
- `images/`: Directory containing images used in the notebooks and README.
- `README.md`: This file.

## Notebooks Overview

### Build-an-Interactive-Map-with-Folium.ipynb

- **Task**: Create an interactive map to visualize SpaceX launch sites.
- **Skills**: Folium library, geographical data visualization.

### Data Collection - Scraping.ipynb

- **Task**: Scrape additional data about SpaceX launches from Wikipedia.
- **Skills**: Web scraping, BeautifulSoup4.

### Data-Collection – SpaceX-API.ipynb

- **Task**: Collect data from the SpaceX API.
- **Skills**: API requests, data collection.

### Data-Wrangling.ipynb

- **Task**: Clean and preprocess the collected data.
- **Skills**: Data cleaning, handling missing values, data merging.

### EDA-with-Data-Visualization.ipynb

- **Task**: Perform exploratory data analysis (EDA) on the cleaned dataset.
- **Skills**: Data visualization, matplotlib, seaborn, data analysis.

### EDA-with-SQL.ipynb

- **Task**: Perform EDA using SQL queries on the cleaned dataset.
- **Skills**: SQL, data extraction, data analysis.

### SpaceX_Machine Learning Prediction_Part_5.ipynb

- **Task**: Build machine learning models to predict the success of SpaceX launches.
- **Skills**: Machine learning, scikit-learn, model evaluation, predictive analysis.

## Dash Application

The repository includes a Dash application to visualize SpaceX launch data:

- `spacex_dash_app.py`: Contains the code for the Dash application, allowing interactive data exploration.
- `spacex_launch_dash.csv`: CSV file used by the Dash application for visualization.
