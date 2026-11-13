import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
for cx, name, n in ((22, 'Terre', 6), (66, 'Lune', 1)):
    text(ax, cx, 75, name, 'fixe', 'm', weight='bold')
    box(ax, cx - 13, 52, 26, 14, 'sujet', label='1 000 g', size='m')
    for k in range(n):
        arrow(ax, (cx, 52 - k * 4), (cx, 52 - (k + 1) * 4 + 0.2), 'varie', lw=1.4)
    text(ax, cx + 4, 46 if n == 1 else 34, 'poids', 'varie', 's', ha='left')
text(ax, 66, 36, '6 fois plus faible', 'varie', 's')
box(ax, 8, 3, 72, 9, 'resultat', label='même masse : 1 000 g', size='m')
save(fig, '11-052')
