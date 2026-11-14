import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(62)
mat(ax, 20, 40, [['0', '$-1$'], ['1', '0']], 'sujet', 9)
mat(ax, 68, 40, [['0', '1'], ['$-1$', '0']], 'autre', 9)
arrow(ax, (33, 40), (54, 40), 'varie')
text(ax, 43.5, 45, 'change de base', 'varie', 's')
text(ax, 43.5, 35, r'$\neq$', 'limite', 'l')
text(ax, 20, 26, r'$\rho(i)$', 'sujet')
text(ax, 68, 26, r'$\Delta^{-1}\rho(i)\Delta$', 'autre')
arrow(ax, (20, 22), (34, 16.5), 'fixe'); arrow(ax, (68, 22), (54, 16.5), 'fixe')
box(ax, 14, 5, 60, 11, 'resultat', label=r'même action : $\times\ i$')
save(fig, '77-033')
