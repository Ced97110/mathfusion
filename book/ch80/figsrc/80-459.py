import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
ca, cl = 26, 62
va = [0, 0, 1, 1]
text(ax, ca, 57, r'$a$', 'sujet', 'l', weight='bold'); text(ax, cl, 57, 'lampe', 'resultat', 'l', weight='bold')
for i, v in enumerate(va):
    y = 44 - i * 12
    box(ax, ca - 7, y - 4.5, 14, 9, 'sujet', label=str(v))
    box(ax, cl - 7, y - 4.5, 14, 9, 'resultat', label=str(v))
    line(ax, [(ca + 8.5, y), (cl - 8.5, y)], 'fixe', lw=1.0)
    text(ax, (ca + cl) / 2, y + 2.4, '=', 'fixe', 'm')
save(fig, '80-459')
