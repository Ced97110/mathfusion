import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(76)
cx, cy, R = 32, 37, 24
arrow(ax, (cx - R - 4, cy), (cx + R + 5, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - R - 3), (cx, cy + R + 4), 'fixe', lw=0.6)
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
pt = lambda deg: (cx + R * math.cos(math.radians(deg)), cy + R * math.sin(math.radians(deg)))
for r0, a0, a1, role, lw in ((11, 0, 30, 'varie', 1.2), (16, 30, 90, 'varie', 1.2)):
    ax.add_patch(Arc((cx, cy), 2 * r0, 2 * r0, theta1=a0, theta2=a1, color=COL[role], lw=lw, zorder=3))
e, p30, p90 = pt(0), pt(30), pt(90)
disc(ax, *e, 1.3, 'fixe'); disc(ax, *p30, 1.3, 'sujet'); disc(ax, *p90, 1.3, 'resultat')
text(ax, e[0] - 1, cy - 4, r'$(1\,;\,0)$', 'fixe', 's')
text(ax, p30[0] + 2.5, p30[1] + 1.5, r'$(0{,}866\,;\,0{,}5)$', 'sujet', 's', ha='left')
text(ax, p90[0] + 3, p90[1] + 1, r'$(0\,;\,1)$', 'resultat', 's', ha='left')
text(ax, cx + 16, cy + 4, '30°', 'varie', 's')
text(ax, cx + 10, cy + 17.5, '+ 60°', 'varie', 's')
text(ax, 72, 68, r'$x=\cos t$' + '\n' + r'$y=\sin t$', 'sujet', 'm')
text(ax, 44, 5, 'les angles s’additionnent :\n30° + 60° = 90°', 'resultat', 's')
save(fig, '40-128')
