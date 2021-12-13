puzzle="""5421451741
3877321568
7583273864
3451717778
2651615156
6377167526
5182852831
4766856676
3437187583
3633371586""".splitlines()
puzzle = [[int(y) for y in x] for x in puzzle]
 
maxLenY = len(puzzle)
maxLenX = len(puzzle[0])

def getAdjacents(x, y):
    adjList = [(x-1, y-1), (x, y-1), (x+1, y-1),
               (x-1, y  ),           (x+1, y),
               (x-1, y+1), (x, y+1), (x+1, y+1)]
    viableAdjs = []
    for aX, aY in adjList:
        if aX < 0 or aX > (maxLenX-1):
            continue
        if aY < 0 or aY > (maxLenY-1):
            continue
        viableAdjs.append([aX, aY])
    return viableAdjs
 
def doStep():
    flashed = set()
    for y in range(maxLenY):
        for x in range(maxLenX):
            puzzle[y][x] += 1
    findAndFlash(flashed)

def findAndFlash(flashed):
    coords = {}
    for y in range(maxLenY):
        for x in range(maxLenX):
            coord = str([x, y])
            if puzzle[y][x] == 10 and coord not in flashed:
                coords[coord] = [x, y]
                flashed.add(coord)
    flashCoords(coords, flashed)

def flashCoords(coords, flashed):
    for coord in coords:
        x, y = coords[coord]
        flash(x, y)
        adjs = getAdjacents(x, y)
        for adjX, adjY in adjs:
            if puzzle[adjY][adjX] != 0:
                puzzle[adjY][adjX] += 1
                findAndFlash(flashed)

global flashes
flashes = 0
def flash(x, y):
    global flashes
    flashes += 1
    puzzle[y][x] = 0
 
step = 0
while True:
    step += 1
    doStep()
    
    if step == 100:
        part1ans = flashes
 
    allFlashed = True
    for y in range(maxLenY):
        for x in range(maxLenX):
            if puzzle[y][x] != 0:
                allFlashed = False

    if allFlashed:
        part2ans = step
        break
    
print(f'part 1: {part1ans}')
print(f'part 2: {part2ans}')
