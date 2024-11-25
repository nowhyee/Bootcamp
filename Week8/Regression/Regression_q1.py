from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
data = pd.read_csv("iris.csv")
X = data.drop("Name", axis=1)  # Drop 'Name' column (target)
y = data["Name"]  # 'Name' is the target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit logistic regression
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Get probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# Try different thresholds
thresholds = [0.3, 0.5, 0.7]
for threshold in thresholds:
    y_pred = (y_proba >= threshold).astype(int)
    print(f"Threshold: {threshold}")
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted')}")
    print(f"Recall: {recall_score(y_test, y_pred, average='weighted')}\n")
