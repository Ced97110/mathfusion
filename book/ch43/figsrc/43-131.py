import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pions(ax, x, y, n, role, w=24, h=13):
    box(ax, x, y, w, h, role)
    for i in range(n):
        r, c = divmod(i, 3)
        disc(ax, x + 5 + c * 7, y + h - 3.6 - r * 5.6 + 0.0, 1.9, 'fixe')
fig, ax = canvas(66)
xs = [3.5, 32, 60.5]
text(ax, 44, 61, 'Partition 1 : tailles différentes', 'sujet', 's')
for x, n in zip(xs, [4, 5, 3]):
    pions(ax, x, 40, n, 'sujet')
    text(ax, x + 12, 35.5, f'{n} pions', 'sujet', 's')
text(ax, 44, 27, 'Partition 2 : même taille', 'autre', 's')
for x in xs:
    pions(ax, x, 6, 4, 'autre')
    text(ax, x + 12, 1.8, '4 pions', 'autre', 's')
save(fig, '43-131')
