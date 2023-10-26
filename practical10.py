import pandas as pd
import matplotlib.pyplot as plt

from mlxtend.frequent_patterns import apriori

# Create a DataFrame for the transaction dataset
data = pd.DataFrame({
    'Transaction ID': [1, 2, 3, 4, 5],
    'Items': [
        'Milk, Bread',
        'Bread, Butter, Jam',
        'Milk, Bread, Butter',
        'Bread, Jam',
        'Milk, Jam'
    ]
})

# Perform one-hot encoding to convert the items into binary format
data_encoded = data['Items'].str.get_dummies(', ')

# Concatenate the one-hot encoded columns with the original DataFrame
data = pd.concat([data['Transaction ID'], data_encoded], axis=1)

# Apply Apriori algorithm to find frequent item sets with a minimum support threshold
min_support = 0.2  # You can adjust this threshold as needed
frequent_itemsets = apriori(data.drop('Transaction ID', axis=1), min_support=min_support, use_colnames=True)

# Count the occurrence of each frequent itemset
itemset_counts = data_encoded.sum()

# Create a bar chart to visualize itemset counts
plt.bar(itemset_counts.index, itemset_counts.values)
plt.xlabel('Frequent Itemsets')
plt.ylabel('Count')
plt.title('Frequent Itemset Counts')
plt.xticks(rotation=45)
plt.show()

# Display frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)
