# Question 67: Square with Main Diagonal

n = 10

for row in range(n):
    for col in range(n):

        # بررسی چهار ضلع مربع
        is_border = (
            row == 0
            or row == n - 1
            or col == 0
            or col == n - 1
        )

        # بررسی قطر اصلی
        is_main_diagonal = row == col

        # اگر خانه روی مرز یا قطر اصلی باشد
        if is_border or is_main_diagonal:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()