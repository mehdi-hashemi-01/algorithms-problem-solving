#1732. Find the Highest Altitude

gain = [-5, 1, 5, 0, -7]

highest = 0
altitude = 0

for value in gain:
    altitude += value
    highest = max(highest, altitude)

print(highest)