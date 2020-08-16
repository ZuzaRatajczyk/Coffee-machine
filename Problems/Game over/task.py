scores = input().split()
incorrect = scores.count('I')
i = 0
c = 0
if incorrect < 3:
    print('You won')
    print(scores.count('C'))
else:
    print('Game over')
    for score in scores:
        if score == 'C':
            c += 1
        else:
            i += 1
            if i == 3:
                break
    print(c)
