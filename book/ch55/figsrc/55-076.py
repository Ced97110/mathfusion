import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$e_1$ = somme des variables', 'sujet', 'm')
for y, vals, role in ((48, (2, 3, 4), 'sujet'), (22, (3, 4, 2), 'autre')):
    for i, v in enumerate(vals):
        x = 14 + 20 * i
        disc(ax, x, y, 5, role, label=str(v), size='l')
        if i < 2: text(ax, x + 10, y, '+', 'encre', 'l')
    text(ax, 76, y, '= 9', 'resultat', 'l', weight='bold')
text(ax, 44, 35, 'autre ordre', 'fixe', 's')
save(fig, '55-076')
