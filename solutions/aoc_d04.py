puzzle = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".splitlines()

call = [int(x.strip()) for x in puzzle[1].split(",")]

cards = [[int(i) for i in x.split(" ") if i.strip()] for x in puzzle[3:] if x.strip()]
cardsRows = [cards[x:x+5] for x in range(0, len(cards), 5)]

cardsColumns = []
for card in cardsRows:
    cardsColumn = []
    for x in range(0, len(card[0])):
        column = []
        for i in range(0, len(card)):
            column.append(card[i][x])
        cardsColumn.append(column)
    cardsColumns.append(cardsColumn)

allcallednumbers = set()
cardsthathavewon = []
for number in call:
    allcallednumbers.add(number)
    for x in range(0, len(cardsColumns)):
        if x not in [idx[0] for idx in cardsthathavewon]:
            found = False
            for i in range(0, len(cardsColumns[0])):
                if set(cardsColumns[x][i]).issubset(allcallednumbers) and not found:
                    cardsthathavewon.append([x, number, allcallednumbers.copy()])
                    found = True
            for i in range(0, len(cardsRows[0])):
                if set(cardsRows[x][i]).issubset(allcallednumbers) and not found:
                    cardsthathavewon.append([x, number, allcallednumbers.copy()])
                    found = True

def findtotal(cardwin):
    indx, number, allcallednumbers = cardwin
    allnumbersinlastwinningcard = set(sum(cardsColumns[indx], []))
    return sum(allnumbersinlastwinningcard - allcallednumbers) * number

part1ans = findtotal(cardsthathavewon[0])
print(f'part 1: {part1ans}')

part2ans = findtotal(cardsthathavewon[-1])
print(f'part 2: {part2ans}')