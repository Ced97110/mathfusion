import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(92)
c = (40, 44); r = 26
disc(ax, c[0], c[1], r, 'fixe', fill=False, lw=0.6)
line(ax, [(c[0], c[1] - r), (c[0], c[1] + r)], 'fixe', lw=0.8); line(ax, [(c[0] - r, c[1]), (c[0] + r, c[1])], 'fixe', lw=0.8)
b = 40; tip = (c[0] + r*math.sin(math.radians(b)), c[1] + r*math.cos(math.radians(b)))
arrow(ax, c, tip, 'sujet', lw=1.6)
arc(ax, c, 13, 90 - b, 90, 'varie', lw=1.2)
text(ax, c[0], c[1] + r + 5, 'nord (départ)', 'encre', 'm')
text(ax, c[0], c[1] - r - 4, 'S', 'encre', 'm'); text(ax, c[0] + r + 6, c[1], 'E (est)', 'resultat', 'm'); text(ax, c[0] - r - 4, c[1], 'O', 'encre', 'm')
text(ax, c[0] + 4.5, c[1] + 19, r'$40°$', 'varie', 's')
text(ax, tip[0] + 3, tip[1] + 3, 'cap', 'sujet', 'm', ha='left')
text(ax, c[0] - 8, c[1] - 4, 'port', 'encre', 's')
save(fig, '36-127')
