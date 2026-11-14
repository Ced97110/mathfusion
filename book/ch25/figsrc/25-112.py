import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(86)
ox, oy, u = 14, -12, 26
P = (ox, oy+2*u); R = (ox+u, oy+2*u); Q = (ox+u, oy+2*u+0.75*u)
arrow(ax, (ox, 28), (ox, 80), 'fixe', lw=0.9)
line(ax, [(ox-3, oy+2*u-0.75*3), (ox+1.75*u, oy+2*u+0.75*1.75*u)], 'sujet', lw=1.2)
poly(ax, [P, R, Q], 'varie'); rmark(ax, R, -1, 1)
arc(ax, P, 10, 0, 36.87)
text(ax, P[0]+12, P[1]+2.2, r'$\theta$', 'varie', 'm', ha='left')
text(ax, P[0]-2, P[1]-4, 'P', 'sujet', 'm', ha='right')
text(ax, R[0]+1.5, R[1]-4, 'R', 'sujet', 'm', ha='left')
text(ax, Q[0]+1, Q[1]+4, 'Q', 'sujet', 'm', ha='left')
text(ax, (P[0]+R[0])/2, P[1]-4.5, 'avance 1 : adjacent', 'fixe', 's')
text(ax, R[0]+3, (R[1]+Q[1])/2+2, r'montée $m$', 'resultat', 's', ha='left')
text(ax, R[0]+3, (R[1]+Q[1])/2-2.5, 'opposé', 'resultat', 's', ha='left')
text(ax, 64, 26, r'tan $\theta$ = $m$ / 1', 'sujet', 'm') if False else text(ax, 52, 16, r'tan $\theta$ = $m$ / 1 = $m$', 'sujet', 'm')
text(ax, 52, 8, 'pente = tangente', 'resultat', 's')
save(fig, '25-112')
