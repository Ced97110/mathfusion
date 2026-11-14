import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
cx, cy, R = 44, 48, 30
P = lambda deg, rad=R: (cx + rad * math.cos(math.radians(deg)), cy + rad * math.sin(math.radians(deg)))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
line(ax, [(cx - R - 4, cy), (cx + R + 4, cy)], 'fixe', lw=0.6)
pts = [P(72 * k) for k in range(5)]
poly(ax, pts, role='sujet', fill=False)
line(ax, [(cx, cy), P(0)], 'fixe')
line(ax, [(cx, cy), P(72)], 'varie', lw=1.2)
line(ax, [P(k, 11) for k in range(0, 73, 6)], 'varie', lw=1.0)
text(ax, *P(36, 17), '72°', 'varie', 's')
labs = ['1', 'ω', 'ω²', 'ω³', 'ω⁴']
for k, (p, t) in enumerate(zip(pts, labs)):
    disc(ax, p[0], p[1], 2.2, role='varie' if k == 1 else 'sujet')
    text(ax, *P(72 * k, R + 6), t, 'varie' if k == 1 else 'sujet', 'm', weight='bold')
text(ax, 44, 8, 'ω = cos 72° + i sin 72°', 'encre', 's')
text(ax, 44, 2.5, '5 × 72° = 360° : ω⁵ = 1', 'resultat', 's')
save(fig, '63-156')
