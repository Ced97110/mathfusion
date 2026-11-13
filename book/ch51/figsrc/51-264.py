import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(64)
cx, cy, d = 25, 32, 8
text(ax, cx, 59, r'$\mathbb{Z}[i]$ : tous les $a+bi$', 'sujet', 's')
for a in range(-2, 3):
    for b in range(-2, 3):
        disc(ax, cx + a * d, cy + b * d, 1.6, 'sujet')
for (a, b), s in (((0, 0), '0'), ((1, 0), '1'), ((2, 0), '2'), ((0, 1), r'$i$')):
    text(ax, cx + a * d, cy + b * d - 4.2 if (a, b) != (0, 1) else cy + d + 4, s, 'encre', 's')
L = 2 * d + 3
arrow(ax, (cx + L, cy), (cx + L + 6, cy), 'varie'); arrow(ax, (cx - L, cy), (cx - L - 6, cy), 'varie')
arrow(ax, (cx, cy + L), (cx, cy + L + 5), 'varie'); arrow(ax, (cx, cy - L), (cx, cy - L - 5), 'varie')
box(ax, 54, 40, 32, 10, 'resultat', 'intègre : oui', 's')
box(ax, 54, 27, 32, 10, 'limite', 'fini : non', 's')
box(ax, 54, 9, 32, 14, 'fixe', 'théorème : ne dit\nrien ici', 's')
save(fig, '51-264')
