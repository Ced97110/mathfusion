import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
ox, oy, u = 8, 8, 8.0
X = (ox + 3 * u, oy + 4 * u)
line(ax, [(ox, oy), (ox + 3 * u, oy)], 'fixe', lw=1.2); line(ax, [(ox + 3 * u, oy), X], 'fixe', lw=1.2)
line(ax, [(ox + 3 * u - 2.5, oy), (ox + 3 * u - 2.5, oy + 2.5), (ox + 3 * u, oy + 2.5)], 'fixe', lw=0.7)
arrow(ax, (ox, oy), X, 'sujet', lw=1.6)
text(ax, ox + 1.5 * u, oy - 3.2, '3', 'fixe', 's'); text(ax, ox + 3 * u + 3, oy + 2 * u, '4', 'fixe', 's')
text(ax, ox + 1.5 * u - 4, oy + 2 * u + 3, r'$\|x\|=5$', 'sujet', 'm', weight='bold')
text(ax, 62, 42, r'$\langle x,x\rangle$', 'sujet', 'm'); text(ax, 62, 35, r'$=9+16=25$', 'sujet', 's')
arrow(ax, (62, 31), (62, 25), 'varie'); text(ax, 74, 28, 'racine', 'varie', 's')
text(ax, 62, 19.5, r'$\sqrt{25}=5$', 'resultat', 'm', weight='bold')
save(fig, '73-077')
