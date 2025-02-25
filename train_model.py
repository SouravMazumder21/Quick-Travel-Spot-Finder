import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (replace with your Kaggle dataset)
data = {
    'location': ['Beach', 'Mountain', 'City', 'Forest', 'Desert'],
    'temperature': [30, 15, 25, 20, 35],
    'popularity': [5, 4, 5, 3, 2],
    'label': [1, 0, 1, 0, 0]  # 1 = Recommended, 0 = Not Recommended
}

df = pd.DataFrame(data)

# Splitting data
X = df[['temperature', 'popularity']]
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
