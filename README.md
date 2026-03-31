# Underdog Detection in Football: Predicting Upsets Using FIFA Rankings

## Project Overview
This project investigates whether underdog victories (upsets) in international football can be predicted using FIFA rankings and match-related statistics. The analysis focuses on historical FIFA World Cup data across multiple tournaments to understand the conditions under which lower-ranked teams defeat stronger opponents.

## Motivation
Football is widely considered unpredictable, especially in major tournaments such as the FIFA World Cup. While FIFA rankings provide an estimate of team strength, they do not always explain surprising match outcomes. This project aims to evaluate the predictive power of FIFA rankings and identify key factors contributing to upset results.

## Research Question
Can underdog victories in FIFA World Cup matches be predicted using FIFA rankings and historical performance data?

## Dataset
The project uses publicly available datasets that include:

- FIFA World Cup match data (multiple tournaments)
  - Team names
  - Match outcomes
  - Goals scored
  - Tournament stage

- FIFA ranking data
  - Team rankings over time
  - Rankings matched to each game based on the closest date prior to the match

## Data Processing
The datasets are merged using team names and match dates. FIFA rankings are aligned with each match by selecting the closest available ranking prior to the game.

New features are created, including:
- Ranking difference between teams
- Goal difference statistics
- Historical performance indicators

A binary target variable is defined:
- Upset = 1 if the lower-ranked team wins
- Upset = 0 otherwise

## Methodology
The project follows a standard data science pipeline:

1. Data Collection and Cleaning
2. Feature Engineering
3. Exploratory Data Analysis (EDA)
4. Model Development

Machine learning models used:
- Logistic Regression
- Decision Tree Classifier

## Evaluation Metrics
Model performance is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

## Expected Outcomes
The project aims to determine:
- Whether FIFA rankings are a strong predictor of match outcomes
- How frequently upsets occur
- Which factors increase the likelihood of underdog victories

## Project Structure
### 2. Feature Engineering
- Ranking gap calculation  
- Performance-based indicators  
- Match context features  

### 3. Modeling
- Logistic Regression  
- Decision Tree Classifier  

### 4. Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-Score  

### 5. Interpretation
- Feature importance analysis  
- Role of FIFA rankings vs other factors  

---

## Model Goal
Predict the probability that a match result will be an upset, based on pre-match information.

---

## Expected Results
- FIFA rankings will have predictive value, but not be sufficient alone  
- Upsets are influenced by multiple factors beyond rankings  
- Football retains a level of unpredictability  

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---


## Requirements
All code is written in Python. Required libraries include:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn



## Reproducibility
To reproduce the analysis:
1. Download the datasets
2. Place them in the data/ directory
3. Run the notebooks or scripts in order


## Author
Ahmet Emir Çankaya
