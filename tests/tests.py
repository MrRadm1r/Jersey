from collections import Counter
a = []
for i in range(1000):
    a.append(i//(1000/72))
print(Counter(Counter(a).values()))