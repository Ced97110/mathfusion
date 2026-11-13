import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s = 5.4                     # 1 unité = 5,4 mm
ox, oy = 13, 11
Cx, Cy = ox + 4 * s, oy + 4.5 * s
R = math.sqrt(36.25)        # ≈ 6,02
arrow(ax, (3, oy), (86, oy), 'fixe', lw=0.7)
arrow(ax, (ox, 4), (ox, 71), 'fixe', lw=0.7)
line(ax, [(Cx + R * s * math.cos(t), Cy + R * s * math.sin(t)) for t in [2 * math.pi * i / 400 for i in range(401)]], 'sujet', lw=1.4)
# θ = 0 : r = 8 ; θ = 90° : r = 9
line(ax, [(ox, oy), (ox + 8 * s, oy)], 'varie', lw=2.0)
line(ax, [(ox, oy), (ox, oy + 9 * s)], 'varie', lw=2.0)
disc(ax, ox + 8 * s, oy, 1.1, 'varie')
disc(ax, ox, oy + 9 * s, 1.1, 'varie')
text(ax, 36, oy - 4.5, 'θ = 0 : r = 8', 'varie', 's')
text(ax, ox + 3.5, oy + 9 * s - 6.5, 'θ = 90° : r = 9', 'varie', 's', ha='left')
# centre et rayon
line(ax, [(Cx, Cy), (ox, oy)], 'fixe', lw=0.9, dash=True)
disc(ax, Cx, Cy, 1.2, 'resultat')
text(ax, Cx + 2, Cy + 4, 'centre (4 ; 4,5)', 'resultat', 's', ha='left')
text(ax, 17, 24, 'rayon ≈ 6,02', 'fixe', 's', ha='left') if False else None
text(ax, 31, 21.5, 'rayon ≈ 6,02', 'fixe', 's', ha='left')
disc(ax, ox, oy, 1.1, 'sujet')
text(ax, ox - 3.2, oy - 3.2, 'O', 'sujet', 's')
text(ax, 2, 80, 'r = 8 cos θ + 9 sin θ', 'encre', 'm', ha='left')
text(ax, 2, 74.5, '(x − 4)² + (y − 4,5)² = 36,25', 'sujet', 's', ha='left')
save(fig, '40-105')
