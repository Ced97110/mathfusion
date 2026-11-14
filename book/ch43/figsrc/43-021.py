import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for x, big, lab in ((16, r'$a$', 'premier nombre'), (44, r'$R$', 'la règle'), (72, r'$b$', 'second nombre')):
    text(ax, x, 54, big, 'sujet' if big != r'$R$' else 'varie', 'xl')
    text(ax, x, 45, lab, 'encre', 's')
    line(ax, [(x, 50), (x, 47)], 'fixe')
box(ax, 4, 20, 38, 12, 'resultat', label=r'$2\ R\ 5$ : oui')
box(ax, 46, 20, 38, 12, 'limite', label=r'$5\ R\ 2$ : non')
text(ax, 44, 10, 'règle : plus petit que', 'fixe', 's')
text(ax, 44, 37, "l'ordre compte", 'encre', 's')
save(fig, '43-021')
