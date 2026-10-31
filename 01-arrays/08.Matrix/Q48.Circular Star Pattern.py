# Question 48: Circular Star Pattern

n = int(input("Enter an odd number: "))

if n < 5 or n % 2 == 0:
    print("Please enter an odd number >= 5.")

else:
    for row in range(n):

        for col in range(n):

            # اولین و آخرین سطر:
            # سه ستاره در مرکز چاپ می‌شوند.
            if row == 0 or row == n - 1:
                condition = (
                    n // 2 - 1 <= col <= n // 2 + 1
                )

            # سطر دوم و سطر ماقبل آخر:
            # دو ستاره نزدیک هر طرف چاپ می‌شوند.
            elif row == 1 or row == n - 2:
                condition = col in (
                    1, 2, n - 3, n - 2
                )

            # سایر سطرها:
            # فقط دو طرف دایره ستاره دارند.
            else:
                condition = col == 0 or col == n - 1

            if condition:
                print("*", end="")
            else:
                print(" ", end="")

        print()