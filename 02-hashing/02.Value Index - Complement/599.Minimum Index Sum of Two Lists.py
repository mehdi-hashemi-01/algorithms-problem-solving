#599. Minimum Index Sum of Two Lists

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]

list2 = [
    "Piatti",
    "The Grill at Torrey Pines",
    "Hungry Hunter Steakhouse",
    "Shogun"
]


# نگهداری اندیس هر رشته در لیست اول
index_map = {name: i for i, name in enumerate(list1)}

min_sum = float("inf")
result = []

for j, name in enumerate(list2):
    # رشته باید در هر دو لیست وجود داشته باشد
    if name not in index_map:
        continue

    index_sum = index_map[name] + j

    if index_sum < min_sum:
        # کمینهٔ جدید: پاسخ‌های قبلی کنار گذاشته می‌شوند
        min_sum = index_sum
        result = [name]

    elif index_sum == min_sum:
        # مجموع برابر: این رشته هم یکی از پاسخ‌هاست
        result.append(name)

print(result)