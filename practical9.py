from itertools import combinations

# Function to generate candidate itemsets
def generate_candidates(itemset, k):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            union = list(set(itemset[i]) | set(itemset[j]))
            if len(union) == k:
                candidates.append(union)
    return candidates

# Function to prune infrequent itemsets
def prune_itemsets(itemset, candidates, min_support):
    frequent_itemset = []
    for candidate in candidates:
        count = 0
        for item in itemset:
            if set(candidate).issubset(set(item)):
                count += 1
        if count >= min_support:
            frequent_itemset.append(candidate)
    return frequent_itemset

# Function to find frequent itemsets using Apriori
def apriori(data, min_support):
    itemset = [[item] for item in data]
    k = 2
    frequent_itemsets = []
    
    while itemset:
        candidates = generate_candidates(itemset, k)
        frequent_itemset = prune_itemsets(data, candidates, min_support)
        
        if not frequent_itemset:
            break

        frequent_itemsets.extend(frequent_itemset)
        itemset = frequent_itemset
        k += 1
    
    return frequent_itemsets

# Example usage
data = ["A", "B", "C", "D", "A", "C", "D", "A", "D", "B", "C", "E"]
min_support = 2
result = apriori(data, min_support)
print("Frequent Itemsets:")
for itemset in result:
    print(itemset)
