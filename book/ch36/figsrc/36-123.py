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
s = 7.0; x0 = 5
rows = [(150, 6.77, 84), (170, 6.97, 62), (179, 7.00, 40)]
for ang, a, y in rows:
    t = math.radians(ang); b, c = 3, 4
    a_ = math.sqrt(b*b + c*c - 2*b*c*math.cos(t))
    C = (x0, y); B = (x0 + a_*s, y)
    ax_ = (b*b + a_*a_ - c*c) / (2*a_); ay = math.sqrt(max(b*b - ax_*ax_, 0))
    Ap = (x0 + ax_*s, y + ay*s)
    line(ax, [C, B], 'resultat', lw=1.2)
    line(ax, [C, Ap], 'sujet', lw=1.2); line(ax, [Ap, B], 'autre', lw=1.2)
    text(ax, Ap[0], Ap[1] + 3.2, r'$A=%d°$' % ang, 'varie', 's')
    text(ax, 62, y + 2, r'$a\approx%s$' % (f'{a:.2f}'.replace('.', '{,}')), 'resultat', 's', ha='left')
y = 18
line(ax, [(x0, y), (x0 + 3*s, y)], 'sujet', lw=1.6); line(ax, [(x0 + 3*s, y), (x0 + 7*s, y)], 'autre', lw=1.6)
ax.plot([x0 + 3*s], [y], 'o', color=COL['varie'], ms=3, zorder=4)
brace(ax, x0, x0 + 7*s, y + 1.5, 'resultat', down=False, label=r'$a=3+4=7$')
text(ax, x0 + 1.5*s, y - 4, '3', 'sujet', 's'); text(ax, x0 + 5*s, y - 4, '4', 'autre', 's')
text(ax, 62, y, r'$A=180°$', 'varie', 's', ha='left')
text(ax, 44, 96, 'côtés 3 (bleu) et 4 (violet)', 'encre', 's')
save(fig, '36-123')
