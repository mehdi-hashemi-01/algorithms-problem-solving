# Question 66: Boundary Square Pattern

n = 10

for row in range(n):
    for col in range(n):

        # بررسی مرزهای مربع
        is_top = row == 0
        is_bottom = row == n - 1
        is_left = col == 0
        is_right = col == n - 1

        # ستاره فقط روی مرزها چاپ می‌شود
        if is_top or is_bottom or is_left or is_right:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()