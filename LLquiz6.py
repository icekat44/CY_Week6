numbers = list(map(int, input().split()))

largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num
print(largest)