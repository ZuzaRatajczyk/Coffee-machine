word = input()
if not word.islower():
    snake_case = word
    positions = []
    for position, char in enumerate(snake_case):
        if char.isupper():
            positions.extend([position])
    i = 0
    for position in positions:
        position = int(position)
        if i >= 1:
            position += 1
        snake_case = snake_case[:position] + "_" + snake_case[position:]
        i += 1
    print(snake_case.lower())
else:
    print(word)
