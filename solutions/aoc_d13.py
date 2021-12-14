dots, folds="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n\n")
dots, folds = dots.splitlines(), folds.splitlines()
dots = [[int(d) for d in dot.split(",")] for dot in dots]
folds = [f[11:].split('=') for f in folds]
folds = [[direction, int(num)] for direction, num in folds]

maxX = max([d for d,_ in dots])
maxY = max([d for _,d in dots])

block = [['.' for _ in range(maxX+1)] for _ in range(maxY+1)]

for x, y in dots:
    block[y][x] = '#'

def combine(part1, part2): # assumes part1 and part2 are same size
    for y in range(len(part2)):
        for x in range(len(part2[0])):
            if part2[y][x] == '#':
                part1[y][x] = '#'
    return part1      
    
def fold(direction, num):
    if direction == 'y':
        part1, part2 = block[:num], block[num+1:][::-1]
        diff = len(part1) - len(part2) # accounts for different sized splits (only on y axis)
        if diff > 0:
            part2 = [['.' for _ in range(len(part2[0]))] for _ in range(diff)] + part2
    elif direction == 'x':
        part1, part2 = [], []
        for y in range(len(block)):
            part1.append([block[y][x] for x in range(num)])
            part2.append([block[y][x] for x in range(num+1, len(block[0]))][::-1])
    return combine(part1, part2)

def countDots(block):
    dots = 0
    for line in block:
        for char in line:
            if char == '#':
                dots += 1
    return dots

totalFolds = 0
for direction, num in folds:
    totalFolds += 1 
    block = fold(direction, num)
    if totalFolds == 1:
        part1ans = countDots(block)

print(f'part 1: {part1ans}')

part2ans = '\n'.join([''.join(b) for b in block])
print(f'part 2:\n{part2ans}')
