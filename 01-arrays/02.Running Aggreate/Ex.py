def running_score(changes):
    running_sum = 0
    result = []

    for change in changes:
        # اعمال تغییر فعلی روی مجموع قبلی
        running_sum += change

        # ذخیرهٔ امتیاز پس از این تغییر
        result.append(running_sum)

    return result


print(running_score([3, -1, 4, -2]))  # [3, 2, 6, 4]
print(running_score([5, 2, 1]))       # [5, 7, 8]
print(running_score([-2, -3, 4]))     # [-2, -5, -1]
print(running_score([]))             # []



def highest_running_balance(changes):
    current_balance = 0

    # موجودی اولیه نیز یکی از موجودی‌های مشاهده‌شده است
    max_balance = 0

    for change in changes:
        # محاسبهٔ موجودی جدید
        current_balance += change

        # اگر موجودی جدید رکورد بیشتری دارد، آن را ذخیره می‌کنیم
        if current_balance > max_balance:
            max_balance = current_balance

    return max_balance


print(highest_running_balance([4, -2, 5, -6, 3]))  # 7
print(highest_running_balance([-2, -3, -1]))       # 0
print(highest_running_balance([2, 3, -1, 4]))      # 8
print(highest_running_balance([]))                 # 0




def first_running_sum_at_least(nums, target):
    running_sum = 0

    # دریافت هم‌زمان اندیس و مقدار هر عنصر
    for index, number in enumerate(nums):
        running_sum += number

        # اولین نقطه‌ای که مجموع به حد موردنظر می‌رسد
        if running_sum >= target:
            return index

    # اگر حلقه تمام شود و شرط هیچ‌وقت برقرار نشده باشد
    return -1


print(first_running_sum_at_least([2, 3, 1, 4], 6))  # 2
print(first_running_sum_at_least([1, 1, 1], 5))     # -1
print(first_running_sum_at_least([5, 2, 3], 4))     # 0
print(first_running_sum_at_least([], 6))            # -1

