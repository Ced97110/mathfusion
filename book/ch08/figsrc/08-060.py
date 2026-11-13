import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def frac(x, n, d, r):
    text(ax, x, 62, n, r, 'xl', weight='bold'); line(ax, [(x - 9, 57), (x + 9, 57)], r, lw=1.2); text(ax, x, 51, d, r, 'xl', weight='bold')
frac(16, '4,32', '1,8', 'sujet'); frac(72, '43,2', '18', 'autre')
text(ax, 44, 57, '=', 'encre', 'xl')
arrow(ax, (28, 62), (60, 62), 'varie'); text(ax, 44, 68, r'$\times10$ en haut', 'varie', 's')
arrow(ax, (28, 51), (60, 51), 'varie'); text(ax, 44, 45, r'$\times10$ en bas', 'varie', 's')
arrow(ax, (16, 44), (34, 28), 'resultat'); arrow(ax, (72, 44), (54, 28), 'resultat')
box(ax, 20, 16, 48, 11, 'resultat', label='les deux valent 2,4', size='m')
save(fig, '08-060')
