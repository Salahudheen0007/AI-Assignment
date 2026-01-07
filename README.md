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


* Naive Bayes

* Logistic Regression

* Random Forest

* XGBoost

### Among them, Logistic Regression  was selected as the final model because both Logistic Regression and Random Forest showed the best balance of precision and recall using the F1-score metric.And chose Logistic Regression for deployment


## How the system works(basic)

* Messages are cleaned using Lowercasing,Removing punctuation,Stopword removal and Lemmatization

* Text is converted into numbers using CountVectorizer.

* The trained model predicts whether a message is Spam or Not Spam.

* The model is deployed using FastAPI and can be accessed through an API.
  
# Setup Instructions
️1.Clone the Repository
* git clone <https://github.com/Salahudheen0007/AI-Assignment>
* cd AI-Assignment


2.Create a virtual environment
* python -m venv venv


️3.Activate the environment
* Windows : venv\Scripts\activate
* Mac/Linux : source venv/bin/activate

4.Install dependencies
* pip install -r requirements.txt


5.Run the API
* uvicorn app:app --reload

Open in your browser:

http://127.0.0.1:8000/docs
## API Usage


POST /predict
### Example Input

Congratulations! You have won a free prize. Claim now!

### Output
```json
{
  "input": "Congratulations! You have won a free prize. Claim now!",
  "prediction": "Spam"
}
