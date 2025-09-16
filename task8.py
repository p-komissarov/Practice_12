words = input().split()
words.sort(key=len)
print(" ".join(words))