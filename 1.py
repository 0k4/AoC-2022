inputFile = './input/1.txt'
maxLoad = 0

with open(inputFile) as f:
    d = f.read().split("\n\n")

for x in d:
    load = 0
    y = (x.split("\n"))
    for nummer in range(0,len(y)):
        load += int(y[nummer])
    if load > maxLoad:
        maxLoad = load

print(maxLoad)

#### pt2
maxLoad = 0
loads = []

for x in d:
    load = 0
    y = (x.split("\n"))
    for nummer in range(0,len(y)):
        load += int(y[nummer])
    # tussendoor de sommen ook bijhouden
    loads.append(load)
    if load > maxLoad:
        maxLoad = load
    
# sommen sorteren en som van top 3 returnen
loads = sorted(loads)[-3:]
print(sum(list(filter(lambda x: (x),loads))))