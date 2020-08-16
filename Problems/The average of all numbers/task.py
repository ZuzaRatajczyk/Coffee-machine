# put your python code here
a = int(input())
b = int(input())
numbers = []
for i in range(a, b):
    if i % 3 == 0:
        numbers.extend([i])
if b % 3 == 0:
    num     bers.extend([b])
mean = sum(numbers) / len(numbers)
print(mean)
