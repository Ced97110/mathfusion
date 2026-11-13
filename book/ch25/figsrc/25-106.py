import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def rmark(ax, C, dx, dy, s=2.2, role='fixe'):
    line(ax, [(C[0]+dx*s, C[1]), (C[0]+dx*s, C[1]+dy*s), (C[0], C[1]+dy*s)], role)
def arc(ax, c, r, t0, t1, role='varie'):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=t0, theta2=t1, color=COL[role], lw=1.0, zorder=3))
fig, ax = canvas(72)
A = (8, 14); C = (52, 14); B = (52, 14+44*0.625)
poly(ax, [A, C, B], 'sujet'); rmark(ax, C, -1, 1)
arc(ax, A, 10, 0, 32)
text(ax, 21, 17, '32°', 'sujet', 's', ha='left')
arc(ax, B, 9, 180+32, 270, 'varie')
text(ax, B[0]-3, B[1]-12.5, '58°', 'varie', 's', ha='right') if False else None
text(ax, B[0]-9, B[1]-13, '58°', 'varie', 's')
text(ax, 30, 9, r'$w$ : opposé de 58°', 'varie', 's')
text(ax, C[0]+2, (C[1]+B[1])/2, '7 m : adjacent', 'varie', 's', ha='left') if False else None
text(ax, C[0]+2, (C[1]+B[1])/2+1.5, '7 m', 'varie', 's', ha='left')
text(ax, C[0]+2, (C[1]+B[1])/2-2.5, 'adjacent à 58°', 'varie', 's', ha='left')
text(ax, 44, 66, '90 − 32 = 58', 'varie', 'm')
text(ax, 44, 59, r'$w$ = 7 × tan 58° ≈ 11,20 m', 'resultat', 's')
save(fig, '25-106')
