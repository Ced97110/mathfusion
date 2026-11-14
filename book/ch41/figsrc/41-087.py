import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
from matplotlib.patches import Arc
fig, ax = canvas(60)
ox, oy, s = 56, 8, 7.5
P = lambda x, y: (ox + s * x, oy + s * y)
rows = [('sujet', r'$1\times4+3\times2=10$'),
        ('fixe', r'$\sqrt{10}$ et $\sqrt{20}$'),
        ('varie', r'$\cos\theta\approx0{,}7071$'),
        ('resultat', r'$\theta=45^\circ$')]
y = 56
for i, (role, lab) in enumerate(rows):
    y -= 10
    box(ax, 2, y, 42, 9, role, label=lab, size='s')
    if i < 3:
        arrow(ax, (23, y), (23, y - 1.6), 'fixe', lw=0.8)
    y -= 4.4 if False else 3
arrow(ax, P(0, 0), P(1, 3), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(4, 2), 'autre', lw=1.4)
ax.add_patch(Arc((ox, oy), 18, 18, theta1=math.degrees(math.atan2(2, 4)), theta2=math.degrees(math.atan2(3, 1)), color=COL['resultat'], lw=1.6, zorder=4))
text(ax, ox - 3, oy + 21, r'$\langle1,3\rangle$', 'sujet', 's')
text(ax, ox + 25, oy + 5, r'$\langle4,2\rangle$', 'autre', 's')
text(ax, ox + 22, oy + 20, r'$\theta$', 'resultat', 'm')
save(fig, '41-087')
