# DSA210TermProject

# ⚽ Underdog Detection in Football  
### Predicting Upsets Using FIFA Rankings in World Cup History

## 📌 Project Overview
Football matches are often predicted using indicators such as team strength and global rankings. However, international tournaments frequently produce surprising outcomes where lower-ranked teams defeat stronger opponents.

This project investigates whether these **upsets** can be predicted using **FIFA rankings** and historical match data from FIFA World Cup tournaments.

---

## 🎯 Objectives
- Analyze the relationship between FIFA ranking differences and match outcomes  
- Identify patterns behind underdog victories (upsets)  
- Build a machine learning model to predict the probability of an upset  
- Evaluate the predictive power of FIFA rankings  

---

## 📊 Dataset

### Sources
- World Cup match datasets (Kaggle)  
- Historical FIFA rankings (public sources)  

### Coverage
- FIFA World Cups: **1998 – 2018**  
- Several hundred international matches  

### Features
- Team names  
- Match results  
- Goals scored  
- Tournament stage  

### Engineered Features
- FIFA ranking (both teams)  
- Ranking difference  
- Historical performance metrics  
- **Upset Outcome (Target Variable)**  
  - 1 → Lower-ranked team wins  
  - 0 → Otherwise  

---

## 🔍 Methodology

### 1. Exploratory Data Analysis (EDA)
- Distribution of ranking differences  
- Frequency of upsets  
- Upsets by tournament stage  
- Goal patterns and trends  

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

## 🤖 Model Goal
Predict the probability that a match result will be an **upset**, based on pre-match information.

---

## 📈 Expected Results
- FIFA rankings will have **predictive value**, but not be sufficient alone  
- Upsets are influenced by multiple factors beyond rankings  
- Football retains a level of unpredictability  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 📁 Project Structure
