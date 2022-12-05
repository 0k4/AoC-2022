with open('./input/4.txt') as f:
    c = 0
    def zitLijstinLijst(A, B):
        return ', '.join(map(str, A)) in ', '.join(map(str, B))
    for elfenpaar in f.read().split("\n"):
        g1 = int(elfenpaar.split(sep=',')[0].split('-')[0])
        g2 = int(elfenpaar.split(sep=',')[0].split('-')[1])
        g3 = int(elfenpaar.split(sep=',')[1].split('-')[0])
        g4 = int(elfenpaar.split(sep=',')[1].split('-')[1])
        l,l2 = [i for i in range(g1,g2+1)],[i for i in range(g3,g4+1)]
        if zitLijstinLijst(l,l2) or zitLijstinLijst(l2,l):
            c += 1
    print(c)