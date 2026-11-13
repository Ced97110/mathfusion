import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def grid(x, y, role):
    for i in range(6):
        for j in range(4):
            box(ax, x+i*2.4, y+j*2.4, 2.4, 2.4, role, r=0.2, lw=0.4)
grid(6, 34, 'sujet'); grid(6, 8, 'autre')
text(ax, 13, 49, r'$\det = 1$ : 24', 'sujet', 's'); text(ax, 13, 23, r'$\det = 2$ : 24', 'autre', 's')
text(ax, 22, 55, r'48 matrices de $GL_2$', 'encre', 'm')
box(ax, 62, 33, 12, 10, 'resultat', label='1', size='l'); box(ax, 62, 7, 12, 10, 'resultat', label='2', size='l')
arrow(ax, (22, 39), (60, 38), 'varie'); arrow(ax, (22, 13), (60, 12), 'varie')
text(ax, 68, 50, r'$F^*$', 'resultat', 'l'); text(ax, 68, 26, '2 valeurs', 'resultat', 's')
text(ax, 41, 30, '2 classes', 'varie', 's')
save(fig, '73-038')
