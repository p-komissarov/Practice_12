text = input()
m = c = 0
p = None

for i in text:
    if i == p:
        c += 1
        m = max(m, c)
    else:
        c = 1
        p = i

print(m)