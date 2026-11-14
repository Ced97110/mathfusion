import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
steps = [(38, r'$x^2+2x+5=0$', 'fixe'), (21, r'$x^2+2x=-5$', 'fixe'), (4, r'$(x+1)^2=-4$', 'sujet')]
for y, s, r in steps:
    box(ax, 4, y, 46, 10, r, True, s, 'l')
for y0, lab in [(38, '5 passe à droite'), (21, '+ 1 des deux côtés')]:
    arrow(ax, (27, y0), (27, y0 - 7), 'varie')
    text(ax, 31, y0 - 3.5, lab, 'varie', 's', ha='left')
arrow(ax, (50, 9), (58, 9), 'limite')
box(ax, 58, 4, 28, 10, 'limite', True, 'impossible', 'm')
text(ax, 72, 19, 'un carré ne vaut pas −4', 'limite', 's')
save(fig, '23-096')
