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

fig, ax = canvas(78)
text(ax, 44, 71, '4 rotations', 'encre', 's')
text(ax, 44, 38, '4 retournements', 'encre', 's')
names = ['1', r'$r$', r'$r^2$', r'$r^3$', r'$s$', r'$rs$', r'$r^2s$', r'$r^3s$']
for i in range(8):
    row, col = divmod(i, 4)
    cx = 13 + 21 * col; cy = 58 if row == 0 else 25
    tile(ax, cx, cy, 7, P(col, row == 1))
    text(ax, cx, cy - 12, names[i], 'encre', 's')
disc(ax, 20, 5, 1.8, 'varie'); text(ax, 24, 5, 'coin 1', 'encre', 's', ha='left')
disc(ax, 52, 5, 1.1, 'fixe'); text(ax, 56, 5, 'coin 2', 'encre', 's', ha='left')
save(fig, '44-008')
