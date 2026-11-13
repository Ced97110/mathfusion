import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(75)
box(ax, 4, 54, 26, 12, 'sujet', label='$a=2+i$')
arrow(ax, (31, 60), (44, 60), 'varie'); text(ax, 37.5, 65, r'$\rho$', 'varie')
mat(ax, 64, 60, [['2', '$-1$'], ['1', '2']], 'sujet', 8)
arrow(ax, (17, 53), (17, 29), 'varie'); arrow(ax, (64, 53), (64, 41), 'varie')
box(ax, 4, 16, 26, 12, 'resultat', label='$g(a)=0$')
text(ax, 37.5, 22, r'$\Leftrightarrow$', 'encre', 'l')
text(ax, 64, 36, r'$g(\rho(a))$', 'resultat', 's')
mat(ax, 64, 22, [['0', '0'], ['0', '0']], 'resultat', 8)
save(fig, '77-041')
