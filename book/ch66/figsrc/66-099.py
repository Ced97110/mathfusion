import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 24, 32, 16
V = [(cx + R * math.cos(math.radians(k * 360 / 7)), cy + R * math.sin(math.radians(k * 360 / 7))) for k in range(7)]
disc(ax, cx, cy, R, 'fixe', fill=False)
poly(ax, V, 'fixe')
line(ax, [(cx - R - 1, cy), (cx + 2 * R * math.cos(math.radians(360 / 7)) + 3, cy)], 'fixe')
line(ax, [V[1], V[6]], 'fixe', dash=True)
for i, v in enumerate(V):
    disc(ax, v[0], v[1], 1.1, 'sujet' if i == 1 else ('autre' if i == 6 else 'fixe'))
disc(ax, 2 * V[1][0] - cx, cy, 1.4, 'resultat')
text(ax, V[1][0] + 3.5, V[1][1] + 2.5, 'ζ', 'sujet', 'm')
text(ax, V[6][0] + 5, V[6][1] - 2.5, 'ζ⁻¹', 'autre', 'm')
text(ax, 2 * V[1][0] - cx + 0.5, cy + 3.6, 'y', 'resultat', 'm')
text(ax, 66, 57, 'φ(7) = 6', 'encre', 'l')
text(ax, 66, 50, 'y = ζ + ζ⁻¹ ≈ 1,247', 'resultat', 's')
text(ax, 66, 43, 'y³ + y² − 2y − 1 = 0', 'sujet', 'm')
text(ax, 66, 36, 'y³ ≈ 1,939 ; y² ≈ 1,555', 'fixe', 's')
text(ax, 66, 29, '1,939 + 1,555 − 2,494 − 1 = 0', 'fixe', 's')
text(ax, 66, 17, 'degré 3, pas puissance de 2', 'limite', 's')
text(ax, 66, 11, 'heptagone impossible', 'limite', 'm', weight='bold')
save(fig, '66-099')
