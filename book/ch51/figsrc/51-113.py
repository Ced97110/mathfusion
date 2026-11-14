import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 3, 38, 38, 24, 'autre'); text(ax, 22, 56, 'corps gauche', 'autre', 'm', weight='bold'); text(ax, 22, 45, 'inverses, ordre libre', 'autre', 's')
box(ax, 47, 38, 38, 24, 'fixe'); text(ax, 66, 56, 'anneau intègre', 'fixe', 'm', weight='bold'); text(ax, 66, 45, 'pas de diviseur de zéro', 'fixe', 's')
box(ax, 14, 3, 60, 19, 'sujet'); text(ax, 44, 15.5, 'corps', 'sujet', 'l', weight='bold'); text(ax, 44, 7.5, 'inverses + commutatif', 'sujet', 's')
arrow(ax, (22, 38), (22, 22), 'varie'); text(ax, 24.5, 30, '+ commutatif', 'varie', 's', ha='left')
arrow(ax, (66, 38), (66, 22), 'varie'); text(ax, 63.5, 30, '+ inverses', 'varie', 's', ha='right')
save(fig, '51-113')
