puzzle = "16,1,2,0,4,2,7,1,2,14".split(",")
puzzle = [int(x) for x in puzzle]

bot, top = min(puzzle), max(puzzle)

def findFuelUsed(num, better=False):
    if not better:
        total = 0
        for x in range(1, num+1):
            total += x
        return total
    return int(((num*num) + num) / 2)

def solve(part2=False, better=False):
    fuel_counts = [0 for _ in range(bot, top)]
    for x in range(bot, top):
        for pos in puzzle:
            distance = abs(pos - (x+1))
            fuel_counts[x] += findFuelUsed(distance, better) if part2 else distance
    return min(fuel_counts), fuel_counts.index(min(fuel_counts)) + 1

part1ans, median = solve()         
print(f'part 1: {part1ans, median}')

part2ans, mean = solve(part2=True, better=True)
print(f'part 2 better: {part2ans, mean}')

part2ans, mean = solve(part2=True)
print(f'part 2: {part2ans, mean}')                           
            
