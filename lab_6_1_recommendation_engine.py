# === Movie Recommendation System (Content-Based Filtering) ===
# This script recommends movies by comparing their genres using text vectorization
# and cosine similarity — a common technique in content-based recommendation engines.

import pandas as pd
from sklearn.feature_extraction.text import (
    CountVectorizer,
)  # Converts text into word-count vectors
from sklearn.metrics.pairwise import (
    cosine_similarity,
)  # Measures similarity between vectors (0 = no match, 1 = identical)

# --- Dataset ---
# A small sample of movies, each tagged with a genre description.
# In a real system, this would come from a database or CSV file.
movies = pd.DataFrame(
    {
        "title": [
            "Star Quest",
            "Galaxy War",
            "Love in Paris",
            "Robot Future",
            "Mystery Manor",
            "Action Strike",
            "Space Journey",
            "Romantic Escape",
        ],
        "genre": [
            "sci-fi adventure",
            "sci-fi action",
            "romance drama",
            "sci-fi thriller",
            "mystery thriller",
            "action thriller",
            "sci-fi adventure",  # Shares both words with "Star Quest" — expect high similarity
            "romance comedy",
        ],
    }
)

# --- Step 1: Vectorize the genre text ---
# CountVectorizer scans all genre strings and builds a vocabulary of unique words
# (e.g. ["action", "adventure", "comedy", "drama", "mystery", "romance", "sci-fi", "thriller"]).
# Each movie's genre is then represented as a vector of word counts.
# Example: "sci-fi adventure" → [0, 1, 0, 0, 0, 0, 1, 0]
#                          ^action ^adventure     ^sci-fi
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(
    movies["genre"]
)  # Returns a sparse matrix: (num_movies × num_unique_words)

# --- Step 2: Compute pairwise cosine similarity ---
# Cosine similarity compares the angle between two vectors rather than their magnitude.
# This means "sci-fi adventure" and "sci-fi adventure" score 1.0 (identical),
# while "romance drama" and "sci-fi action" score 0.0 (no shared words).
# The result is an (8×8) matrix where similarity[i][j] is the score between movie i and movie j.
# The diagonal is always 1.0 since every movie is identical to itself.
similarity = cosine_similarity(genre_matrix)

# --- Output ---
# Prints the raw similarity matrix. In a real app, you'd use this to find the
# top-N most similar movies to a given title — the recommendation step.
print(f"similarity: {similarity}")


"""
NOTES:
Sparse matrix: genre_matrix stores only non-zero values for efficiency — most movies won't contain most words, so storing all the zeros would waste memory.

Cosine similarity vs. Euclidean distance: Cosine similarity is preferred here because it focuses on which words appear, not how many times, making short and long genre strings comparable.

fit_transform: fit builds the vocabulary from the data; transform applies it. Calling both together with fit_transform is standard practice when working with a single dataset.
"""

# a function that returns recommendations
def recommend_movie(title, data, sim_matrix):
    if title not in data["title"].values:
        return ["Movie not found."]
    
    index = data[data["title"] == title].index[0]
    scores = list(enumerate(sim_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i, score in scores[1:4]:
        recommendations.append(data.iloc[i]["title"])
    
    return recommendations

result = recommend_movie("Star Quest", movies, similarity)

print("Because you liked Star Quest:")
for item in result:
    print("-", item)