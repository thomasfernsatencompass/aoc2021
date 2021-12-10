puzzle ="""
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""".splitlines()
puzzle = [[[set(z) for z in y.split(" ")] for y in x.split(" | ")] for x in puzzle if x]

uniquedigits = {2:1, 4:4, 3:7, 7:8}
part1ans = 0
for _, code in puzzle:
    for c in code:
        if len(c) in uniquedigits:
            part1ans += 1
print(f'part 1: {part1ans}')

part2ans = 0
for enc, code in puzzle:
    enc = sorted(enc, key=len)
    one, four, seven, eight = enc.pop(0), enc.pop(1), enc.pop(0), enc.pop()
    dm = {1:one, 4:four, 7:seven, 8:eight}
    up = (dm[7] - dm[4]).pop()

    lo5s = enc[:3]
    lo6s = enc[-3:]

    r1, r2 = None, None
    for lo6 in lo6s:
        diff = dm[1] - lo6
        if len(diff) == 1:
            dm[6] = lo6
            r1 = diff.pop()
            r2 = (dm[1] - set(r1)).pop()
        elif len(diff) == 0:
            leftmid = dm[4] - dm[1]
            if leftmid <= lo6:
                dm[9] = lo6
            else:
                dm[0] = lo6

    for lo5 in lo5s:
        diff = dm[1] - lo5
        if len(diff) == 0:
            dm[3] = lo5
            continue
        diff = lo5 - set(r1)
        if len(diff) == 5:
            dm[5] = lo5
        elif len(diff) == 4:
            dm[2] = lo5

    md = {''.join(sorted(list(v), key=str.lower)):str(k) for k,v in dm.items()}

    digit = ''
    for c in [''.join(sorted(list(cset), key=str.lower)) for cset in code]:
       digit += md[c]
    part2ans += int(digit)
print(f'part 2: {part2ans}')

    
