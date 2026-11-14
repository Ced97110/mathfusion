import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(100)
bx, bw, bh = 10, 68, 12
ys = [84, 58, 32, 6]
box(ax, bx, ys[0], bw, bh, 'sujet', label=r'tan 32° = 7 / $w$')
box(ax, bx, ys[1], bw, bh, 'sujet', label=r'tan 32° × $w$ = 7')
box(ax, bx, ys[2], bw, bh, 'resultat', label=r'$w$ = 7 / tan 32°')
box(ax, bx, ys[3], bw, bh, 'resultat', label=r'$w$ ≈ 7 / 0,6249 ≈ 11,20 m')
for i, lab in enumerate([r'× $w$ des deux côtés', r'÷ tan 32° des deux côtés']):
    arrow(ax, (44, ys[i]), (44, ys[i+1]+bh), 'varie')
    text(ax, 48, ys[i]-7, lab, 'varie', 's', ha='left')
arrow(ax, (44, ys[2]), (44, ys[3]+bh), 'fixe')
text(ax, 48, ys[2]-7, 'calcul', 'fixe', 's', ha='left')
text(ax, 82, ys[2]+bh/2, r'$w$ seul', 'resultat', 's', ha='left') if False else None
save(fig, '25-105')
