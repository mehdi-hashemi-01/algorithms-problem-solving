# Question 69: Square with Both Diagonals

n = 9

for row in range(n):
    for col in range(n):

        # آیا خانه روی ضلع مربع است؟
        is_border = (
            row == 0
            or row == n - 1
            or col == 0
            or col == n - 1
        )

        # قطر اصلی از بالا-چپ به پایین-راست
        is_main_diagonal = row == col

        # قطر فرعی از بالا-راست به پایین-چپ
        is_secondary_diagonal = (
            row + col == n - 1
        )

        # ترکیب سه شرط
        if (
            is_border
            or is_main_diagonal
            or is_secondary_diagonal
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()