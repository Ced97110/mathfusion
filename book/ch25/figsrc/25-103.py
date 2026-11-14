import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(64)
k = 78/22.4; xl = 5; xr = 83; xm = 44; wall = 10; g = 12
rise = 7*k
poly(ax, [(xl, g+wall), (xm, g+wall+rise), (xr, g+wall)], 'fixe')
line(ax, [(xl, g), (xl, g+wall)], 'fixe', lw=1.2); line(ax, [(xr, g), (xr, g+wall)], 'fixe', lw=1.2)
line(ax, [(xl, g+wall), (xr, g+wall)], 'fixe', dash=True)
line(ax, [(xm, g+wall), (xm, g+wall+rise)], 'sujet', lw=1.6)
arc(ax, (xl, g+wall), 10, 0, 32)
text(ax, 17.5, g+wall+2.8, 'inclinaison 32°', 'varie', 's', ha='left')
text(ax, xm+1.5, g+wall+rise/2, 'montée 7 m', 'sujet', 's', ha='left')
arrow(ax, (14, g+wall+9.5), (14, g+wall+5.2), 'varie') if False else None
brace(ax, xl, xr, g, 'autre', 'portée 22,4 m', size='s')
save(fig, '25-103')
