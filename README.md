# 10 Academy Intensive Training Week-0 Challenge

# Task 1: Git, GitHub, and Exploratory Data Analysis (EDA)

## Overview
This task focuses on setting up the development environment, implementing version control with Git and GitHub, and performing exploratory data analysis on the news dataset.

## Objectives
- Set up a Python virtual environment and install necessary dependencies.
- Create a Git repository and configure it for the project.
- Implement continuous integration and continuous deployment (CI/CD) using GitHub Actions.
- Perform exploratory data analysis to gain insights into the news dataset, including:
  - Understanding the dataset structure and content
  - Identifying top news sources, countries, and topics
  - Analyzing the sentiment distribution across news articles
  - Comparing content metadata across news sources

## Steps

1. **Set up Python Environment**:
   - Create a new virtual environment using a tool like `venv` or `conda`.
   - Install the required dependencies by running `pip install -r requirements.txt`.

2. **Initialize Git Repository**:
   - Create a new Git repository in your local machine using `git init`.
   - Add the necessary files to the repository using `git add .`.
   - Make the initial commit with a descriptive message: `git commit -m "Initial commit"`.

3. **Configure CI/CD with GitHub Actions**:
   - Create a new GitHub repository and push your local repository to the remote:
     ```
     git remote add origin https://github.com/your-username/news-data-analysis.git
     git push -u origin main
     ```
   - In the GitHub repository, set up a new GitHub Actions workflow to run unit tests and code linting on every push.
   - Configure the workflow to run Flake8 for code style checking and a set of unit tests.

4. **Perform Exploratory Data Analysis**:
   - Load the news dataset and examine the data structure, features, and content.
   - Identify the top news sources by article count and website traffic.
   - Analyze the distribution of news articles across countries and regions.
   - Investigate the most common topics covered in the news articles using keyword extraction and topic modeling.
   - Assess the sentiment of news headlines and content, comparing the sentiment distribution across news sources.
   - Explore the relationships between news reporting frequency, sentiment, and website global ranking.

## Deliverables
- A public GitHub repository containing the code and configuration files for Task 1.
- A summary report highlighting the key findings and insights from the exploratory data analysis.

## Next Steps
After completing Task 1, you will proceed to Task 2, which focuses on building data science components, including time-series analysis, news headline classification, and topic modeling.
