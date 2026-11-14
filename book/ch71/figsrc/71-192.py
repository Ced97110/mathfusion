import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(58)
cx, cy, k = 44, 29, 11
arrow(ax, (cx - 28, cy), (cx + 30, cy), 'fixe', lw=0.6); arrow(ax, (cx, cy - 22), (cx, cy + 24), 'fixe', lw=0.6)
line(ax, [(cx - 19, cy - 19), (cx + 19, cy + 19)], 'varie', dash=True)
line(ax, [(cx - 19, cy + 19), (cx + 19, cy - 19)], 'varie', dash=True)
for sg in (1, -1):
    line(ax, [(cx + sg * k * math.cosh(t / 10), cy + k * math.sinh(t / 10)) for t in range(-12, 13)], 'sujet', lw=1.4)
arrow(ax, (cx, cy), (cx + k, cy + k), 'resultat', lw=1.0); arrow(ax, (cx, cy), (cx + k, cy - k), 'resultat', lw=1.0)
text(ax, cx + k - 3, cy + k + 2, '(1, 1)', 'resultat', 's', ha='right')
text(ax, cx + k - 3, cy - k - 2, '(1, −1)', 'resultat', 's', ha='right')
text(ax, 64, 51, '$y=x$', 'varie', 's'); text(ax, 64, 7, '$y=-x$', 'varie', 's')
text(ax, 2, 53, '$x^2-y^2=1$', 'sujet', 's', ha='left')
text(ax, 2, 7, '$Q=0$ sur les pointillés', 'varie', 's', ha='left')
save(fig, '71-192')
