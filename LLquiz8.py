items = input().split()
target = input()

count = 0
for item in items:
    if item == target:
        count += 1
print(count)