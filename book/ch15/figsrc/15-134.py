import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, left):
    box(ax, 3, y, 44, 13, 'varie', label=left, size='m')
    text(ax, 50, y + 6.5, '=', 'encre', 'l')
    box(ax, 53, y, 32, 13, 'fixe', label=r'$2x+7$', size='m')
row(62, r'$3(x+2)-5$')
arrow(ax, (25, 61), (25, 49), 'varie')
text(ax, 54, 55, 'simplifier le côté', 'varie', 's')
row(34, r'$3x+1$')
arrow(ax, (44, 33), (44, 24), 'resultat')
box(ax, 14, 11, 60, 12, 'resultat', label=r'$x=6$ : 19 = 19', size='m')
text(ax, 44, 5, r'$x$ seul, exposant 1 : degré 1', 'sujet', 's')
save(fig, '15-134')
