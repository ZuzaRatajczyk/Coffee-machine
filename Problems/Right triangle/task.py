def area(a, b):
    s = 0.5 * a * b
    return s


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = area(leg_1, leg_2)

    def pythagorean_theorem(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            print(round(area(self.a, self.b), 1))
        else:
            print("Not right")


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

right_triangle = RightTriangle(input_c, input_a, input_b)
right_triangle.pythagorean_theorem()
