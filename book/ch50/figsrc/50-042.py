import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
cx, cy, R = 44, 38, 24
P = lambda a, r: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
poly(ax, [P(a, R) for a in (90, 210, 330)], 'fixe')
for a, role, nm in [(90, 'sujet', r'$P_1$'), (210, 'autre', r'$P_2$'), (330, 'fixe', r'$P_3$')]:
    line(ax, [P(a, 29), P(a + 180, 15)], role, lw=1.6)
    text(ax, *P(a, 34), nm, role, 'l')
pts = [P(110 + 80 * i / 30, 31) for i in range(31)]
line(ax, pts, 'varie', lw=1.3)
arrow(ax, pts[-3], pts[-1], 'varie', lw=1.3)
text(ax, 3, 66, r'$a$ : un tiers de tour', 'varie', 'm', ha='left')
text(ax, 44, 7, r'$P_2=aP_1a^{-1}$', 'encre', 'l')
save(fig, '50-042')
