def prefix_sum(nums):
    prefix = []
    running_sum = 0

    for number in nums:
        # اضافه‌کردن عدد فعلی به مجموع قبلی
        running_sum += number

        # ذخیرهٔ مجموع از ابتدای لیست تا این موقعیت
        prefix.append(running_sum)

    return prefix


print(prefix_sum([2, 4, 1, 3]))  # [2, 6, 7, 10]
print(prefix_sum([5, 1, 2]))     # [5, 6, 8]
print(prefix_sum([-1, 3, 2]))    # [-1, 2, 4]
print(prefix_sum([]))           # []




def build_prefix(nums):
    # صفر اولیه، مجموع صفر عنصر را نشان می‌دهد
    prefix = [0]

    for number in nums:
        # آخرین مجموع ذخیره‌شده + عدد فعلی
        new_sum = prefix[-1] + number
        prefix.append(new_sum)

    return prefix


def range_sum(prefix, left, right):
    # حذف مجموع عناصر قبل از ابتدای بازه
    return prefix[right + 1] - prefix[left]


prefix = build_prefix([2, 4, 1, 3, 5])
print(prefix)                   # [0, 2, 6, 7, 10, 15]
print(range_sum(prefix, 1, 3))   # 8

prefix = build_prefix([5, 2, 7, 1])
print(range_sum(prefix, 0, 2))   # 14

prefix = build_prefix([3, 6, 2, 8])
print(range_sum(prefix, 2, 3))   # 10





def count_left_sum_greater(nums):
    total_sum = sum(nums)
    left_sum = 0
    count = 0

    # آخرین عنصر باید در سمت راست باقی بماند
    for i in range(len(nums) - 1):
        # افزودن عنصر فعلی به بخش چپ
        left_sum += nums[i]

        # مجموع عناصر باقی‌مانده در سمت راست
        right_sum = total_sum - left_sum

        # فقط بزرگ‌تر بودن شمرده می‌شود
        if left_sum > right_sum:
            count += 1

    return count


print(count_left_sum_greater([5, 1, 2, 1]))  # 3
print(count_left_sum_greater([1, 2, 3, 4]))  # 1
print(count_left_sum_greater([4, 3, 1]))     # 1
print(count_left_sum_greater([5]))           # 0
print(count_left_sum_greater([]))            # 0