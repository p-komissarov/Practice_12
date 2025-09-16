text = input()

m = c = 0

for i in text:
    if i == " ":
        c += 1
        m = max(m, c)
    else:
        c = 0
        
print(m)