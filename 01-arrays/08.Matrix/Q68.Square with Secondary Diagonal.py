# Question 68: Square with Secondary Diagonal

n = 10

for row in range(n):
    for col in range(n):

        # بررسی مرزهای مربع
        is_border = (
            row == 0
            or row == n - 1
            or col == 0
            or col == n - 1
        )

        # بررسی قطر فرعی
        is_secondary_diagonal = (
            row + col == n - 1
        )

        # چاپ ستاره روی مرز یا قطر فرعی
        if is_border or is_secondary_diagonal:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()