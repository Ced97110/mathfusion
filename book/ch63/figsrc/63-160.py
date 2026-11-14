import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
cx, cy, R = 44, 50, 26
P = lambda deg, rad=R: (cx + rad * math.cos(math.radians(deg)), cy + rad * math.sin(math.radians(deg)))
ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.6, ls='--', zorder=1))
line(ax, [(cx - R - 6, cy), (cx + R + 2.5, cy)], 'resultat', lw=1.4)
ang = {1: 72, 2: 144, 3: 216, 4: 288}
names = {0: '1', 1: 'ω', 2: 'ω²', 3: 'ω³', 4: 'ω⁴'}
disc(ax, *P(0), 2.3, role='resultat')
text(ax, *P(0, R + 5.5), '1', 'resultat', 'm', weight='bold')
for k, a in ang.items():
    disc(ax, *P(a), 2.3, role='sujet')
    text(ax, *P(a, R + 6.5), names[k], 'sujet', 'm', weight='bold')

def chord(a, b):
    (x0, y0), (x1, y1) = P(ang[a]), P(ang[b])
    d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * 3, y0 + uy * 3), (x1 - ux * 3, y1 - uy * 3), 'varie', lw=1.1)

for a, b in [(1, 2), (2, 4), (4, 3), (3, 1)]:
    chord(a, b)
text(ax, 44, 11, 'σ₂ : ω ↦ ω² ↦ ω⁴ ↦ ω³ ↦ ω (4 pas)', 'varie', 's')
text(ax, 44, 4, 'σ₄ : miroir de l’axe réel (vert)', 'resultat', 's')
save(fig, '63-160')
