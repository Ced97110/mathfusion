import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
for i in range(5):
    for j in range(5):
        disc(ax, 5 + 6 * i, 28 + 6 * j, 1.0, 'fixe')
text(ax, 17, 20, 'éléments : une\ninfinité', 'fixe', 's')
text(ax, 32.6, 40, '≠', 'encre', 'l')
box(ax, 35, 31, 26, 18, 'sujet', label='une base\n(1, 0), (0, 1)', size='s')
text(ax, 48, 25, '2 éléments', 'sujet', 's')
arrow(ax, (61, 40), (68, 40), 'resultat')
box(ax, 68, 31, 18, 18, 'resultat', label='rang\n= 2')
text(ax, 64, 12, 'même nombre pour\ntoutes les bases', 'resultat', 's')
save(fig, '58-067')
