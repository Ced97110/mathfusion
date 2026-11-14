import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
# left: E (16 elements) over F (4 elements), basis of 2 elements ; right: 3 non-zero elements form a group
text(ax, 22, 78, r'$[E:F]$ = dimension', 'sujet', 'm')
box(ax, 3, 36, 38, 36, 'sujet', label=None)
text(ax, 22, 66, 'E : 16 éléments', 'sujet', 's')
box(ax, 8, 40, 28, 16, 'autre', label='F : 4 éléments', size='s')
text(ax, 22, 29, 'base de 2 éléments', 'varie', 's')
for i in range(2):
    disc(ax, 17 + i * 10, 21, 2.6, 'varie')
text(ax, 22, 11, 'dimension 2', 'varie', 's')
text(ax, 66, 78, r'$\mathbb{F}_q^{*}$ = groupe', 'sujet', 'm')
box(ax, 49, 36, 34, 36, 'fixe', fill=False, dash=True)
text(ax, 66, 66, 'non nuls', 'fixe', 's')
for i in range(3):
    disc(ax, 56 + i * 10, 49, 3.2, 'sujet')
text(ax, 66, 29, r'$q - 1 = 3$ éléments', 'sujet', 's')
text(ax, 66, 18, 'groupe pour $\\times$', 'sujet', 's')
save(fig, '67-063')
