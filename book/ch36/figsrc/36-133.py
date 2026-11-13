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
r = 15
def dial(cx, cy):
    disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
    line(ax, [(cx, cy - r), (cx, cy + r)], 'fixe', lw=0.8); line(ax, [(cx - r, cy), (cx + r, cy)], 'fixe', lw=0.8)
    text(ax, cx, cy + r + 3.2, 'N', 'encre', 's'); text(ax, cx, cy - r - 3.2, 'S', 'encre', 's')
    text(ax, cx + r + 3, cy, 'E', 'fixe', 's'); text(ax, cx - r - 3, cy, 'O', 'fixe', 's')
def arr(cx, cy, b, role):
    a = math.radians(b); arrow(ax, (cx, cy), (cx + r*math.sin(a), cy + r*math.cos(a)), role, lw=1.6)
cA = (22, 46); cB = (66, 46)
dial(*cA); arr(*cA, 40, 'sujet'); arr(*cA, 220, 'varie')
arc(ax, cA, 8, 50, 90, 'sujet', lw=1.2); arc(ax, cA, 8, -130, -90, 'varie', lw=1.2)
text(ax, *pol(cA, 12.5, 70), r'$40°$', 'sujet', 's')
dial(*cB); arr(*cB, 110, 'sujet'); arr(*cB, 290, 'varie')
arc(ax, cB, 8, -90, -20, 'sujet', lw=1.2); arc(ax, cB, 8, 90, 160, 'varie', lw=1.2)
text(ax, *pol(cB, 12.5, -55), r'$70°$', 'sujet', 's')
text(ax, 22, 16, 'N 40° E', 'sujet', 'm'); text(ax, 22, 9, 'S 40° O', 'varie', 'm')
text(ax, 66, 16, 'S 70° E', 'sujet', 'm'); text(ax, 66, 9, 'N 70° O', 'varie', 'm')
save(fig, '36-133')
