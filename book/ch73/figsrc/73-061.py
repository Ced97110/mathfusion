import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (44, 10); u = 5
from matplotlib.patches import Arc
ax.add_patch(Arc(o, 50, 50, theta1=0, theta2=180, ec=COL['fixe'], lw=0.8, ls='--', zorder=1))
arrow(ax, o, (o[0]+3*u, o[1]+4*u), 'sujet', lw=1.3); arrow(ax, o, (o[0]-4*u, o[1]+3*u), 'resultat', lw=1.3)
arrow(ax, (o[0]+10, o[1]+17), (o[0]-9, o[1]+17), 'varie', curve=0.35)
text(ax, o[0]+17, o[1]+27, r'$x = (3, 4)$', 'sujet', 's', ha='left'); text(ax, o[0]+17, o[1]+22, r'$Q = 25$', 'sujet', 's', ha='left')
text(ax, o[0]-21, o[1]+25, r'$\eta x = (-4, 3)$', 'resultat', 's', ha='right'); text(ax, o[0]-21, o[1]+20, r'$Q = 25$', 'resultat', 's', ha='right')
text(ax, o[0], o[1]+30, r'$\eta$ : quart de tour', 'varie', 's')
text(ax, o[0], o[1]-4, 'cercle : Q = 25 partout', 'fixe', 's')
save(fig, '73-061')
