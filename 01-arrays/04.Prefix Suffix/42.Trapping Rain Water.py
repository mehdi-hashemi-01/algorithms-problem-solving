#42. Trapping Rain Water

height = [4, 2, 0, 3, 2, 5]

n = len(height)

left_max = [0] * n
right_max = [0] * n

# -------------------------
# 1) Prefix Maximum
# -------------------------

left_max[0] = height[0]

for i in range(1, n):
    if left_max[i - 1] > height[i]:
        left_max[i] = left_max[i - 1]
    else:
        left_max[i] = height[i]
    # left_max[i] = max(left_max[i - 1], height[i])

# -------------------------
# 2) Suffix Maximum
# -------------------------

right_max[n - 1] = height[n - 1]

for i in range(n - 2, -1, -1):
    if right_max[i + 1] > height[i]:
        right_max[i] = right_max[i + 1]
    else:
        right_max[i] = height[i]
    # right_max[i] = max(right_max[i + 1], height[i])

# -------------------------
# 3) Calculate Water
# -------------------------

water = 0

for i in range(n):
    # water += min(left_max[i], right_max[i]) - height[i]
    if left_max[i] < right_max[i]:
        water_level = left_max[i]
    else:
        water_level = right_max[i]

    current_water = water_level - height[i]

    water += current_water


print("left_max  =", left_max)
print("right_max =", right_max)
print("water     =", water)