puzzle = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".splitlines()

def findIntersecting(ignoreDiagonals):
    positions = []
    for line in [x for x in puzzle if x]:
        a, b = line.split(" -> ")
        a = [int(a) for a in a.split(",")]
        b = [int(b) for b in b.split(",")]
        positions.append([a, b])

    plottedpoints = []
    for position in positions:
        p1, p2 = position
        x1, y1 = p1
        x2, y2 = p2

        xMov = x2 - x1
        yMov = y2 - y1

        if ignoreDiagonals:
            if xMov != 0 and yMov != 0:
                continue

        xStep = 1 if xMov >= 0 else -1
        allXcoords = [x1 + x for x in range(0, xMov, xStep)]
        if len(allXcoords) == 0:
            allXcoords = [x1 for _ in range(abs(yMov))]
        allXcoords.append(x2)
            
        yStep = 1 if yMov >= 0 else -1
        allYcoords = [y1 + y  for y in range(0, yMov, yStep)]
        if len(allYcoords) == 0:
            allYcoords = [y1 for _ in range(abs(xMov))]
        allYcoords.append(y2)
        
        for idx in range(len(allXcoords)):
            plottedpoints.append([allXcoords[idx], allYcoords[idx]])

    plottedpointcount = {str(x):0 for x in plottedpoints}

    for plottedpoint in plottedpoints:
        plottedpointcount[str(plottedpoint)] += 1

    allintersectingcoords = [count for (coord,count) in plottedpointcount.items() if count > 1]
    return len(allintersectingcoords)


part1ans = findIntersecting(ignoreDiagonals=True)
print(f'part 1: {part1ans}')

part2ans = findIntersecting(ignoreDiagonals=False)
print(f'part 2: {part2ans}')