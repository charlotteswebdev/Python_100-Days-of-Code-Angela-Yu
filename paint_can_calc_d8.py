import math
def paint_calc(height, width, cover):
    area = (height * width) / cover
    num_of_cans = (math.ceil(area))
    if num_of_cans <= 1:
        print(f"You'll need {num_of_cans} can of paint.")
    else:
        print(f"You'll need {num_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

