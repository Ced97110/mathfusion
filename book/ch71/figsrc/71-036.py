import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 4, 62, 'règle (€ par kilo)', 'fixe', 's', ha='left')
text(ax, 84, 62, 'panier de 1 kg ; 2 kg', 'fixe', 's', ha='right')
rows = ((46, 'sujet', r'$f$ : 2 ; 1', '4 €'), (28, 'autre', r'$g$ : 1 ; 3', '7 €'), (8, 'resultat', r'$f+g$ : 3 ; 4', '11 €'))
for y, r, a, b in rows:
    box(ax, 4, y, 34, 10, r, label=a); arrow(ax, (40, y + 5), (58, y + 5), 'fixe'); box(ax, 60, y, 22, 10, 'resultat', label=b)
text(ax, 21, 40, '+', 'encre', 'l'); text(ax, 21, 22, '=', 'encre', 'l')
text(ax, 71, 40, '+', 'encre', 'l'); text(ax, 71, 22, '=', 'encre', 'l')
save(fig, '71-036')
