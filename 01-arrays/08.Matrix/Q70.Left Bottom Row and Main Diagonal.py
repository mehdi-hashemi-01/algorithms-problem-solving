# Question 70: Left Column, Bottom Row and Main Diagonal

n = 10

for row in range(n):
    for col in range(n):

        # بررسی ستون اول
        is_first_column = col == 0

        # بررسی سطر آخر
        is_last_row = row == n - 1

        # بررسی قطر اصلی
        is_main_diagonal = row == col

        # چاپ ستاره اگر حداقل یک شرط برقرار باشد
        if (
            is_first_column
            or is_last_row
            or is_main_diagonal
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()