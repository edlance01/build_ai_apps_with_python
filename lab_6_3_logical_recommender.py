import pandas as pd

# --- Dataset ---
# A small product catalog with names, descriptive tags, and prices.
# Tags are plain-text keywords that will be used to measure similarity between products.
products = pd.DataFrame(
    {
        "name": [
            "Wireless Earbuds",
            "Noise Cancelling Headphones",
            "Bluetooth Speaker",
            "Gaming Mouse",
            "Mechanical Keyboard",
            "Smart Watch",
            "Fitness Tracker",
            "USB Microphone",
        ],
        "tags": [
            "audio portable music",
            "audio premium music",
            "audio portable party",
            "gaming computer accessories",
            "gaming typing computer",
            "wearable fitness tech",
            "wearable health fitness",
            "audio recording creator",
        ],
        "price": [49, 100, 79, 29, 89, 149, 59, 99],
    }
)

# --- Similarity Matrix ---
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# CountVectorizer converts each product's tags into a word-count vector.
# For example, "audio portable music" becomes a vector counting occurrences
# of every unique word across all products.
vectorizer = CountVectorizer()
tag_matrix = vectorizer.fit_transform(products["tags"])

# Compute cosine similarity between every pair of products.
# The result is an NxN matrix where similarity[i][j] is a score from 0 to 1 —
# 1 means the products share identical tags, 0 means no overlap at all.
similarity = cosine_similarity(tag_matrix)


# --- Recommendation Function ---
def recommend_product(name, data, sim_matrix, max_price=None):
    """
    Returns up to 3 product recommendations similar to the given product.

    Args:
        name (str):         The product name to base recommendations on.
        data (DataFrame):   The product catalog with "name", "tags", and "price" columns.
        sim_matrix:         Precomputed cosine similarity matrix for all products.
        max_price (float):  Optional price ceiling — products above this are skipped.

    Returns:
        list[str]: Up to 3 recommended products as "Name - $price" strings,
                   or an error message if the product isn't found.
    """

    # Guard clause: exit early if the requested product doesn't exist
    if name not in data["name"].values:
        return ["Product not found."]

    # Find the row index of the requested product in the DataFrame
    index = data[data["name"] == name].index[0]

    # Pair each product's index with its similarity score to the requested product
    scores = list(enumerate(sim_matrix[index]))

    # Sort by similarity score descending so the closest matches come first
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    # Skip index 0 (the product itself always has a perfect similarity score of 1.0)
    for i, score in scores[1:]:
        item = data.iloc[i]

        # If a price limit was set, skip any products that exceed it
        if max_price is not None and item["price"] > max_price:
            continue

        # Format the recommendation as "Product Name - $price"
        recommendations.append(f"{item['name']} - ${item['price']}")

        # Stop once we have 3 recommendations
        if len(recommendations) == 3:
            break

    return recommendations


# --- Example Usage ---

# Find products similar to "Wireless Earbuds" that cost $89 or less
result = recommend_product("Wireless Earbuds", products, similarity, max_price=89)

print("Recommended products:")
for item in result:
    print("-", item)
