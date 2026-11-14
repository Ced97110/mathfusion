import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, a, b, c, ra, rb, rc):
    box(ax, 6, y, 30, 9, ra, label=a, size='s'); box(ax, 40, y, 22, 9, rb, label=b, size='s'); box(ax, 66, y, 16, 9, rc, label=c, size='s')
row(56, r'$2x-y$', r'$+\,3z$', r'$=0$', 'fixe', 'varie', 'fixe')
text(ax, 3, 47, '−', 'encre', 'l')
row(40, r'$2x-y$', r'$+\,0z$', r'$=0$', 'fixe', 'fixe', 'fixe')
line(ax, [(6, 36), (82, 36)], 'encre', lw=0.9)
row(24, r'$0$', r'$3z$', r'$=0$', 'fixe', 'varie', 'fixe')
box(ax, 22, 6, 44, 11, 'resultat', label=r'donc $z=0$')
arrow(ax, (44, 23), (44, 17.5), 'varie')
save(fig, '80-288')
