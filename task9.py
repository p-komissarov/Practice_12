text = input().split()
words = set()
p = None

for word in text:
    if word in words:
        p = word
        break
    words.add(word)

print(p)

