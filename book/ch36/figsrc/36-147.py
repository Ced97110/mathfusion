import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(80)
s = 6; y0 = 32
poly(ax, [(8, y0), (8 + 4*s, y0), (8 + 4*s, y0 + 3*s), (8, y0 + 3*s)], 'sujet')
line(ax, [(8, y0), (8 + 4*s, y0 + 3*s)], 'varie', lw=1.4, dash=True)
A = (50, y0); B = (50 + 4*s, y0); C = pol(B, 3*s, 62.72); D = (C[0] - 4*s, C[1])
poly(ax, [A, B, C, D], 'autre'); line(ax, [A, C], 'varie', lw=1.4, dash=True)
arc(ax, B, 5, 62.72, 180, 'varie', lw=1.1)
text(ax, 8 + 2*s, y0 - 4, '4', 'sujet', 's'); text(ax, 4.5, y0 + 1.5*s, '3', 'sujet', 's')
text(ax, 50 + 2*s, y0 - 4, '4', 'autre', 's'); text(ax, C[0] + 3, (B[1] + C[1]) / 2, '3', 'autre', 's')
text(ax, 22, y0 + 2.2*s, '5', 'varie', 's'); text(ax, 66, y0 + 2*s, '6', 'varie', 's')
text(ax, 80, y0 - 4, r'$117{,}28°$', 'varie', 's')
text(ax, 20, 18, 'diagonale 5 : rectangle', 'sujet', 's'); text(ax, 66, 18, 'diagonale 6 : penché', 'autre', 's')
text(ax, 44, 6, 'une diagonale fixe la figure', 'encre', 's')
save(fig, '36-147')
