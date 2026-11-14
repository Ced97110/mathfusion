import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 60, 57, 'circuit', 'sujet', 's'); text(ax, 78, 57, r"$a$ seul", 'autre', 's')
S = [('ouvert', 'ouvert', 0), ('ouvert', 'fermé', 0), ('fermé', 'ouvert', 1), ('fermé', 'fermé', 1)]
for i, (a, b, on) in enumerate(S):
    y = 46 - 12 * i
    text(ax, 2, y, rf"$a$ {a}, $b$ {b}", 'encre', 's', ha='left')
    for x in (60, 78): disc(ax, x, y, 3.4, 'resultat' if on else 'fixe')
disc(ax, 5, 5, 2.6, 'resultat'); text(ax, 10, 5, 'le courant passe', 'resultat', 's', ha='left')
disc(ax, 52, 5, 2.6, 'fixe'); text(ax, 57, 5, 'coupé', 'fixe', 's', ha='left')
save(fig, '80-425')
