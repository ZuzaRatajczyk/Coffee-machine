score = int(input())
max_score = int(input())

if score >= (0.9 * max_score):
    print("A")
elif score >= (0.8 * max_score):
    print("B")
elif score >= (0.7 * max_score):
    print("C")
elif score >= (0.6 * max_score):
    print("D")
else:
    print("F")