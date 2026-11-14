import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(56)
f = numberline(ax, 8, 70, 28, -4, 4, every=2)
ax.add_patch(Rectangle((f(-1), 26.4), f(1) - f(-1), 3.2, ec=COL['limite'], fc=FILL['limite'], lw=0.8, zorder=2.5))
text(ax, f(0), 17, 'jamais entre −1 et 1', 'limite', 's')
for v, lab, ha, x in ((1.2208, '35° : 1,2208', 'right', 50), (2, '60° : 2', 'left', 53)):
    line(ax, [(f(v), 28), (f(v), 38.5)], 'resultat'); disc(ax, f(v), 28, 1.0, 'resultat')
    text(ax, x, 41, lab, 'resultat', 's', ha=ha)
line(ax, [(75.5, 29), (75.5, 38.5)], 'resultat', dash=True)
text(ax, 86, 47, '89° : 57,30 →', 'resultat', 's', ha='right')
text(ax, 44, 52, '|sec θ| ≥ 1', 'encre', 'm', weight='bold')
save(fig, '31-105')
