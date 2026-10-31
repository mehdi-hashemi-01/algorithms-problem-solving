#1346. Check If N and Its Double Exist
arr = [3, 1, 7, 11]
seen = set()

for num in arr:
    # آیا دو برابر عدد فعلی قبلاً دیده شده است؟
    if 2 * num in seen:
        print(True)

    # آیا نصف عدد فعلی قبلاً دیده شده است؟
    if num % 2 == 0 and num // 2 in seen:
        print(True)

    # ذخیره پس از بررسی، برای جلوگیری از مقایسه با خودش
    seen.add(num)

print(True)