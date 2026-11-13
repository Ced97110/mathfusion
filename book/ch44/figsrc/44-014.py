import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

POS = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # coin en haut a droite, haut a gauche, bas a gauche, bas a droite
def P(k, refl=False):
    """Position (indice dans POS) des coins 1 a 4 apres s (si refl) puis r^k."""
    return [((3 - i) + k) % 4 if refl else (i + k) % 4 for i in range(4)]
def tile(ax, cx, cy, h, idx, nums='mark', role='sujet'):
    poly(ax, [(cx + h, cy + h), (cx - h, cy + h), (cx - h, cy - h), (cx + h, cy - h)], role)
    r = 0.26 * h
    for i in range(4):
        px, py = POS[idx[i]]; x, y = cx + px * h * 0.62, cy + py * h * 0.62
        if i == 0: disc(ax, x, y, r, 'varie', label=None if nums == 'mark' else '1')
        elif nums == 'all': disc(ax, x, y, r, 'fixe', label=str(i + 1))
        elif nums == 'mark' and i == 1: disc(ax, x, y, r * 0.6, 'fixe')

fig, ax = canvas(70)
xs = [11, 33, 55, 77]
for i, x in enumerate(xs): tile(ax, x, 56, 6, P(i))
for a, b in zip(xs, xs[1:]):
    arrow(ax, (a + 7.5, 56), (b - 7.5, 56), 'varie'); text(ax, (a + b) / 2, 64, r'$r$', 'varie', 's')
arrow(ax, (77, 49), (11, 49), 'resultat', curve=-0.3)
text(ax, 44, 31, r'$r$ : quatrième fois', 'varie', 's')
text(ax, 44, 14, r'$r^4 = 1$', 'resultat', 'xl')
save(fig, '44-014')
