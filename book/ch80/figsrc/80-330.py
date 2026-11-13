import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
heads = (r'$\mathcal{P}(\{s\})$', r'$\mathbb{Z}/2$', 'logique')
rows = ((38, 'fixe', (r'$\varnothing$', '0', 'faux')), (18, 'sujet', (r'$\{s\}$', '1', 'vrai')))
for i, c in enumerate((18, 44, 70)):
    text(ax, c, 58, heads[i], 'encre', 'm')
    for y, role, labs in rows: box(ax, c - 11, y, 22, 12, role, label=labs[i])
for y, role, labs in rows:
    for xa in (29, 55): line(ax, [(xa, y + 6), (xa + 4, y + 6)], role, dash=True)
text(ax, 44, 8, 'une structure, trois noms', 'encre', 's')
save(fig, '80-330')
