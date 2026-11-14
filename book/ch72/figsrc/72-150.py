import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 77, '4 plis du carré', 'sujet', 'm')
cs = [14, 34, 54, 74]; s = 7
for c, ang in zip(cs, [0, 90, 45, 135]):
    cy = 62
    box(ax, c - s, cy - s, 2 * s, 2 * s, 'fixe')
    d = 10.5 if ang in (0, 90) else 10
    t = math.radians(ang)
    line(ax, [(c - d * math.cos(t), cy - d * math.sin(t)), (c + d * math.cos(t), cy + d * math.sin(t))], 'sujet', lw=1.5)
arrow(ax, (8, 48), (8, 32), 'varie')
text(ax, 13, 40, 'produits de 2 plis', 'varie', 's', ha='left')
for k, c in enumerate(cs):
    cy = 20
    box(ax, c - s, cy - s, 2 * s, 2 * s, 'fixe')
    th = math.radians(45 + 90 * k)
    disc(ax, c + 4.5 * 1.414 * math.cos(th), cy + 4.5 * 1.414 * math.sin(th), 1.6, 'varie')
    text(ax, c, cy - 11, ['0', '1 quart', '2 quarts', '3 quarts'][k], 'encre', 's')
text(ax, 44, 4, '4 plis + 4 rotations : 8 symétries', 'resultat', 's')
save(fig, '72-150')
