words = input().split()
first = words[0]
res = []

for word in words:
    if word != first and len(word) == len(set(word)):
        res.append(word)

print(res)