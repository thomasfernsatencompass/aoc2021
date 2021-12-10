inputs = """forward 5
down 5
forward 8
up 3
down 8
forward 2
""".splitlines()

def yaxis(line):
    return line.startswith("up") or line.startswith("down")

def direction(line):
    if line.startswith("down") or line.startswith("forward"):
        return 1
    return -1

def number(line):
    return int(line.split(" ")[1])

totalYaxis = sum([number(x) * direction(x) for x in inputs if yaxis(x)])
totalXaxis = sum([number(x) * direction(x) for x in inputs if not yaxis(x)])
part1 = totalYaxis * totalXaxis
print(f"part 1: {part1}")

aim = 0
horizontal = 0
depth = 0
for line in inputs:
    if yaxis(line):
        aim += number(line) * direction(line)
    else:
        horizontal += number(line)
        depth += aim * number(line)
part2 = horizontal * depth
print(f"part 2: {part2}")


