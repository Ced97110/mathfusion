import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

cx, cy, r = 22, 78, 16
fig, ax = canvas(100)
arrow(ax, (3, cy), (cx + r + 6, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 4), (cx, cy + r + 6), 'fixe', lw=0.6)
disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.6)
p1 = (cx + r * math.cos(math.radians(30)), cy + r * math.sin(math.radians(30)))
p3 = (cx, cy + r)
line(ax, [(cx, cy), p1], 'sujet', lw=1.2)
line(ax, [(cx, cy), p3], 'resultat', lw=1.2)
disc(ax, p1[0], p1[1], 1.2, 'sujet'); disc(ax, p3[0], p3[1], 1.2, 'resultat')
ax.add_patch(Arc((cx, cy), 13, 13, theta1=0, theta2=30, ec=COL['sujet'], lw=1.1, zorder=3))
ax.add_patch(Arc((cx, cy), 22, 22, theta1=0, theta2=90, ec=COL['resultat'], lw=1.1, zorder=3))
text(ax, cx + 9, cy + 1.8, r'$\theta$', 'sujet', 's')
text(ax, cx + 10.5, cy + 10.5, r'$3\theta$', 'resultat', 's')
text(ax, p1[0] + 2, p1[1] - 2.5, r'$\mathrm{cis}\,\theta$', 'sujet', 's', ha='left')
text(ax, p3[0] + 2.5, p3[1] + 3, r'$\mathrm{cis}\,3\theta=i$', 'resultat', 's', ha='left')
# le cube, à droite du cercle
text(ax, 84, 90, r'$n=3,\ \theta=30°$', 'encre', 'm', ha='right')
text(ax, 84, 80, r'$(\cos\theta+i\sin\theta)^3$', 'sujet', 'm', ha='right')
text(ax, 84, 71, r'$=\cos 3\theta+i\sin 3\theta$', 'resultat', 'm', ha='right')
# on développe le cube, puis on compare les parties
text(ax, 44, 56, 'on développe le cube, on compare :', 'fixe', 's')
box(ax, 2, 33, 84, 18, 'varie')
text(ax, 5, 47, 'partie réelle', 'varie', 's', ha='left')
text(ax, 44, 40, r'$\cos 3\theta=\cos^3\theta-3\cos\theta\,\sin^2\theta$', 'varie', 'l')
box(ax, 2, 12, 84, 18, 'autre')
text(ax, 5, 26, 'partie imaginaire', 'autre', 's', ha='left')
text(ax, 44, 19, r'$\sin 3\theta=3\cos^2\theta\,\sin\theta-\sin^3\theta$', 'autre', 'l')
text(ax, 44, 5, r'essai $\theta=30°$ : $\frac{3\sqrt{3}}{8}-\frac{3\sqrt{3}}{8}=0=\cos 90°$', 'varie', 's')
save(fig, '39-116')
