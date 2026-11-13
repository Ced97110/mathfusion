import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(58)
cx, cy, cw, ch = 26, 28, 13, 9
box(ax, cx - cw, cy, cw, ch, 'sujet'); box(ax, cx, cy - ch, cw, ch, 'sujet')
box(ax, cx, cy, cw, ch, 'fixe'); box(ax, cx - cw, cy - ch, cw, ch, 'fixe')
mat(ax, cx, cy, [['2', '$-1$'], ['1', '2']], 'fixe', cw, ch, roles=[['sujet', 'fixe'], ['fixe', 'sujet']])
text(ax, 26, 43, 'la diagonale en bleu', 'sujet', 's')
arrow(ax, (42, 28), (50, 28), 'fixe')
box(ax, 52, 21, 32, 14, 'resultat', label=r'$\mathrm{tr}\,M=2+2=4$', size='s')
save(fig, '77-048')
