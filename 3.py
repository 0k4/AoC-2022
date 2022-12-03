inputFile = './input/3.txt'
d = []
puntentotaal = 0

with open(inputFile) as f:
    d = f.read().split("\n")

def commonLetter(inputstring):
    lenInput = len(inputstring)
    pt1 = inputstring[0:lenInput//2]
    pt2 = inputstring[lenInput//2:]
    for letter in pt1:
        if letter in pt2:
            return letter
    return -1

def returnLetterScore(inputLetter):
    inputLetter = str(inputLetter)
    if inputLetter.islower():
        return (ord(inputLetter) - 96)
    if inputLetter.isupper():
        return (ord(inputLetter) - 38)

for rugzak in d:
    puntentotaal += int(returnLetterScore(commonLetter(rugzak)))

print(puntentotaal)

##PT 2
def returnGroupLetter(rugzakkenLijst):
    alleZakken = ''.join(rugzakkenLijst)
    for letter in alleZakken:
        if letter in rugzakkenLijst[0] and letter in rugzakkenLijst[1] and letter in rugzakkenLijst[2]:
            return letter

# reset
puntentotaal = 0

# classic for loop met 3 step
for i in range(0,len(d),3):
    a = [d[i],d[i+1],d[i+2]]
    puntentotaal += returnLetterScore(returnGroupLetter(a))

print(puntentotaal)