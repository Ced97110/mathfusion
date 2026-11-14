import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(74)
box(ax, 6, 56, 32, 11, 'sujet', label=r'$x^7 - 1$', size='l')
text(ax, 44, 61.5, '=', 'resultat', 'xl')
box(ax, 50, 56, 32, 11, 'sujet', label=r'$x^7 + 1$', size='l')
text(ax, 44, 46, r'dans $\mathbb{F}_2$ : $1 + 1 = 0$', 'varie', 'm')
text(ax, 44, 38, 'l’opposé de 1 est 1', 'varie', 's')
xs, p = brow(fig, ax, 44, 24, '10000001', roles=['varie'] + ['sujet'] * 7)
arrow(ax, (xs[0], 14), (xs[0], 19.5), 'varie')
text(ax, xs[0] - 3, 10, 'le −1 est devenu 1', 'varie', 's', ha='left')
save(fig, '68-187')
