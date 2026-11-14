import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, 'sans lettre : à chaque fois', 'fixe', 's')
for x0 in (3, 31, 59):
    box(ax, x0, 47, 26, 10, 'fixe', label='le nombre 2 + 3 i', size='s')
text(ax, 44, 38, r'on pose $z = 2 + 3\,i$', 'varie', 'm')
text(ax, 44, 29, 'avec la lettre', 'sujet', 's')
for x0 in (10, 38, 66):
    box(ax, x0, 14, 12, 10, 'sujet', label=r'$z$', size='m')
text(ax, 44, 5, r'en général $z = a + b\,i$', 'sujet', 's')
save(fig, '39-041')
