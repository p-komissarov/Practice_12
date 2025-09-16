secret = input()

for _ in range(25): 
    print()

for attempt in range(10):
    guess = input()
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for i in guess if i in secret) - bulls
    print(f"Быков: {bulls} Коров: {cows}")
    if bulls == 4:
        print("Победа!")
        break
else:
    print("Проигрыш!")