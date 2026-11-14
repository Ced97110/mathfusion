import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, v, role="sujet", cw=8, ch=6, size="m", roles=None):
    for r in range(2):
        for c in range(2):
            text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, v[r][c], roles[r][c] if roles else role, size)
    for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)):
        line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], role)

fig, ax = canvas(72)
R = [['sujet', 'fixe'], ['fixe', 'sujet']]
for cx, v, lab in ((22, [['2', '$-1$'], ['1', '2']], r'base $1,\ i$'), (66, [['2', '1'], ['$-1$', '2']], r'base $i,\ 1$')):
    box(ax, cx - 8, cy := 46, 8, 6, 'sujet'); box(ax, cx, cy - 6, 8, 6, 'sujet')
    mat(ax, cx, cy, v, 'sujet', 8, 6, roles=R)
    text(ax, cx, 58, lab, 'fixe', 's')
    text(ax, cx, 33, '$2+2=4$', 'resultat')
    arrow(ax, (cx, 30), (44, 17), 'resultat')
box(ax, 14, 5, 60, 12, 'resultat', label=r'trace de $2+i$ : $4$')
save(fig, '77-034')
