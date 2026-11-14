import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
for x in range(-3, 4):
    for y in range(6):
        if x == 0:
            role = 'sujet'
        elif y == 0:
            role = 'autre'
        else:
            role = 'fixe'
        disc(ax, 44 + 8 * x, 14 + 8 * y, 1.5, role)
box(ax, 44 - 4, 14 - 4, 8, 48, 'sujet', fill=False, dash=True)
box(ax, 44 - 28, 14 - 4, 56, 8, 'autre', fill=False, dash=True)
text(ax, 44, 64, 'tor M : tués par 6', 'sujet', 'm')
text(ax, 80, 14, 'L', 'autre', 'm')
text(ax, 44, 4, 'M = ℤ ⊕ ℤ/6 = tor M ⊕ L', 'encre', 'm')
save(fig, '60-075')
