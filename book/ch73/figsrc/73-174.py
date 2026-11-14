import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x in (15, 57): line(ax, [(x, 24), (x, 42)], 'sujet', lw=1.8)
box(ax, 19, 24, 34, 18, 'fixe', fill=False, dash=True)
for x, l in [(27, '0'), (36, '1'), (45, '2')]: disc(ax, x, 33, 3.2, 'autre', label=l)
text(ax, 36, 47, 'un ensemble', 'autre', 's'); text(ax, 70, 33, '= 3', 'resultat', 'xl')
text(ax, 70, 41, 'un nombre', 'resultat', 's')
brace(ax, 15, 57, 22, 'sujet', label='nombre d’éléments de', down=True)
save(fig, '73-174')
