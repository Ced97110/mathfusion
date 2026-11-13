import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cols = [('Longueur', ['pouces', 'pieds', 'yards', 'miles']), ('Masse', ['onces', 'livres', 'tonnes']), ('Capacité', ['cuillères', 'tasses', 'pintes', 'gallons'])]
for c, (h, us) in enumerate(cols):
    x = 3 + c * 28.5
    box(ax, x, 45, 26, 8, 'sujet', label=h, size='m', weight='bold')
    for r, u in enumerate(us):
        box(ax, x + 2, 34 - r * 9, 22, 7.5, 'fixe', label=u, size='s')
save(fig, '11-021')
