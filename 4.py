with open('./input/4.txt') as f:
    c = 0
    for elfenpaar in f.read().split("\n"):
        g1,g2,g3,g4 = int(elfenpaar.split(sep=',')[0].split('-')[0]),int(elfenpaar.split(sep=',')[0].split('-')[1]),int(elfenpaar.split(sep=',')[1].split('-')[0]),int(elfenpaar.split(sep=',')[1].split('-')[1])
        l,l2 = [i for i in range(g1,g2+1)],[i for i in range(g3,g4+1)]
        if ', '+', '.join(map(str, l))+',' in ', '+', '.join(map(str, l2))+',' or ', '+', '.join(map(str, l2))+',' in ', '+', '.join(map(str, l))+',':
            c += 1
    print(c)