import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 14, 10, 11
s5 = 5 ** 0.5
for a in range(0, 7):
    for b in (0, 1, 2):
        disc(ax, ox + a * u, oy + b * s5 * u, 0.7, 'fixe')
arrow(ax, (ox - 6, oy), (ox + 6 * u + 6, oy), 'fixe', lw=0.7)
hx, hy = ox + 3 * u, oy + 2 * s5 * u
line(ax, [(hx, oy), (hx, hy)], 'varie', dash=True)
line(ax, [(ox, hy), (hx, hy)], 'varie', dash=True)
disc(ax, hx, hy, 1.6, 'sujet')
text(ax, hx + 3, hy + 3, '3 + 2√−5', 'sujet', 's', ha='left')
disc(ax, hx, oy, 1.6, 'resultat')
text(ax, hx, oy - 4, '3', 'resultat', 's')
text(ax, hx + 2, oy + 5, 'a = 3', 'varie', 's', ha='left')
text(ax, ox + 15, hy + 3.5, '2 × 2,236 ≈ 4,47', 'varie', 's')
text(ax, ox + 6 * u - 8, oy + 4.5, 'entiers : b = 0', 'fixe', 's')
save(fig, '56-011')
