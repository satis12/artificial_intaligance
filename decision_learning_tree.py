import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

# Load the CSV data
data = pd.read_csv('restaurant_waiting.csv')

# Prepare the features and target variable
X = data[['Party Size', 'Reservation Time', 'Arrival Time', 'Wait Time (minutes)']].copy()
y = data['Table Assigned']

# Convert date/time columns to Unix timestamps
X['Reservation Time'] = pd.to_datetime(X['Reservation Time']).apply(lambda x: x.timestamp())
X['Arrival Time'] = pd.to_datetime(X['Arrival Time']).apply(lambda x: x.timestamp())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Plot the decision tree and save it as a PNG file
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=X.columns.to_list(), class_names=None)  # Set class_names to None
plt.savefig('decision_tree_graph.png')
plt.show()
