c = 0
while True:
    ticket = input().strip()
    c += 1
    digits = [int(i) for i in ticket]
    n = len(digits)
    
    if n % 2 == 0:
        half = n // 2
        sum1 = sum(digits[:half])
        sum2 = sum(digits[half:])
        if sum1 == sum2:
            print(c)
            break