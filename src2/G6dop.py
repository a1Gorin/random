import random
arr = []
for i in range(1, 5):
    arr.append(input())
random.shuffle(arr)
arr.sort(key=lambda x: x.lower())
print(arr)