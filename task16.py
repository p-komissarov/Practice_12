text = input()
balance = 0

for i in text:
    if i == '(':
        balance += 1
    elif i == ')':
        balance -= 1

print(balance == 0)