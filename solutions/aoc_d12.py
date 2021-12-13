puzzle="""mj-TZ
start-LY
TX-ez
uw-ez
ez-TZ
TH-vn
sb-uw
uw-LY
LY-mj
sb-TX
TH-end
end-LY
mj-start
TZ-sb
uw-RR
start-TZ
mj-TH
ez-TH
sb-end
LY-ez
TX-mt
vn-sb
uw-vn
uw-TZ""".splitlines()
puzzle=[x.split("-") for x in puzzle]
 
routeMap = {}
for start, end in puzzle:
    if end != 'start':
        if start in routeMap:
            routeMap[start].append(end)
        else:
            routeMap[start] = [end]
    if start != 'start':
        if end in routeMap:
            routeMap[end].append(start)
        else:
            routeMap[end] = [start]
del routeMap['end']
 
def hasDupe(path):
    path = [p for p in path if p.lower() == p][1:]
    for cave in path:
        if path.count(cave) == 2:
            return True
    return False 
 
def traverse(paths, cave, part2=False, p=['start'], v=[]):
    visited, path = v.copy(), p.copy()
    if cave not in routeMap:
        path.append('end')
        paths.append(path)
    else:
        if cave == cave.lower():
            if hasDupe(path) or not part2:
                path.append(cave)
                if cave not in visited:
                    visited.append(cave)
                    for ncave in routeMap[cave]:
                        traverse(paths, ncave, part2, path, visited)
            else:
                path.append(cave)
                visited.append(cave)
                for ncave in routeMap[cave]:
                    traverse(paths, ncave, part2, path, visited)
        else: # uppercase
            for ncave in routeMap[cave]:
                traverse(paths, ncave, part2, path, visited)

part1paths = []
part2paths = []
for route in routeMap['start']:
    traverse(part1paths, route, part2=False)
    traverse(part2paths, route, part2=True)
 
print(f'part 1: {len(part1paths)}')
print(f'part 2: {len(part2paths)}')
