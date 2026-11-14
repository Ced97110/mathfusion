import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
poly(ax, [(14, 12), (62, 12), (62, 64), (14, 64)], 'sujet')
arrow(ax, (14, 12), (68, 12), 'fixe', lw=1.0); arrow(ax, (14, 12), (14, 68), 'fixe', lw=1.0)
px, py = 38, 40
line(ax, [(px, 12), (px, py)], 'varie', dash=True); line(ax, [(14, py), (px, py)], 'varie', dash=True)
disc(ax, px, py, 2.6, 'sujet')
text(ax, px + 3, py + 4, r'$(x,\,y)$', 'sujet', 'm', ha='left')
text(ax, px, 7.5, r'$x$', 'varie', 'm'); text(ax, 9, py, r'$y$', 'varie', 'm')
text(ax, 78, 12, r'1er $\mathbb{R}$', 'fixe', 's'); text(ax, 14, 73, r'2e $\mathbb{R}$', 'fixe', 's')
text(ax, 76, 52, r'$\mathbb{R}\times\mathbb{R}$', 'resultat', 'l', weight='bold')
text(ax, 76, 44, 'le plan', 'resultat', 'm')
save(fig, '42-165')
