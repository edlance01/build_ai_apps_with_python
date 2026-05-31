
import pandas as pd

ratings = pd.DataFrame({
    "user": ["A", "A", "A", "B", "B", "C", "C", "C"],
    "movie": [
        "Star Quest",
        "Galaxy War",
        "Robot Future",
        "Star Quest",
        "Action Strike",
        "Love in Paris",
        "Romantic Escape",
        "Mystery Manor"
    ],
    "liked": [1,1,1,1,1,1,1,1]
})

print(ratings)