numbers = list(map(int, input().split()))

for number in numbers:
    if number > 100:
        break
    if number <= 0:
        continue
    print(number)