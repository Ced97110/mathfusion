import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 22, 46, r'$D_1=(x-1)^2$', 'sujet', 'm'); text(ax, 66, 46, r'$D_2=(x-1)(x+3)$', 'autre', 'm')
box(ax, 4, 26, 17, 10, 'sujet', label=r'$x-1$'); box(ax, 23, 26, 17, 10, 'sujet', label=r'$x-1$')
box(ax, 47, 26, 17, 10, 'sujet', label=r'$x-1$'); box(ax, 66, 26, 17, 10, 'autre', label=r'$x+3$')
brace(ax, 4, 40, 25, 'sujet', '2 fois')
brace(ax, 47, 64, 25, 'sujet', '1 fois'); brace(ax, 66, 83, 25, 'autre', '1 fois')
text(ax, 44, 8, r'exposant de $x-1$ : 2 et 1', 'varie', 's')
save(fig, '21-070')
