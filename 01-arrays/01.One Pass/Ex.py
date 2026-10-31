def max_consecutive_even(nums):
    current_count = 0
    best_count = 0

    for num in nums:
        # باقی‌ماندهٔ تقسیم عدد زوج بر ۲ برابر صفر است
        if num % 2 == 0:
            current_count += 1

            # ثبت رکورد جدید در صورت افزایش طول بخش زوج
            best_count = max(best_count, current_count)
        else:
            # عدد فرد، پیوستگی اعداد زوج را قطع می‌کند
            current_count = 0

    return best_count


print(max_consecutive_even([2, 4, 5, 6, 8, 10, 3]))  # 3
print(max_consecutive_even([1, 3, 5, 7]))             # 0
print(max_consecutive_even([2, 4, 6, 8]))             # 4
print(max_consecutive_even([]))                     # 0




def count_increasing_steps(nums):
    count = 0

    # از اندیس ۱ شروع می‌کنیم؛ عنصر اول، عنصر قبلی ندارد
    for i in range(1, len(nums)):
        current = nums[i]
        previous = nums[i - 1]

        # فقط افزایش واقعی شمرده می‌شود؛ برابری کافی نیست
        if current > previous:
            count += 1

    return count


print(count_increasing_steps([3, 5, 4, 8, 10]))  # 3
print(count_increasing_steps([5, 4, 3, 2]))      # 0
print(count_increasing_steps([1, 2, 3, 4]))      # 3
print(count_increasing_steps([2, 2, 3]))         # 1
print(count_increasing_steps([]))                # 0




def max_increase(nums):
    # برای تشکیل یک جفت، حداقل دو عنصر لازم داریم
    if len(nums) < 2:
        return 0

    minimum_so_far = nums[0]
    best_increase = 0

    for j in range(1, len(nums)):
        current = nums[j]

        # اختلاف عدد فعلی با کمترین عددِ قبل از آن
        increase = current - minimum_so_far

        # نگهداری بیشترین افزایش مثبت
        best_increase = max(best_increase, increase)

        # عدد فعلی می‌تواند کمینهٔ جدید برای عناصر بعدی باشد
        minimum_so_far = min(minimum_so_far, current)

    return best_increase


print(max_increase([8, 3, 6, 2, 7]))   # 5
print(max_increase([9, 7, 5, 3]))      # 0
print(max_increase([4, 2, 10, 1, 6]))  # 8
print(max_increase([4, 2, 10,19, 1, 6]))  # 8
print(max_increase([5]))               # 0
print(max_increase([]))                # 0



