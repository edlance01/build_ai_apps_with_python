import pandas as pd

# our data set shows correlation between hours studied and score
data = {
    "hours_studied": [1,2,3,4,5,6,7,8],
    "score": [15,20,30,40,50,65,70,85]
}

df = pd.DataFrame(data)

print(df)

# The thing we know (hours studied) and the thing we want to predict (score)
X = df[["hours_studied"]] # double brackets says, 8 rows / 1 column
y = df["score"]

# simple linear regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y) # Where learning happens

# Pass it as a DataFrame with the correct column name
prediction = model.predict(pd.DataFrame({"hours_studied": [5]}))
print(prediction)

"""
Key takeaway, you didn't use pure if/then logic e.g., if hours studied is 5 then score is 50.
Instead, you gave the system examples and let it figure it out itself.

STOP WRITING RULES, START TRAINING SYSTEMS

The pattern is: Data > Model > Training > Prediction
"""