import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [18, 44, 70]
for x, t, r in zip(cols, ['gallons', 'miles', 'miles ÷ gallons'], ['varie', 'varie', 'resultat']):
    text(ax, x, 56, t, r, 's', weight='bold')
rows = [(1, 25), (2, 50), (4, 100)]
for i, (g, m) in enumerate(rows):
    y = 36 - i * 15
    box(ax, 10, y, 16, 10, 'varie', label=str(g))
    box(ax, 36, y, 16, 10, 'varie', label=str(m))
    box(ax, 62, y, 16, 10, 'resultat', label='25', weight='bold')
    arrow(ax, (27, y + 5), (35, y + 5), 'fixe'); arrow(ax, (53, y + 5), (61, y + 5), 'fixe')
save(fig, '09-113')
