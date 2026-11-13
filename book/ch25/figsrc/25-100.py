import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(76)
g = 10; e = 18; L = 36
line(ax, [(4, g), (84, g)], 'fixe')
line(ax, [(4, e), (84, e)], 'fixe', dash=True)
P = [(8, g), (34, g), (34, g + L)]; Q = [(50, e), (72, e), (72, e + L)]
poly(ax, P, 'sujet'); poly(ax, Q, 'autre')
line(ax, [(34, g + L), (84, g + L)], 'sujet', dash=True)
line(ax, [(72, e + L), (84, e + L)], 'autre', dash=True)
text(ax, 41, g + L / 2, '16,78 m', 'sujet', 's')
text(ax, 79, e + L / 2, '16,78 m', 'autre', 's')
text(ax, 20, g - 4, 'base : sol', 'sujet', 's')
text(ax, 61, e - 4, 'base : œil', 'autre', 's')
text(ax, 44, g + L + 2.8, 'sommet 1', 'sujet', 's')
text(ax, 78, e + L + 2.8, 'sommet 2', 'autre', 's')
text(ax, 44, 70, 'même nombre, sommets différents', 'limite', 's')
text(ax, 23, 62, 'triangle 1', 'sujet', 's'); text(ax, 63, 62, 'triangle 2', 'autre', 's')
save(fig, '25-100')
