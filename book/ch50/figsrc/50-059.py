import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'indice $[G : H]$ = nombre de paquets', 'resultat', 'm')
text(ax, 44, 59, r'$[G : H] = |G|\,/\,|H| = 12\,/\,3 = 4$', 'resultat', 'l')
rows = [('sujet', r'$H = \{0, 4, 8\}$', 0), ('varie', r'décalé de 1 : $\{1, 5, 9\}$', 1),
        ('varie', r'décalé de 2 : $\{2, 6, 10\}$', 2), ('varie', r'décalé de 3 : $\{3, 7, 11\}$', 3)]
n = 0
for k, (role, lab, s) in enumerate(rows):
    y = 46 - k * 10
    for j in range(3):
        disc(ax, 8 + j * 7.5, y, 2.6, role); n += 1
    text(ax, 28, y, lab, role, 's', ha='left')
assert n == 12
line(ax, [(78, 49), (80, 49), (80, 19), (78, 19)], 'resultat')
text(ax, 84, 34, '4', 'resultat', 'l', weight='bold', ha='center')
text(ax, 44, 10, '4 paquets de 3 = 12 éléments', 'encre', 's')
save(fig, '50-059')
