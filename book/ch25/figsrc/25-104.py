import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(62)
k = 78/22.4; xl = 5; xr = 83; xm = 44; wall = 10; g = 14
rise = 7*k
poly(ax, [(xl, g+wall), (xm, g+wall+rise), (xm, g+wall)], 'sujet')
poly(ax, [(xr, g+wall), (xm, g+wall+rise), (xm, g+wall)], 'autre')
line(ax, [(xl, g), (xl, g+wall)], 'fixe', lw=1.2); line(ax, [(xr, g), (xr, g+wall)], 'fixe', lw=1.2)
line(ax, [(xm, g+wall), (xm, g+wall+rise)], 'fixe', dash=True)
text(ax, 24, g+wall+4, 'triangle 1', 'sujet', 's')
text(ax, 64, g+wall+4, 'triangle 2', 'autre', 's')
brace(ax, xl, xm-0.6, g, 'sujet', r'$w$ = 11,2 m', size='s')
brace(ax, xm+0.6, xr, g, 'autre', r'$w$ = 11,2 m', size='s')
text(ax, xm, 55, 'portée = 2 $w$ = 22,4 m', 'resultat', 'm')
save(fig, '25-104')
