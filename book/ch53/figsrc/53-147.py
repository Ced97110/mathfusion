import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'Alice signe avec sa clé privée', 'encre', 'm', weight='bold')
text(ax, 44, 53, r'clé privée $d = 27$, horloge $n = 55$', 'fixe', 'm')
for y, m, s in ((28, 8, 2), (10, 3, 42)):
    box(ax, 2, y, 18, 10, 'sujet', label=rf'$m = {m}$')
    box(ax, 68, y, 18, 10, 'resultat', label=rf'$s = {s}$')
    arrow(ax, (21, y + 5), (67, y + 5), 'varie')
    text(ax, 44, y + 9, rf'${m}^{{27}}$ : reste par 55', 'varie', 's')
text(ax, 44, 3, 'même opération, autre message', 'fixe', 's')
save(fig, '53-147')
