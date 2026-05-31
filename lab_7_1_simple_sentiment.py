import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Very happy with the service",
        "I hate this",
        "This is terrible",
        "Worst experience ever"
    ],
    "label": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
# note that the model doesn't see "love" or "terrible" as words.
# It sees them as posistions in a vector, and the presence or absence of thos words becomes a signal
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Now we can train a model on top of that
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X,y) # the model learns which words tend to appear in positive vs negative sentences

# testing it
test_text = ["I really love this"]
test_vector = vectorizer.transform(test_text)

prediction = model.predict(test_vector)

print("Prediction:", "Positive" if prediction[0] == 1 else "Negative")