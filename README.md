# Salary Estimator

## Overview

This project focuses on building a salary estimator system for tech jobs based on the current market salary trends. Market salaries were scraped from Glassdoor, focusing on data-related job positions. Data cleaning, EDA were done before model building. Feature Selection, Data Preprocessing were done before implementing ML models. Multiple models were implemented to choose the best performer.

1. **Linear Regression:**
   - Linear regression models are built using both statsmodel and sklearn.

2. **Lasso Regression:**
   - Baseline Lasso regression is performed, followed by hyperparameter tuning using GridSearchCV.

3. **Random Forest Regression:**
   - A Random Forest regression model is built and evaluated. Hyperparameter tuning is performed using RandomizedSearchCV.

4. **Ensemble Testing:**
   - The model's predictions are tested using various ensembles, including Linear Regression, Lasso Regression, and Random Forest Regression.

## Data Files

- `glassdoor_jobs.csv`: Information scraped from Glassdoor containing salaries for different job postings as well as information about the companies, domain, location, etc.
- `processed_df.csv`: Processed `glassdoor_jobs.csv` after the data cleaning process.
- `EDA_glassdoor_jobs.csv`: Glassdoor_jobs after further processing for EDA.

## Code Files

1. **`glassdoor_scraper`:** Web scraping job data from Glassdoor using Selenium.
   - `01_data_collection:` Implementation of Glassdoor scraper, scraped 1000 job postings.
   - `02_data_cleaning:` Cleaning the Glassdoor Jobs dataset for further analysis and modeling.
   - `03_EDA:` Exploring and visualizing key aspects of the Glassdoor Jobs dataset.
   - `04_model_building:` Building a salary estimation model using the Glassdoor Jobs dataset.

## Figures

Various images generated during EDA for better visualization and understanding.

## Selenium Web Scraper

### Overview

This project involves web scraping job data from Glassdoor using Selenium. The scraper gathers information such as job title, salary estimate, job description, company details, and more.

#### Author

Although multiple tweaks were made on the original code, the original author must be credited.
- Original Author: Kenarapfaik
- GitHub: [scraping-glassdoor-selenium](https://github.com/arapfaik/scraping-glassdoor-selenium)

- Scraped 1000 job postings on Glassdoor.
- The script uses Selenium to automate browser interactions.
- It navigates through job listings, clicks on each job to gather details, and stores the information in a Pandas DataFrame.
- Information gathered includes 'Job Title', 'Salary Estimate', 'Job Description', 'Rating', 'Company Name', 'Location', 'size', 'type', 'founded', 'industry', 'sector', 'company_revenue', company’s other perks, and work environment.

## Data Cleaning and Processing

### Overview

Focuses on cleaning the Glassdoor Jobs dataset for further analysis and modeling. The dataset is loaded, and various data cleaning and preprocessing steps are performed to enhance the quality and usability of the data.

### Data Cleaning Steps

1. **Salary Estimate Parsing:**
   - The 'Salary Estimate' column is parsed to extract meaningful salary information.
   - Separate columns for minimum, maximum, and average salary are created.

2. **Company Name Standardization:**
   - The 'Company Name' column is cleaned to remove additional information, leaving only the company name.

3. **Job Location:**
   - The 'Location' column is used to extract the state code and create a new 'job_state' column.

4. **Company Age:**
   - A new 'company_age' column is created based on the 'founded' column.

5. **Tech Requirements:**
   - Tech-related requirements are identified and stored in binary columns (e.g., Python, Excel, Spark, AWS, SQL, etc.).

6. **Job Title and Seniority:**
   - The 'Job Title' column is simplified, and a new 'jobtitle_simp' column is created.
   - Seniority level is identified and stored in a new 'seniority' column.

7. **Fix States Names:**
   - State names are fixed and standardized for consistency.

8. **Job Description Length:**
   - A new column 'jobdesc_length' is created to represent the length of job descriptions.

9. **Hourly Rate Conversion:**
   - Hourly rate salaries are converted to annual salaries for consistency.

10. **Cleaned Dataset:**
    - The cleaned dataset is saved as 'processed_df.csv' in the `data/processed` directory.

## Exploratory Data Analysis

### Overview

EDA focuses on exploring and visualizing key aspects of the Glassdoor Jobs dataset.

### Summary of EDA

All EDA plots and figures can be accessed from “reports/figures”.

1. **Companies Rating Distribution:**
   - A histogram is plotted to visualize the distribution of company ratings.
   - The plot is saved as `companies_rating_dist.png`.

2. **Average Salary Distribution:**
   - A histogram is plotted to visualize the distribution of average salaries.
   - The plot is saved as `average_salary_dist.png`.

3. **Average Salary Boxplot:**
   - A boxplot is created to visualize the distribution of average salaries.
   - The plot is saved as `average_salary_boxplot.png`.

4. **Bar Plot for Company Size:**
   - A horizontal bar plot is generated to show the distribution of average salaries based on company size.
   - The plot is saved as `company_size_barplot.html`.

5. **Bar Plot for Average Salary per Company Size:**
   - A horizontal bar plot is created to display the average salary for each company size category.
   - The plot is saved as `salary_company_size_Barplot.html`.

6. **Correlation Heatmap:**
   - A heatmap is generated to display the correlation between numerical features such as company age, average salary, and company rating.
   - The plot is saved as `heatmap.html`.

7. **Bar Charts for Categorical Variables:**
   - Bar charts are created for each categorical variable, displaying their frequency.
   - The charts are saved as individual PNG files in the specified directory.

## Model Building

### Overview

Focuses on building a salary estimation model using the Glassdoor Jobs dataset. The dataset is loaded and processed, and various machine learning models are trained and evaluated for predicting average salaries. The models include Linear Regression, Lasso Regression, and Random Forest Regression.

### Model Building Steps

1. **Data Loading:**
   - The cleaned dataset is loaded for model building.

2. **Feature Selection:**
   - Relevant features are selected for model building, including numerical, categorical, and binary features.

3. **Data Preprocessing:**
   - Categorical variables are one-hot encoded to make them compatible with machine learning models.

4. **Train-Test Split:**
   - The dataset is split into training and testing sets.

5. **Linear Regression:**
   - Linear regression models are built using both statsmodel and sklearn.

6. **Lasso Regression:**
   - Baseline Lasso regression is performed, followed by hyperparameter tuning using GridSearchCV.

7. **Random Forest Regression:**
   - A Random Forest regression model is built and evaluated. Hyperparameter tuning is performed using RandomizedSearchCV.

8. **Ensemble Testing:**
   - The model's predictions are tested using various ensembles, including Linear Regression, Lasso Regression, and Random Forest Regression.

9. **Model Serialization:**
   - The best-performing Random Forest model is serialized using Pickle for future use.
  

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
