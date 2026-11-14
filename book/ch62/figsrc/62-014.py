import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, s = 44, 32, 17
R = 2 ** (1 / 3)
P = [(cx + R * s, cy), (cx - R / 2 * s, cy + R * math.sqrt(3) / 2 * s), (cx - R / 2 * s, cy - R * math.sqrt(3) / 2 * s)]
ax.add_patch(Circle((cx, cy), R * s, fill=False, ec=COL['fixe'], ls='--', lw=0.9, zorder=1))
arrow(ax, (cx - 26, cy), (cx + 30, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 27), (cx, cy + 27), 'fixe', lw=0.6)
for x, y in P:
    line(ax, [(cx, cy), (x, y)], 'resultat', lw=1.5)
    disc(ax, x, y, 1.5, 'sujet')
disc(ax, cx, cy, 1.0, 'encre')
text(ax, cx + 3, cy - 3, '0', 'encre', 's')
text(ax, cx + 11, cy + 2.8, '∛2', 'resultat', 'm')
text(ax, cx - 7.5, cy + 10, '∛2', 'resultat', 'm')
text(ax, cx - 7.5, cy - 10, '∛2', 'resultat', 'm')
text(ax, 44, 67, '(distance)$^3$ = 2, donc distance = ∛2 ≈ 1,26', 'encre', 's')
text(ax, 44, 3, 'même distance : un seul cercle', 'resultat', 'm')
save(fig, '62-014')
