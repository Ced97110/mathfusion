import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(70)
g = 8; k = 1.9   # mm per metre
eye = g + 1.6*k; top = eye + 16.78*k
tx = 62; ex = 10
line(ax, [(4, g), (84, g)], 'fixe')
box(ax, tx-2, g, 4, 1.6*k, 'fixe', r=0.3)
box(ax, tx-2, eye, 4, 16.78*k, 'sujet', r=0.3)
line(ax, [(ex, eye), (tx, eye)], 'fixe', dash=True)
line(ax, [(ex, eye), (tx, top)], 'varie')
disc(ax, ex, eye, 1.2, 'varie')
line(ax, [(ex, g), (ex, eye)], 'fixe')
arc(ax, (ex, eye), 9, 0, 33)
text(ax, 20, eye+3.2, '40°', 'varie', 's', ha='left')
text(ax, 4, eye+9, 'votre œil', 'varie', 's', ha='left')
text(ax, 44, eye+2.5, 'ligne de l’œil', 'fixe', 's')
line(ax, [(tx+4, eye), (tx+4, top)], 'sujet'); text(ax, tx+6, (eye+top)/2, '16,78 m', 'sujet', 's', ha='left')
line(ax, [(tx+4, g), (tx+4, eye)], 'fixe'); text(ax, tx+6, g+1.0, '+ 1,60 m', 'fixe', 's', ha='left', va='bottom')
text(ax, tx, top+4, 'total : 18,38 m', 'resultat', 'm')
save(fig, '25-099')
