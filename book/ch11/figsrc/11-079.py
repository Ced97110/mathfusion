import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
x0, y0, w, h = 14, 46, 46, 22
ax.add_patch(Rectangle((x0, y0), w, h, fc=FILL['fixe'], ec=COL['fixe'], lw=1.0, zorder=2))
line(ax, [(x0, y0), (x0, y0 + h)], 'sujet', lw=2.6)
text(ax, x0 - 3, y0 + h / 2, r'$l$', 'sujet', 'l'); text(ax, x0 + w / 2, y0 + h / 2, r'$L$', 'fixe', 'l')
text(ax, x0 + w + 3, y0 + h / 2, 'largeur = côté bleu', 'sujet', 's', ha='left')
box(ax, 4, 26, 36, 9, 'fixe', label='2 × longueur', size='m'); text(ax, 44, 30.5, '+', 'encre', 'l')
box(ax, 48, 26, 36, 9, 'sujet', label='2 × largeur', size='m')
arrow(ax, (22, 25), (22, 17), 'varie'); arrow(ax, (66, 25), (66, 17), 'varie')
box(ax, 10, 6, 24, 10, 'fixe', label=r'$2L$', size='l'); text(ax, 44, 11, '+', 'encre', 'l')
box(ax, 54, 6, 24, 10, 'sujet', label=r'$2l$', size='l')
save(fig, '11-079')
