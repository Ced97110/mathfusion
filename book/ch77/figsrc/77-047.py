import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, r'multiplier par $2+i$', 'encre', 's')
box(ax, 24, 18, 20, 16, 'sujet'); box(ax, 44, 18, 20, 16, 'varie')
text(ax, 34, 50, r'$1\mapsto 2+i$', 'sujet', 's'); text(ax, 54, 50, r'$i\mapsto -1+2i$', 'varie', 's')
arrow(ax, (34, 47), (34, 35), 'sujet'); arrow(ax, (54, 47), (54, 35), 'varie')
cx, cy, cw, ch = 44, 26, 20, 8
for r, row in enumerate([['2', '$-1$'], ['1', '2']]):
    for c, t in enumerate(row): text(ax, cx + (c - 0.5) * cw, cy + (0.5 - r) * ch, t, ['sujet', 'varie'][c])
for s, e in ((cx - cw, 1.6), (cx + cw, -1.6)): line(ax, [(s + e, cy + ch), (s, cy + ch), (s, cy - ch), (s + e, cy - ch)], 'fixe')
text(ax, 11, 26, r'$\rho(2+i)$', 'encre', 's')
save(fig, '77-047')
