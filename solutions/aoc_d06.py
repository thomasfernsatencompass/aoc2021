puzzle = "3,4,3,1,2"

fishes = [int(x) for x in puzzle.split(",")]

def findTotal(days):
    fishAmt = [0 for _ in range(10)]
    for fish in fishes:
        fishAmt[fish] += 1

    for day in range(days):
        lastDayFishes = fishAmt[0]
        
        for i in range(9):
            fishAmt[i] = fishAmt[i+1]

        fishAmt[8] = lastDayFishes
        fishAmt[6] += lastDayFishes

    return sum(fishAmt)

part1ans = findTotal(80)
print(f'part 1: {part1ans}')

part2ans = findTotal(256)
print(f'part 2: {part2ans}')
