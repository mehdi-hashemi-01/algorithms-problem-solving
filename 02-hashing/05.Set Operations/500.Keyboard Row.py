#500. Keyboard Row
words = ["Hello","Alaska","Dad","Peace"]

row1 = set("qwertyuiop")
row2 = set("asdfghjkl")
row3 = set("zxcvbnm")

# لیست کلمات قابل تایپ با یک ردیف
result = []

# بررسی تک تک کلمات
for word in words:

    # تبدیل حروف بزرگ به کوچک
    letters = set(word.lower())

    # آیا تمام حروف در یکی از سه ردیف هستند؟
    if (
        letters.issubset(row1)
        or letters.issubset(row2)
        or letters.issubset(row3)
    ):
        # حفظ شکل اصلی کلمه
        result.append(word)

print(result)

fst = set(('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'))
sec = set(('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'))
thd = set(('Z', 'X', 'C', 'V', 'B', 'N', 'M'))
ans = []

for word in words:

    fstflag = 1
    for l in word:
        if l.upper() not in fst:
            fstflag = 0
            break

    if fstflag:
        ans.append(word)
        continue

    secflag = 1
    for l in word:
        if l.upper() not in sec:
            secflag = 0
            break

    if secflag:
        ans.append(word)
        continue

    thdflag = 1
    for l in word:
        if l.upper() not in thd:
            thdflag = 0
            break

    if thdflag:
        ans.append(word)
        continue

print(ans)