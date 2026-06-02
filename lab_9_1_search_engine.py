from openai import OpenAI
import numpy as np


documents = [
    "Learn Python programming from scratch",
    "Affordable smartphones with great battery life",
    "Best laptops for developers",
    "Healthy recipes for quick meals",
    "How to build AI applications using Python",
    "Budget-friendly gadgets and tech deals"
]

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

doc_embeddings = [get_embedding(doc) for doc in documents]
#print(f"dc:{doc_embeddings[0]}")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query):
    query_embedding = get_embedding(query)

    scores = []

    for i, doc_embedding in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, doc_embedding)
        scores.append((documents[i], score))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return scores[:3]

#results = search("cheap tech gadgets")
results = search("fast cars")

for doc, score in results:
    print(f"{doc} (score: {score:.4f})")
