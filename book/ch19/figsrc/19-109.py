import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
line(ax, [(6, 12), (82, 24)], 'sujet', lw=1.5); line(ax, [(6, 32), (82, 44)], 'autre', lw=1.5)
for x in (20, 44, 68):
    y0 = 12 + (x - 6) * 12 / 76
    arrow(ax, (x, y0), (x, y0 + 20), 'varie', both=True)
text(ax, 44, 56, 'même écart partout', 'varie', 'm')
text(ax, 14, 6, 'premier rail', 'sujet', 's', ha='left'); text(ax, 14, 50, 'second rail', 'autre', 's', ha='left')
box(ax, 54, 2, 30, 9, 'resultat', label='parallèles', size='m')
save(fig, '19-109')
