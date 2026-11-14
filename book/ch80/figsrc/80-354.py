import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 57, 'Paul : dans A, B et C', 'encre', 'm')
text(ax, 16, 49, 'somme', 'sujet', 's')
text(ax, 44, 49, 'paires', 'limite', 's')
text(ax, 72, 49, 'triple', 'resultat', 's')
for i in (-1, 0, 1):
    disc(ax, 16 + 6.5 * i, 40, 2.4, 'sujet')
    disc(ax, 44 + 6.5 * i, 40, 2.4, 'limite')
disc(ax, 72, 40, 2.4, 'resultat')
line(ax, [(28, 40), (33, 40)], 'encre', lw=1.2)
line(ax, [(57, 40), (62, 40)], 'encre', lw=1.2); line(ax, [(59.5, 37.5), (59.5, 42.5)], 'encre', lw=1.2)
text(ax, 16, 22, '3', 'sujet', 'l')
text(ax, 44, 22, r'$3-3=0$', 'limite', 'm')
text(ax, 72, 22, r'$0+1=1$', 'resultat', 'm')
arrow(ax, (22, 22), (35, 22), 'varie'); arrow(ax, (53, 22), (62, 22), 'varie')
text(ax, 44, 9, 'Paul compté 1 fois, comme il faut', 'resultat', 's')
save(fig, '80-354')
