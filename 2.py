inputFile = './input/2.txt'
d = []
puntentotaal = 0

with open(inputFile) as f:
    d = f.read().split("\n")

def matchPuntCalculator9000(matchString):
    if 'A X' in matchString:
        return 4
    if 'A Y' in matchString:
        return 8
    if 'A Z' in matchString:
        return 3
    if 'B X' in matchString:
        return 1
    if 'B Y' in matchString:
        return 5
    if 'B Z' in matchString:
        return 9
    if 'C X' in matchString:
        return 7
    if 'C Y' in matchString:
        return 2
    if 'C Z' in matchString:
        return 6
    else:
        return 0

for x in range(0,len(d)):
    puntentotaal += matchPuntCalculator9000(d[x])
print(puntentotaal)

### pt2

def matchPuntCalculator9001(matchString):
    if 'A X' in matchString:
        return 3
    if 'A Y' in matchString:
        return 4
    if 'A Z' in matchString:
        return 8
    if 'B X' in matchString:
        return 1
    if 'B Y' in matchString:
        return 5
    if 'B Z' in matchString:
        return 9
    if 'C X' in matchString:
        return 2
    if 'C Y' in matchString:
        return 6
    if 'C Z' in matchString:
        return 7
    else:
        return 0

puntentotaal = 0
for x in range(0,len(d)):
    puntentotaal += matchPuntCalculator9001(d[x])
print(puntentotaal)