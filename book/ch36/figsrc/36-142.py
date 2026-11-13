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
s = 9; O = (10, 50)
u = (O[0] + 3*s, O[1]); v = pol(O, 4*s, 60)
arrow(ax, O, u, 'sujet', lw=1.6); arrow(ax, O, v, 'autre', lw=1.6); arrow(ax, v, u, 'resultat', lw=1.6)
arc(ax, O, 8, 0, 60, 'varie', lw=1.1)
text(ax, (O[0] + u[0]) / 2, O[1] - 4, 'u', 'sujet', 'm'); text(ax, 14, 70, 'v', 'autre', 'm')
text(ax, 42, 74, 'u − v', 'resultat', 'm', ha='left')
text(ax, *pol(O, 13, 30), r'$60°$', 'varie', 's')
text(ax, 50, 60, r'$u\cdot v=3\times4\times0{,}5=6$', 'encre', 's', ha='left')
text(ax, 50, 53, 'correction : 2 × 6 = 12', 'varie', 's', ha='left')
k = 2.4; x0 = 10
box(ax, x0, 31, 9*k, 6, 'sujet', label='9'); box(ax, x0 + 9*k, 31, 16*k, 6, 'autre', label='16')
box(ax, x0, 21, 13*k, 6, 'resultat', label='13'); box(ax, x0 + 13*k, 21, 12*k, 6, 'varie', label='− 12', dash=True)
text(ax, 44, 11, '9 + 16 − 12 = 13', 'resultat', 'm')
save(fig, '36-142')
