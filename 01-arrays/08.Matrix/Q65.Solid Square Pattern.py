# Question 65: Solid Square Pattern

n = 10

# حلقه بیرونی برای سطرها
for row in range(n):

    # حلقه داخلی برای ستون‌ها
    for col in range(n):

        # تمام خانه‌ها ستاره دارند
        print("*", end=" ")

    # پایان هر سطر
    print()