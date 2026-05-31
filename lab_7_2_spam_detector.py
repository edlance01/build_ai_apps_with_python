import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
    "message": [
        "Win a free iPhone now",
        "Congratulations, you have won a prize",
        "Call me when you get this",
        "Let's meet tomorrow",
        "Limited time offer, click now",
        "Are we still on for today?"
    ],
    "label": [1, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

model = MultinomialNB()
model.fit(X,y)

test_message = ["You have won a free ticket"]
test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

print("Spam" if prediction[0] == 1 else "Not Spam")
