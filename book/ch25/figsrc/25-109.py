import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(72)
A = (6, 14); C = (6+24, 14); B = (C[0], 14+48)
poly(ax, [A, C, B], 'sujet'); rmark(ax, C, -1, 1)
arc(ax, A, 8, 0, 63.43)
text(ax, A[0]+10, A[1]+6, 'angle ?', 'varie', 's', ha='left') if False else text(ax, A[0]+9, A[1]+4, '?', 'varie', 'm', ha='left')
text(ax, 18, 9.5, 'ombre : 1 m', 'fixe', 's')
text(ax, C[0]+2, 38, 'bâton : 2 m', 'sujet', 's', ha='left')
box(ax, 46, 46, 38, 14, 'fixe')
text(ax, 65, 56, 'rapport', 'fixe', 's'); text(ax, 65, 50, '2 ÷ 1 = 2', 'fixe', 'm')
text(ax, 65, 62.5, 'Thalès s’arrête là', 'fixe', 's')
arrow(ax, (65, 46), (65, 34), 'varie'); text(ax, 68, 40, 'arctan', 'varie', 's', ha='left')
box(ax, 46, 20, 38, 14, 'resultat')
text(ax, 65, 30, 'angle du soleil', 'resultat', 's'); text(ax, 65, 24, '≈ 63,43°', 'resultat', 'm')
save(fig, '25-109')
