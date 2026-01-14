import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("water_usage_data.csv")

# Features (inputs) and target (output)
X = data[['people', 'showers', 'laundry']]
y = data['usage']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = r2_score(y_test, y_pred)

# Prediction function
def predict_water_usage(people, showers, laundry):
    prediction = model.predict([[people, showers, laundry]])
    return prediction[0]

# Accuracy function
def get_model_accuracy():
    return accuracy
