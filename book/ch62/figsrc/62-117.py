import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# 5 elements go injectively into 5 places : every place is filled
text(ax, 44, 62, 'modulo 5 : 5 restes, 5 places', 'encre', 'm')
text(ax, 2, 50, r'$a$', 'sujet', 'l', ha='left')
text(ax, 2, 28, r'$a^5$', 'resultat', 'l', ha='left')
for k in range(5):
    x = 20 + k * 15
    disc(ax, x, 50, 4, 'sujet', label=str(k))
    arrow(ax, (x, 45.5), (x, 33.5), 'varie')
    box(ax, x - 5, 22, 10, 11, 'resultat', label=str(k ** 5 % 5))
text(ax, 44, 14, '5 images distinctes dans 5 places', 'encre', 's')
box(ax, 14, 2, 60, 9, 'resultat', label='aucune place vide', size='s')
save(fig, '62-117')
