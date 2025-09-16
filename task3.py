text = input().lower()
letters = set()

for i in text:
    if i not in letters and i.isalpha():
        letters.add(i)

print(len(letters))