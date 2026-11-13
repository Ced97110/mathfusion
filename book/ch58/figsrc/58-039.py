import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, ch = 9.0, 8.0
rows = [(50, 'n = 2', ['2', '1']), (36, 'n = 1', ['7']), (22, 'n = 0', [])]
for y, lab, vals in rows:
    text(ax, 14, y + ch / 2, lab, 'encre', 'm')
    for i, s in enumerate(vals): box(ax, 30 + i * cw, y, cw, ch, 'sujet', label=s, r=0.6)
    if not vals:
        box(ax, 30, y, cw, ch, 'fixe', fill=False, dash=True, r=0.6)
        text(ax, 54, y + ch / 2, 'liste vide', 'fixe', 's', ha='left')
text(ax, 54, 50 + ch / 2, '2 cases', 'fixe', 's', ha='left')
text(ax, 54, 36 + ch / 2, '1 case', 'fixe', 's', ha='left')
box(ax, 20, 4, 48, 11, 'resultat', label=r'$R^{(0)} = \{0\}$ : 1 seule liste', size='s')
arrow(ax, (34.5, 22), (34.5, 15.5), 'resultat')
save(fig, '58-039')
