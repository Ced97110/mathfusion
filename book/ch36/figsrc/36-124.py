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
s = 11.0; x0 = 6
for ang, lab, y in [(10, r'$a\approx1{,}17$', 68), (1, r'$a\approx1{,}002$', 50)]:
    t = math.radians(ang)
    A = (x0, y); C = (x0 + 4*s, y); B = (x0 + 3*s*math.cos(t), y + 3*s*math.sin(t))
    line(ax, [A, C], 'autre', lw=1.2); line(ax, [A, B], 'sujet', lw=1.2); line(ax, [B, C], 'resultat', lw=1.2)
    text(ax, 56, y + 5, r'$A=%d°$' % ang, 'varie', 's', ha='left')
    text(ax, 56, y - 1.5, lab, 'resultat', 's', ha='left')
y = 28
line(ax, [(x0, y), (x0 + 4*s, y)], 'autre', lw=1.6)
line(ax, [(x0, y + 1.2), (x0 + 3*s, y + 1.2)], 'sujet', lw=1.6)
brace(ax, x0 + 3*s, x0 + 4*s, y - 1, 'resultat', down=True, label=r'$a=4-3=1$')
text(ax, x0 + 1.5*s, y + 4.5, '3', 'sujet', 's'); text(ax, x0 + 3.5*s, y + 4.5, '4', 'autre', 's')
text(ax, 56, y + 2, r'$A=0°$', 'varie', 's', ha='left')
save(fig, '36-124')
