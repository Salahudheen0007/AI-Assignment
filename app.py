# Task 4


from fastapi import FastAPI
import pickle
import nltk, string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

@app.post("/predict")
def predict(message: str):
    clean = clean_text(message)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]

    return {
        "input": message,
        "prediction": "Spam" if pred == 1 else "Not Spam"
    }
