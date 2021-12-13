puzzle="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

openers = {'(':')', '[':']', '{':'}', '<':'>'}
points = {')':3, ']':57, '}':1197, '>':25137}

errors = []
remainingStacks = []
for line in puzzle:
    openStack = []
    hasError = False
    for char in line:
        if char in openers:
            openStack.append(char)
        else:
            latest = openStack.pop()
            if openers[latest] != char:
                hasError = True
                errors.append(char)
    if not hasError:
        remainingCloses = [openers[o] for o in openStack[::-1]]
        remainingStacks.append(remainingCloses)
part1ans = sum([points[e] for e in errors])
print(f'part 1: {part1ans}')

autocompleteScore = {')':1, ']':2, '}':3, '>':4}
stackScores = []
for stack in remainingStacks:
    stackScore = 0
    for char in stack:
        stackScore *= 5
        stackScore += autocompleteScore[char]
    stackScores.append(stackScore)
middleScore = sorted(stackScores)[int(len(stackScores)/2)]
print(f'part 2: {middleScore}')   
