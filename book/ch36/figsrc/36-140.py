import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(96)
s = 0.6; A = (10, 14); B = (70, 14); T = pol(A, 113.05*s, 70)
line(ax, [A, B], 'sujet', lw=1.8); line(ax, [A, T], 'resultat', lw=1.4); line(ax, [B, T], 'resultat', lw=1.4)
arc(ax, A, 10, 0, 70, 'varie', lw=1.1); arc(ax, B, 10, 120, 180, 'varie', lw=1.1); arc(ax, T, 9, 250, 300, 'fixe', lw=1.1)
for p, t, dx, dy in [(A, 'A', -3, -2), (B, 'B', 3, -2), (T, 'arbre', 0, 4)]:
    ax.plot(*p, 'o', color=COL['encre'], ms=2.5, zorder=4); text(ax, p[0] + dx, p[1] + dy, t, 'encre', 's')
text(ax, 40, 9, 'base 100 m (mesurée)', 'sujet', 's')
text(ax, *pol(A, 17, 30), r'$70°$', 'varie', 's'); text(ax, *pol(B, 17, 150), r'$60°$', 'varie', 's')
text(ax, *pol(T, 14, 275), r'$50°$', 'fixe', 's')
text(ax, 15, 52, r'$113{,}1$ m', 'resultat', 's'); text(ax, 59, 52, r'$122{,}7$ m', 'resultat', 's', ha='left')
save(fig, '36-140')
