puzzle="""
2199943210
3987894921
9856789892
8767896789
9899965678
""".splitlines()
puzzle = [x for x in puzzle if x]
puzzle = [[int(y) for y in x] for x in puzzle]

maxLenY = len(puzzle)
maxLenX = len(puzzle[0])

def gAdjs(x, y):
    adjList = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    viableAdjs = []
    for adj in adjList:
        aX, aY = adj
        if aX < 0 or aX > (maxLenX-1):
            continue
        if aY < 0 or aY > (maxLenY-1):
            continue
        viableAdjs.append(adj)
    return viableAdjs

minimums = []
part1ans = 0
for y in range(maxLenY):
    for x in range(maxLenX):
        value, adjs = puzzle[y][x], gAdjs(x, y)
        found = True
        for adjX, adjY in adjs:
            adjValue = puzzle[adjY][adjX]
            if adjValue <= value:
                found = False
        if found:
            minimums.append([x, y, value])
            part1ans += value + 1
print(f'part 1: {part1ans}')

seenCoords = set()
def gBasin(x, y, value, coords):
    if str([x, y]) in seenCoords:
        return
    else:
        seenCoords.add(str([x, y]))
    adjacents = gAdjs(x, y)
    for adjacent in adjacents:
        adjacentX, adjacentY = adjacent
        adjacentValue = puzzle[adjacentY][adjacentX]
        if adjacentValue >= value and adjacentValue != 9:
            coords.add(str([adjacent]))
            gBasin(adjacentX, adjacentY, adjacentValue, coords)

lengths = []
for x, y, value in minimums:
    coords = set([str([x, y])])
    gBasin(x, y, value, coords)
    lengths.append(len(coords))
lengths = sorted(lengths)

part2ans = 1
for length in lengths[-3:]:
    part2ans *= length
print(f'part 2: {part2ans}')

    
