import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 6, 52, 76, 10, 'fixe', label='la classe du couple (2, 3)')
arrow(ax, (44, 51), (44, 44), 'varie')
text(ax, 62, 47.5, 's’écrit', 'varie', 's')
text(ax, 44, 38, '[2, 3]', 'sujet', 'xl', weight='bold')
disc(ax, 20, 22, 1.8, 'varie')
text(ax, 20, 15, '(2, 3)', 'varie', 'm')
text(ax, 20, 9, 'un point', 'varie', 's')
box(ax, 46, 14, 38, 16, 'sujet')
for x in (55, 65, 75):
    disc(ax, x, 22, 1.8, 'sujet')
text(ax, 65, 9, '[2, 3] : un groupe', 'sujet', 's')
save(fig, '54-065')
