import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 2, 50, 41, 12, 'sujet', label=r'$(2,3)+(4,5)=(6,8)$', size='s')
box(ax, 45, 50, 41, 12, 'sujet', label=r'$(4,5)+(2,3)=(6,8)$', size='s')
text(ax, 44, 67, 'même résultat dans les deux ordres', 'fixe', 's')
for x, lab in [(22.5, r'$2+4=4+2$'), (65.5, r'$3+5=5+3$')]:
    arrow(ax, (x, 49), (x, 36), 'varie')
    box(ax, x - 18, 22, 36, 13, 'resultat', label=lab)
text(ax, 22.5, 17, 'première place', 'fixe', 's')
text(ax, 65.5, 17, 'seconde place', 'fixe', 's')
text(ax, 44, 7, 'règle déjà connue dans les entiers', 'fixe', 's')
save(fig, '51-082')
