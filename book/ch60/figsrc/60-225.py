import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
u = 9
rows = [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
for k, ps in enumerate(rows):
    y = 60 - 11 * k; x = 5
    role = 'varie' if ps == [2, 2] else 'sujet'
    for p in ps:
        box(ax, x, y, u * p - 1.2, 8, role, label=str(p))
        x += u * p
text(ax, 66, 63, r'$P(4)=5$', 'resultat', 'l', weight='bold')
text(ax, 66, 38, 'part répétée', 'varie', 's')
arrow(ax, (57, 38), (44, 38), 'varie')
save(fig, '60-225')
