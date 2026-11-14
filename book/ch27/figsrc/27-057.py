import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
u = 11
o = (39.3, 8)
P = lambda x, y, z: iso(x, y, z, o, u)
V = {'B': (0, 0, 0), 'A': (4, 0, 0), 'C': (0, 3, 0), 'D': (4, 3, 0),
     'F': (0, 0, 2), 'E': (4, 0, 2), 'G': (0, 3, 2), 'K': (4, 3, 2)}
def wire(role='fixe', lw=0.8):
    hidden = [('D', 'A'), ('D', 'C'), ('D', 'K')]
    edges = [('B', 'A'), ('B', 'C'), ('B', 'F'), ('A', 'E'), ('C', 'G'), ('F', 'E'), ('F', 'G'), ('E', 'K'), ('G', 'K')]
    for p, q in edges: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw)
    for p, q in hidden: line(ax, [P(*V[p]), P(*V[q])], role, lw=lw * 0.8, dash=True)
wire('fixe', 0.7)
pa, ph, pg = P(*V['A']), P(*V['C']), P(*V['G'])
poly(ax, [pa, ph, pg], 'sujet', lw=0.5)
line(ax, [ph, pg], 'sujet', lw=2.0)
line(ax, [pa, ph], 'fixe', lw=1.4)
line(ax, [pa, pg], 'fixe', lw=1.4)
s = 0.45
ua = (4 / 5, -3 / 5, 0)
sq = [(0, 0, 0), (s * ua[0], s * ua[1], 0), (s * ua[0], s * ua[1], s), (0, 0, s)]
line(ax, [P(*(V['C'][i] + q[i] for i in range(3))) for q in sq[1:]] , 'encre', lw=0.8)
disc(ax, *ph, 1.8, 'resultat')
disc(ax, *pg, 1.2, 'sujet'); disc(ax, *pa, 1.2, 'fixe')
text(ax, ph[0] - 4, ph[1] - 3, r'$H$', 'resultat', 'l')
text(ax, pg[0] - 3, pg[1] + 3, r'$G$', 'sujet', 'm')
text(ax, pa[0] + 3, pa[1] - 2.5, r'$A$', 'fixe', 'm')
text(ax, 6, 66, r'$H$ : pied', 'resultat', 'l', ha='left')
text(ax, 6, 60, 'sous le point G', 'resultat', 's', ha='left')
text(ax, 6, 56.5, 'ici, H est le coin C', 'fixe', 's', ha='left')
text(ax, ph[0] + 22, ph[1] + 17, 'angle droit en H', 'encre', 's')
arrow(ax, (ph[0] + 12, ph[1] + 14.5), (ph[0] + 2, ph[1] + 2.2), 'encre', lw=0.6)
save(fig, '27-057')
