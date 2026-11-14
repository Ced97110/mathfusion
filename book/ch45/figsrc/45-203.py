import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
s = 10.0; x0, y0 = 36.0, 14.0
H_, K_ = [0, 2, 4], [0, 3]
for j, k in enumerate(K_):
    box(ax, x0 + j * s, y0 + 3 * s + 1, s, s * 0.8, 'autre', label=str(k), r=0.5)
for i, h in enumerate(H_):
    box(ax, x0 - s - 1, y0 + (2 - i) * s, s, s, 'sujet', label=str(h), r=0.5)
    for j, k in enumerate(K_):
        box(ax, x0 + j * s, y0 + (2 - i) * s, s, s, 'resultat', label=str((h + k) % 6), r=0.5, weight='bold')
text(ax, x0 - s / 2 - 1, y0 + 3 * s + 5, 'H', 'sujet', 'm', weight='bold')
text(ax, x0 + s * 2 + 3, y0 + 3 * s + 5, 'K', 'autre', 'm', weight='bold', ha='left')
text(ax, 44, 7, 'h + k : les six heures', 'resultat', 'm')
text(ax, 44, 61, 'ℤ/6 retrouvé', 'encre', 'm') if False else None
save(fig, '45-203')
