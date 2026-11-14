import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
f = numberline(ax, 8, 70, 56, 0, 2, step=1, arrow_right=True)
x = 8 + (2 ** 0.5) / 2 * 62
disc(ax, x, 56, 2, 'sujet')
text(ax, x, 65, r'$\sqrt{2}$', 'sujet', 'l')
text(ax, x, 70, 'pas une fraction', 'limite', 's')
arrow(ax, (x, 62), (x, 57.5), 'limite', lw=0.6)
text(ax, 44, 43, 'pourtant, il annule :', 'fixe', 's')
box(ax, 14, 27, 60, 11, 'sujet', label=r'$x^2-2$', size='l')
arrow(ax, (44, 27), (44, 20), 'varie')
box(ax, 8, 6, 72, 13, 'resultat', label=r'$(\sqrt{2})^2-2=0$', size='l')
save(fig, '61-069')
