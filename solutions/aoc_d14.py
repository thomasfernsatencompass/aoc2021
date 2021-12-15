puzzle = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()

from collections import Counter

template = puzzle[0]
rules = [x.split(' -> ') for x in puzzle[2:]]
rules = {k:v for k, v in rules}
letters = {}

for l in template:
    letters[l] = 1 if not l in letters else letters[l] + 1

for letter in rules.values():
    if letter not in letters:
        letters[letter] = 0

pairs = {}
for index in range(len(template)-1):
    seq = template[index:index+2]
    pairs[seq] = 1 if not seq in pairs else pairs[seq] + 1

for step in range(40):
    for pair, amount in list(pairs.items()):
        val = rules[pair]
        newpairs = [pair[0] + val, val + pair[1]]
        pairs[pair] -= amount
        letters[val] += amount
        for p in newpairs:
            pairs[p] = amount if not p in pairs else pairs[p] + amount

    if step == 9:
        counts = [amt for _, amt in Counter(letters).most_common()]
        part1ans = counts[0] - counts[-1]
        print(f'part 1: {part1ans}')

counts = [amt for _, amt in Counter(letters).most_common()]
part2ans = counts[0] - counts[-1]
print(f'part 2: {part2ans}')
