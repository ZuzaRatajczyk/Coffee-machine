n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
mean = sum(numbers) / n
print(mean)
