import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
o = (44, 8); u = 8
ax.plot([o[0], o[0]], [o[1], o[1]+30], color=COL['fixe'], lw=1.2, ls='--', zorder=2)
arrow(ax, o, (o[0]+u, o[1]), 'sujet', lw=1.4); arrow(ax, o, (o[0]-u, o[1]), 'resultat', lw=1.4)
arrow(ax, o, (o[0]+3*u, o[1]+2*u), 'sujet', lw=1.0)
arrow(ax, o, (o[0]-3*u, o[1]+2*u), 'resultat', lw=1.0)
arrow(ax, (o[0]+20, o[1]+24), (o[0]-20, o[1]+24), 'varie', curve=0.3)
text(ax, o[0]+9, o[1]-4, r'$u = (1, 0)$', 'sujet', 's', ha='left'); text(ax, o[0]-9, o[1]-4, r'$-u$', 'resultat', 's', ha='right')
text(ax, o[0]+26, o[1]+19, r'$x = (3, 2)$', 'sujet', 's', ha='left'); text(ax, o[0]-26, o[1]+19, r'$S_u x = (-3, 2)$', 'resultat', 's', ha='right')
text(ax, o[0]+2, o[1]+33, 'axe fixe', 'fixe', 's', ha='left'); text(ax, o[0]+2, o[1]+39, 'dét = −1', 'varie', 's', ha='left')
save(fig, '73-064')
