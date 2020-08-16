# Make sure your output matches the assignment *exactly*
num_of_hours = int(input())

if num_of_hours < 2:
    print("That seems reasonable")
elif num_of_hours < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")