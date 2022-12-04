from collections import Counter

abcd = {'A': 58, 'B': 25, 'C': 53,'D': 56, 'E': 86, 'F': 69}
 
b = Counter(abcd)
high = b.most_common(3)
 
print("Dictionary with 3 highest values:")
 
for c in high:
    print(c[0]," :",c[1]," ")