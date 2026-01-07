# Spam Detection AI
## Project Overview

### This project is a simple AI based spam detection system that classifies messages as Spam or Not Spam. The solution has the complete AI workflow from data preprocessing and model training to deployment using FastAPI.

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK
* FastAPI
* Uvicorn

## Dataset

### The dataset consists of SMS messages that are labeled either spam or not spam. Messages marked as ham represent normal texts, while messages labeled spam indicate unwanted or spam content. Before training the models, all messages were cleaned and processed for prediction.

## Model Used

Multiple models were trained and evaluated:

Naive Bayes

Logistic Regression

Random Forest

XGBoost

Among them, Logistic Regression was selected as the final model because it showed the best balance of precision and recall using the F1-score metric.

