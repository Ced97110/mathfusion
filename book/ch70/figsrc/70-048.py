import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, ch, x0 = 22, 11, 26
text(ax, 14, 48, r'$r-s$', 'fixe', 'm')
for j, (s, v) in enumerate([(r'$s=2$', 2), (r'$s=3$', 3)]):
    text(ax, x0 + j * cw + cw / 2, 48, s, 'autre', 'm')
cells = [[('−1', 'fixe'), ('−2', 'fixe')], [('0', 'varie'), ('−1', 'fixe')]]
for i, rname in enumerate([r'$r=1$', r'$r=2$']):
    y = 31 - i * 12
    text(ax, 14, y + ch / 2, rname, 'sujet', 'm')
    for j in range(2):
        s, role = cells[i][j]
        box(ax, x0 + j * cw + 0.5, y, cw - 1, ch, role, label=s, size='l', weight='bold' if role == 'varie' else 'normal')
box(ax, 14, 6, 60, 10, 'resultat', label=r'produit $=0$ : la paire $(2,\ 2)$', size='s')
save(fig, '70-048')
