puzzle = "16,1,2,0,4,2,7,1,2,14".split(",")
puzzle = [int(x) for x in puzzle]

bot, top = min(puzzle), max(puzzle)

def findFuelUsed(num):
    total = 0
    for x in range(1, num+1):
        total += x
    return total

def solve(part2=False):
    fuel_counts = [0 for _ in range(bot, top)]
    for x in range(bot, top):
        for pos in puzzle:
            distance = abs(pos - (x+1))
            fuel_counts[x] += findFuelUsed(distance) if part2 else distance
    return min(fuel_counts)

part1ans = solve()                   
print(f'part 1: {part1ans}')

part2ans = solve(part2=True)
print(f'part 2: {part2ans}')
                           
            
