s1 = input()
s2 = input()
s3 = input()
result = set()

for i in s1 + s2 + s3:
    if (i in s1) + (i in s2) + (i in s3) == 1:
        if i not in result:
            result.add(i)

print(result)

