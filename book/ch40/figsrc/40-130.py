import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(100)
cx, cy, k = 44.5, 46, 0.22
p, e = 149.6, 0.017
rf = lambda t: k * p / (1 + e * math.cos(t))
th = np.linspace(0, 2 * math.pi, 600)
line(ax, [(cx + rf(t) * math.cos(t), cy + rf(t) * math.sin(t)) for t in th], 'sujet', lw=1.4)
line(ax, [(cx, cy), (cx + rf(0), cy)], 'varie', lw=1.0)
line(ax, [(cx, cy), (cx - rf(math.pi), cy)], 'varie', lw=1.0)
disc(ax, cx, cy, 1.8, 'varie')
disc(ax, cx + rf(0), cy, 1.1, 'resultat')
disc(ax, cx - rf(math.pi), cy, 1.1, 'resultat')
text(ax, cx + 16, cy + 3, 'r ≈ 147,1', 'varie', 's')
text(ax, cx - 16, cy + 3, 'r ≈ 152,2', 'varie', 's')
text(ax, cx + rf(0) - 3, cy - 4, 'θ = 0', 'resultat', 's', ha='right')
text(ax, cx - rf(math.pi) + 3, cy - 4, 'θ = π', 'resultat', 's', ha='left')
text(ax, cx, cy - 5, 'Soleil (pôle)', 'varie', 's')
text(ax, 44, 95, r'$r=\frac{p}{1+e\cos\theta}$', 'sujet', 'l')
text(ax, 44, 88, 'Newton, 1687', 'encre', 's')
text(ax, 44, 4, 'Terre : p = 149,6 ; e = 0,017\n(distances en millions de km)', 'encre', 's')
save(fig, '40-130')
