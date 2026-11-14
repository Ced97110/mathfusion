import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for b, role, name, mi, n, v in [(30, 'sujet', 'Vous : 50 miles', 50, 2, '25'), (6, 'autre', 'Voisin : 100 miles', 100, 8, '12,5')]:
    wt = mi * 0.72
    wi = wt / n
    for g in range(n):
        box(ax, 8 + g * wi, b, wi, 8, role, label=v, size='s', r=0.4)
    text(ax, 8, b + 12, name, role, 'm', ha='left', weight='bold')
text(ax, 44, 52, 'miles pour 1 gallon', 'encre', 'm')
text(ax, 44, 2, 'chaque case = 1 gallon', 'fixe', 's')
save(fig, '09-002')
