lower_limit = int(input())
upper_limit = int(input())
ann = int(input())

if lower_limit <= ann <= upper_limit:
    print("Normal")
else:
    if ann < lower_limit:
        print("Deficiency")
    else:
        print("Excess")
