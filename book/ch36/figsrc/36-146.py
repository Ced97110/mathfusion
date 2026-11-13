import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(100)
s = 6
poly(ax, [(8, 60), (8 + 4*s, 60), (8 + 4*s, 60 + 3*s), (8, 60 + 3*s)], 'sujet')
P0 = (50, 60); B = (50 + 4*s, 60); C = pol(B, 3*s, 70); D = (C[0] - 4*s, C[1])
poly(ax, [P0, B, C, D], 'autre')
arrow(ax, (36, 70), (47, 70), 'varie', both=True)
text(ax, 8 + 2*s, 56, '4', 'sujet', 's'); text(ax, 4.5, 60 + 1.5*s, '3', 'sujet', 's')
text(ax, 50 + 2*s, 56, '4', 'autre', 's'); text(ax, C[0] + 2.5, (B[1] + C[1]) / 2, '3', 'autre', 's')
text(ax, 20, 84, 'rectangle', 'sujet', 'm'); text(ax, 64, 84, 'penché', 'autre', 'm')
text(ax, 44, 94, '4 côtés : pas fixé', 'varie', 'm')
A3 = (8, 12); C3 = (8 + 4*s, 12); B3 = (8 + 4*s, 12 + 3*s)
poly(ax, [A3, C3, B3], 'resultat'); line(ax, [A3, C3, B3, A3], 'resultat', lw=1.3)
text(ax, 8 + 2*s, 8, '4', 'resultat', 's'); text(ax, C3[0] + 3, 12 + 1.5*s, '3', 'resultat', 's'); text(ax, 15, 29, '5', 'resultat', 's')
text(ax, 44, 42, '3 côtés : fixé', 'resultat', 'm')
text(ax, 42, 18, 'ne peut pas se pencher', 'fixe', 's', ha='left')
save(fig, '36-146')
