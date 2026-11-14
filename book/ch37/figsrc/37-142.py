import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 57, 'hauteur = a sin C', 'varie', 'm')
k = 0.3; t = math.radians(53); y0 = 24
P0 = (4, y0); P1 = (4 + 120 * k, y0); T = (4 + 110 * k * math.cos(t), y0 + 110 * k * math.sin(t))
poly(ax, [P0, P1, T], 'sujet'); line(ax, [T, (T[0], y0)], 'varie', dash=True, lw=1.1)
text(ax, T[0] + 2, y0 + 8, '$h$', 'varie', 's', ha='left'); text(ax, 11, y0 + 2.2, '53°', 'fixe', 's')
text(ax, 22, 18.5, 'base 120', 'sujet', 's'); text(ax, 22, 13, 'h = 110 × 0,7986 ≈ 87,85', 'varie', 's'); text(ax, 22, 7, '½ × 120 × 87,85 ≈ 5 271', 'resultat', 's')
S = 6.0; O = (52, y0)
poly(ax, [O, (O[0] + 4 * S, y0), (O[0], y0 + 3 * S)], 'autre')
line(ax, [(O[0] + 2.2, y0), (O[0] + 2.2, y0 + 2.2), (O[0], y0 + 2.2)], 'varie', lw=0.7)
text(ax, O[0] + 6, y0 + 3.5, '90°', 'fixe', 's'); text(ax, O[0] - 1.8, y0 + 9, '$h$', 'varie', 's', ha='right')
text(ax, 66, 18.5, 'base 4', 'autre', 's'); text(ax, 66, 13, 'h = 3 × sin 90° = 3', 'varie', 's'); text(ax, 66, 7, '½ × 4 × 3 = 6', 'resultat', 's')
save(fig, '37-142')
