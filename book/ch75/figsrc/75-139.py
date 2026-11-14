import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 22, 52, 'permutations de 3 objets', 'sujet', 's'); text(ax, 66, 52, 'entiers modulo 6', 'autre', 's')
for i in range(3):
    for j in range(2):
        disc(ax, 14 + 8 * i, 40 - 8 * j, 3, 'sujet'); disc(ax, 58 + 8 * i, 40 - 8 * j, 3, 'autre')
text(ax, 22, 26, '6 éléments', 'sujet', 's'); text(ax, 66, 26, '6 éléments', 'autre', 's')
box(ax, 5, 11, 34, 9, 'limite', label=r'$ab\neq ba$', size='m'); box(ax, 49, 11, 34, 9, 'resultat', label=r'$a+b=b+a$', size='m')
text(ax, 44, 4, 'même nombre, groupes différents', 'encre', 's')
save(fig, '75-139')
