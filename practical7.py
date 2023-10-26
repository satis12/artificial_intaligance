import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load your weather dataset
weather_data = pd.read_csv('weather_dataset.csv')

# Remove rows with missing values
weather_data.dropna(inplace=True)

# Prepare the data
X = weather_data[['Temperature (C)', 'Humidity (%)', 'Precipitation (mm)', 'Wind Speed (km/h)']]
y = weather_data['Weather Condition']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Vary the number of neighbors (k) from 1 to the size of the test set
k_values = list(range(1, len(X_test) + 1))
accuracy_scores = []

for k in k_values:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_scores.append(accuracy)

# Create a plot to visualize the effect of varying k on accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_scores, marker='o', linestyle='-')
plt.title('Effect of Number of Neighbors (k) on K-NN Accuracy (Weather Dataset)')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()
