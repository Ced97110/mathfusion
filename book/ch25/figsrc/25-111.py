import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(80)
ox, oy, u = 20, 10, 16   # origin, mm per unit
arrow(ax, (ox, oy-2), (ox, oy+4*u), 'fixe', lw=0.9)
arrow(ax, (ox-4, oy), (ox+3.5*u, oy), 'fixe', lw=0.9)
for v in (1, 2, 3):
    ax.plot([ox-1, ox+1], [oy+v*u, oy+v*u], color=COL['fixe'], lw=0.8)
text(ax, ox-3.5, oy+2*u, '2', 'fixe', 's', ha='right')
text(ax, ox-3.5, oy+4*u, r'$y$', 'fixe', 's', ha='right')
text(ax, ox+3.5*u, oy-3.5, r'$x$', 'fixe', 's')
line(ax, [(ox-2, oy+2*u-1.5), (ox+3*u, oy+2*u+0.75*3*u)], 'sujet', lw=1.4)
disc(ax, ox, oy+2*u, 1.4, 'varie')
text(ax, ox+5, oy+2*u-4.5, r'$p$ = 2', 'varie', 'm', ha='left')
text(ax, 66, 62, r'$y = mx + p$', 'sujet', 'm') if False else text(ax, 62, 64, r'$y = mx + p$', 'sujet', 'm')
box(ax, 54, 20, 30, 22, 'varie')
text(ax, 69, 32, 'chapitre 19 : $b$', 'fixe', 's') if False else None
text(ax, 69, 31, 'hauteur sur', 'varie', 's'); text(ax, 69, 25, 'l’axe vertical', 'varie', 's')
text(ax, 69, 40, 'nom : $p$ (avant : $b$)', 'varie', 's') if False else text(ax, 69, 37, 'nom : p', 'varie', 'm')
save(fig, '25-111')
