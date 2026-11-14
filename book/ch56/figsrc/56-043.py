import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
# Gauche : 12 se casse en deux non-unités
text(ax, 22, 71, 'a = 12', 'encre', 'l')
box(ax, 12, 52, 20, 11, 'fixe', label='12')
line(ax, [(18, 52), (10, 38)], 'varie'); line(ax, [(26, 52), (34, 38)], 'varie')
box(ax, 2, 27, 16, 11, 'varie', label='2')
box(ax, 26, 27, 16, 11, 'varie', label='6')
text(ax, 22, 21, '2 et 6 : pas des unités', 'varie', 's')
text(ax, 22, 12, 'se casse', 'varie', 'm')
# Droite : 7 ne se casse qu'avec une unité
text(ax, 66, 71, 'a = 7', 'encre', 'l')
box(ax, 56, 52, 20, 11, 'sujet', label='7')
line(ax, [(62, 52), (54, 38)], 'sujet'); line(ax, [(70, 52), (78, 38)], 'sujet')
box(ax, 46, 27, 16, 11, 'sujet', label='7')
box(ax, 70, 27, 16, 11, 'fixe', label='1')
text(ax, 78, 21, 'unité', 'fixe', 's')
text(ax, 66, 12, 'ne se casse pas', 'sujet', 'm')
save(fig, '56-043')
