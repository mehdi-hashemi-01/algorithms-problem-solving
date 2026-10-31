# Question 17: Descending Number Pattern

start = 7

# حلقه بیرونی: تعیین عدد شروع هر سطر
for row in range(start, 0, -1):

    # حلقه داخلی: چاپ اعداد از row تا 1
    for num in range(row, 0, -1):
        print(num, end=" ")

    # رفتن به سطر بعد
    print()