import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(80)
s = 56/154
T = (66, 12); S = (T[0]-154*s, 12); H = (T[0], 12+168*s)
line(ax, [(4, 12), (84, 12)], 'fixe')
line(ax, [T, H], 'sujet', lw=2.2); line(ax, [S, T], 'autre', lw=2.2)
line(ax, [S, H], 'varie', lw=1.6)
rmark(ax, T, -1, 1)
arc(ax, S, 11, 0, 47.49)
text(ax, S[0]+14, 15.5, r'$\theta$', 'varie', 'm', ha='left')
text(ax, T[0]+2, (T[1]+H[1])/2+3, '168 cm', 'sujet', 's', ha='left')
text(ax, T[0]+2, (T[1]+H[1])/2-1, 'personne', 'sujet', 's', ha='left')
text(ax, 38, 7.5, 'ombre : 154 cm', 'autre', 's')
text(ax, S[0]+3, S[1]+30, 'rayon', 'varie', 's', ha='left')
text(ax, 44, 74, r'$\theta$ = arctan(168 / 154)', 'sujet', 'm')
text(ax, 44, 67.5, r'≈ 47,49°', 'resultat', 'm')
save(fig, '25-107')
