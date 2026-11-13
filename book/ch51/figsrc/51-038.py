import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
box(ax, 4, 56, 20, 14, 'sujet', label='$-a$', size='xl')
arrow(ax, (26, 63), (33, 63), 'fixe')
text(ax, 35, 66.5, 'l’élément qui, ajouté à a,', 'encre', 'm', ha='left')
text(ax, 35, 59.5, 'donne 0', 'resultat', 'm', ha='left', weight='bold')
for x, head, l1, l2 in [(2, 'cadran à 4 heures', 'a = 1  ;  −a = 3', '1 + 3 = 4, soit 0'),
                        (45, 'entiers', 'a = 5  ;  −a = −5', '5 + (−5) = 0')]:
    box(ax, x, 18, 41, 30, 'fixe')
    text(ax, x + 20.5, 42, head, 'sujet', 's', weight='bold')
    text(ax, x + 20.5, 33, l1, 'encre', 'm')
    text(ax, x + 20.5, 24, l2, 'resultat', 'm')
text(ax, 44, 8, 'même signe −a, deux mondes', 'fixe', 'm')
save(fig, '51-038')
