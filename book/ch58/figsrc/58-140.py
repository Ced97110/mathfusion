import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 5.0
def grid(ox, oy):
    P = lambda x, y: (ox + x * u, oy + y * u)
    for k in range(0, 5):
        line(ax, [P(0, k), P(6, k)], 'fixe', lw=0.3, dash=True)
    for k in range(0, 7):
        line(ax, [P(k, 0), P(k, 4)], 'fixe', lw=0.3, dash=True)
    return P
tgt = (5, 4)
PL = grid(6, 16)
arrow(ax, PL(0, 0), PL(5, 0), 'sujet', lw=1.4)
arrow(ax, PL(5, 0), PL(5, 4), 'autre', lw=1.4)
disc(ax, *PL(*tgt), 1.3, 'resultat')
PR = grid(52, 16)
arrow(ax, PR(0, 0), PR(5, 0), 'sujet', lw=1.4)
line(ax, [PR(-0.3, 0), PR(6.3, 0)], 'sujet', lw=1.8)
disc(ax, *PR(*tgt), 1.3, 'limite')
text(ax, 22, 58, r'$(1,0)$ et $(0,1)$', 'encre', 'm')
text(ax, 66, 58, r'$(1,0)$ seul', 'encre', 'm')
text(ax, 22, 8, r'atteint $(5,4)$ :', 'resultat', 's')
text(ax, 22, 3.5, r'$5\times(1,0)+4\times(0,1)$', 'resultat', 's')
text(ax, 66, 8, r'n’atteint pas $(5,4)$', 'limite', 's')
text(ax, 66, 3.5, 'seulement l’axe horizontal', 'limite', 's')
text(ax, PL(5, 4)[0] + 2, PL(5, 4)[1] + 3.5, r'$(5,4)$', 'resultat', 's', ha='right')
text(ax, PR(5, 4)[0] + 2, PR(5, 4)[1] + 3.5, r'$(5,4)$', 'limite', 's', ha='right')
save(fig, '58-140')
