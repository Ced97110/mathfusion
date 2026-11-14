import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 15, 64, 'éléments d’ordre 4', 'sujet', 's')
text(ax, 43, 64, 'on double', 'varie', 's')
box(ax, 60, 31, 24, 10, 'varie', label='(2, 0)')
for k, v in enumerate(('(1, 0)', '(3, 0)', '(1, 1)', '(3, 1)')):
    y = 52 - 14 * k
    box(ax, 4, y, 22, 9, 'sujet', label=v)
    arrow(ax, (26.5, y + 4.5), (59.5, 36), 'varie')
text(ax, 72, 22, 'K contient (2, 0)', 'limite', 's')
save(fig, '60-257')
