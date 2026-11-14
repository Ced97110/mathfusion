import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def arc(ax, c, r, a0, a1, role="varie", lw=0.9):
    ax.add_patch(Arc(c, 2*r, 2*r, theta1=a0, theta2=a1, ec=COL[role], lw=lw, zorder=3))
def pol(c, r, a):
    return (c[0] + r*math.cos(math.radians(a)), c[1] + r*math.sin(math.radians(a)))
def rightangle(ax, p, a1, a2, s=2.2, role="fixe"):
    q1 = pol(p, s, a1); q2 = pol(p, s, a2); q3 = (q1[0]+q2[0]-p[0], q1[1]+q2[1]-p[1])
    line(ax, [q1, q3, q2], role, lw=0.7)
fig, ax = canvas(74)
r = 17
def dial(cx, cy):
    disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
    line(ax, [(cx, cy - r), (cx, cy + r)], 'fixe', lw=0.8); line(ax, [(cx - r, cy), (cx + r, cy)], 'fixe', lw=0.8)
    text(ax, cx, cy + r + 3.5, 'N', 'encre', 's'); text(ax, cx, cy - r - 3.5, 'S', 'encre', 's'); text(ax, cx + r + 2.5, cy, 'E', 'fixe', 's')
def ship(cx, cy, b, role):
    a = math.radians(b); arrow(ax, (cx, cy), (cx + r*math.sin(a), cy + r*math.cos(a)), role, lw=1.6)
dial(22, 38); ship(22, 38, 40, 'sujet'); arc(ax, (22, 38), 9, 50, 90, 'varie', lw=1.2)
text(ax, 22 + 4.4, 38 + 12.2, r'$40°$', 'varie', 's')
text(ax, 22, 70, r'$N\,40°\,E=040°$', 'sujet', 'l')
dial(66, 38); ship(66, 38, 110, 'autre'); arc(ax, (66, 38), 9, -20, 90, 'varie', lw=1.2); arc(ax, (66, 38), 13, -90, -20, 'fixe', lw=1.0)
text(ax, 66 + 9.6, 38 + 8, r'$110°$', 'varie', 's')
text(ax, 66 + 15, 38 - 14, r'$70°$', 'fixe', 's')
text(ax, 66, 70, r'$S\,70°\,E=110°$', 'autre', 'l')
text(ax, 66, 8, r'$180°-70°=110°$', 'encre', 's')
text(ax, 22, 8, 'dans le sens des aiguilles', 'encre', 's')
save(fig, '36-129')
