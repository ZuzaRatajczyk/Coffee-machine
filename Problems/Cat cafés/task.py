# name = []
# number = []

cafe_dict = {}
while True:
    cat_cafe = input()
    if cat_cafe == "MEOW":
        break
    cat_cafe = cat_cafe.split()
    cafe_dict[cat_cafe[0]] = int(cat_cafe[1])
print(max(cafe_dict, key=cafe_dict.get))



#     name.append(cat_cafe[0])
#     number.append(int(cat_cafe[1]))
# max_cats = number.index(max(number))
# print(name[max_cats])
