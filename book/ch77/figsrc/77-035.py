import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(72)
mat(ax, 20, 50, [['2', '$-1$'], ['1', '2']], 'sujet', 8)
text(ax, 20, 62, r'$\rho(2+i)$', 'sujet')
text(ax, 22, 34, r'$2\times2-(-1)\times1=5$', 'resultat', 's')
o = (66, 14); s = 7
P = [o, (o[0] + 2 * s, o[1] + s), (o[0] + s, o[1] + 3 * s), (o[0] - s, o[1] + 2 * s)]
line(ax, [(54, 14), (84, 14)], 'fixe', 0.6); line(ax, [(66, 10), (66, 40)], 'fixe', 0.6)
poly(ax, P, 'resultat')
poly(ax, [o, (o[0] + s, o[1]), (o[0] + s, o[1] + s), (o[0], o[1] + s)], 'fixe')
text(ax, 69.5, 27, 'aire 5', 'resultat', 's')
text(ax, 70, 7, 'carré unité (aire 1)', 'fixe', 's')
save(fig, '77-035')
