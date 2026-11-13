import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def isobox(ax, a, b, c, origin, u, role):
    P = lambda x, y, z: iso(x, y, z, origin, u)
    poly(ax, [P(0,0,0), P(a,0,0), P(a,0,c), P(0,0,c)], role)
    poly(ax, [P(0,0,0), P(0,b,0), P(0,b,c), P(0,0,c)], role)
    poly(ax, [P(0,0,c), P(a,0,c), P(a,b,c), P(0,b,c)], role)
fig, ax = canvas(62)
o = (28, 12); u = 13
isobox(ax, 2, 1, 0.5, o, u, 'sujet')
p = iso(1, 0, 0, o, u); text(ax, p[0] + 3, p[1] - 3.2, '2 m', 'sujet', 's')
p = iso(0, 0.5, 0, o, u); text(ax, p[0] - 4, p[1] - 2.5, '1 m', 'sujet', 's')
p = iso(0, 1, 0.25, o, u); text(ax, p[0] - 1.5, p[1], '0,5 m', 'sujet', 's', ha='right')
text(ax, 68, 50, r'$V = 2 \times 1 \times 0{,}5$', 'sujet', 'm')
text(ax, 68, 40, r'$V = 1$ m³', 'resultat', 'l', weight='bold')
text(ax, 68, 30, '1 m³ = 1 000 L', 'resultat', 'l', weight='bold')
text(ax, 68, 21, 'volume du bassin', 'fixe', 's')
save(fig, '11-145')
