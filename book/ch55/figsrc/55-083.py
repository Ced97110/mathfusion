import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'pour les variables 1, 2, 3, 4', 'fixe', 's')
vals = [10, 35, 50, 24]
base = 18; sc = 0.95
line(ax, [(4, base), (84, base)], 'fixe')
for k, v in enumerate(vals, start=1):
    c = 14 + 20 * (k - 1)
    box(ax, c - 7, base, 14, v * sc, 'sujet')
    text(ax, c, base + v * sc + 4, str(v), 'sujet', 'm', weight='bold')
    text(ax, c, base - 4, rf'$e_{k}$', 'encre', 'm')
    text(ax, c, base - 10, rf'$k={k}$', 'fixe', 's')
save(fig, '55-083')
