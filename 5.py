import re
c = []
d = []
instr = []

with open('./input/5.txt') as f:
    for lijn in f.read().split("\n"):
        print(lijn)
        #print(len(lijn))
        for i in range(2, len(lijn),4):
            c.append(lijn[i-1])

with open('./input/5a.txt') as f2:
    for lijn in f2.read().split("\n"):
        instr.append(lijn)
        #print(lijn)

c = [c[x:x+9] for x in range(0, len(c),9)]

for i in range(len(c[0])):
    row =[]
    for item in c:
        row.append(item[i])
    d.append(row)
c = []
for lijst in d:
    lijst = lijst[0:8]
    doeMaarVerder = True
    while doeMaarVerder is True:
        try:
            lijst.remove(' ')
        except:
            doeMaarVerder = False
    #lijst.reverse()
    c.append(lijst)

print(c)
def getTopStackStringBaby(d):
    c = []
    for x in d:
        c.append(x[-1:][0])
    return ''.join(map(str, c))

def moveStackPiece(c, fromStack, toStack):
    try:
        tmpSf = c[fromStack][0]
        c[fromStack].pop(0)
        c[toStack].insert(0,tmpSf)
        return c
    except:
        print('SOMETHING WONG',c,fromStack,toStack)
        return c

def parseInstruc(instr):
    pass

#print(getTopStackStringBaby(c))
print(c)
for instruction in instr:
    #print(instruction)
    x = re.findall("\d",instruction)
    x = list(map(int,x))
    print(x)
    amount = x[0]
    for i in range(0,amount-1):
        fromStack  =  x[1]-1
        toStack = x[2]-1
        c = moveStackPiece(c,fromStack,toStack)




#moveStackPiece(c,4,3)
print(c)