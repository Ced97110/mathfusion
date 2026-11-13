import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
r, c1, c2, cy = 26, 28.5, 59.5, 33
d = c2 - c1; h = math.sqrt(r * r - (d / 2) ** 2); a0 = math.atan2(h, d / 2)
ts = [-a0 + 2 * a0 * i / 40 for i in range(41)]
lens = [(c2 + r * math.cos(math.pi - t) * 1 - 0, cy + r * math.sin(math.pi - t)) for t in ts] if False else None
pts = [(c1 + r * math.cos(t), cy + r * math.sin(t)) for t in ts] + [(c2 - r * math.cos(t), cy + r * math.sin(t)) for t in reversed(ts)]
poly(ax, pts, 'sujet')
disc(ax, c1, cy, r, 'fixe', fill=False, lw=1.0); disc(ax, c2, cy, r, 'autre', fill=False, lw=1.0)
text(ax, c1 - 6, cy + r + 4, r'$O(n)$', 'fixe', 'm', weight='bold')
text(ax, c2 + 6, cy + r + 4, r'$SL_n(\mathbb{R})$', 'autre', 'm', weight='bold')
text(ax, 44, cy + 6, r'$SO(n)$', 'sujet', 's', weight='bold'); text(ax, 44, cy - 3, 'quart de tour', 'sujet', 's')
text(ax, 18, cy, 'miroir', 'fixe', 's'); text(ax, 70, cy, 'cisaillement', 'autre', 's')
text(ax, 44, 3, r'$SO(n)=O(n)\cap SL_n(\mathbb{R})$', 'encre', 's')
save(fig, '73-074')
