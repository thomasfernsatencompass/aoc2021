i = """199
200
208
210
200
207
240
269
260
263""".splitlines()

i = [int(x) for x in i]
part1 = len([x for x in range(1, len(i)) if i[x] > i[x-1]])
print(f"part 1: {part1}")

part2 = 0
prev_sum = i[0] + i[1] + i[2]
for x in range(1, len(i) - 2):
    next_sum = i[x] + i[x+1] + i[x+2]
    if next_sum > prev_sum:
        part2 += 1
    prev_sum = next_sum
print(f"part 2: {part2}")
