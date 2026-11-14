import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 5.0
def wire(o, rot):
    r = math.radians(rot)
    def P(x, y, z):
        return iso(x*math.cos(r)-y*math.sin(r), x*math.sin(r)+y*math.cos(r), z, o, u)
    X, Y, Z = 4, 3, 2
    V = [(a, b, c) for a in (0, X) for b in (0, Y) for c in (0, Z)]
    for p in V:
        for q in V:
            if sum(p[i] != q[i] for i in range(3)) == 1 and p < q:
                line(ax, [P(*p), P(*q)], 'fixe', lw=0.8)
    line(ax, [P(X,Y,0), P(0,0,Z)], 'resultat', lw=1.8)
    arrow(ax, P(0,0,0), P(0,0,Z+1.5), 'varie', lw=1.2)
wire((20, 26), 0); wire((64, 26), 50)
text(ax, 20, 56, 'avant', 'sujet', 's'); text(ax, 64, 56, 'après', 'sujet', 's')
text(ax, 44, 29, 'axe CG', 'varie', 's')
arrow(ax, (32, 34), (52, 34), 'varie', curve=-0.3)
for x in (20, 64):
    text(ax, x, 11, '≈ 5,39 m', 'resultat', 's'); text(ax, x, 5, '≈ 21,80°', 'resultat', 's')
save(fig, '27-130')
