#For Part 1
horizontal = 0
vertical = 0
for item in a:
    [direction, unit] = item.split(" ")
    unit = int(unit)
    if direction == 'forward':
        horizontal += unit
    if direction == 'up':
        vertical -= unit
    if direction == 'down':
        vertical += unit
answer = horizontal * vertical
print(answer)
#For Part 2
aim = 0
horizontal2 = 0
vertical2 = 0
for item in a:
    [direction, unit] = item.split(" ")
    unit = int(unit)
    if direction == 'forward':
        horizontal2 += unit
        vertical2 += aim*unit
    if direction == 'up':
        aim -= unit
    if direction == 'down':
        aim += unit

answer2 = horizontal2 * vertical2
print(answer2)
