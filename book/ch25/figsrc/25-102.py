import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(66)
k = 39/11.2; xl = 5; xr = 83; xm = 44; wall = 12; g = 8
rise = 7*k
poly(ax, [(xl, g+wall), (xm, g+wall+rise), (xr, g+wall)], 'sujet')
line(ax, [(xl, g), (xl, g+wall)], 'fixe', lw=1.2); line(ax, [(xr, g), (xr, g+wall)], 'fixe', lw=1.2)
line(ax, [(xl, g+wall), (xr, g+wall)], 'fixe', dash=True)
line(ax, [(xm, g+wall), (xm, g+wall+rise)], 'resultat', lw=1.2)
arc(ax, (xl, g+wall), 10, 0, 32)
text(ax, 17.5, g+wall+2.8, '32°', 'varie', 's', ha='left')
text(ax, xm+1.5, g+wall+rise/2, '7 m', 'resultat', 's', ha='left')
text(ax, xm, g+wall+rise+4, 'faîte', 'sujet', 's')
brace(ax, xl, xm, g+wall-1.5, 'varie', r'$w$ = ?', size='m')
text(ax, 64, 4, '', 'encre')
text(ax, 63, g+wall-6, r'tan 32° = 7 / $w$', 'sujet', 's')
save(fig, '25-102')
