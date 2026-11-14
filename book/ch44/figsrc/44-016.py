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

fig, ax = canvas(64)
tile(ax, 24, 38, 10, P(0), 'all'); tile(ax, 64, 38, 10, P(0, True), 'all')
line(ax, [(8, 38), (35, 38)], 'fixe', dash=True)
text(ax, 10, 42, 'axe', 'fixe', 's')
arrow(ax, (38, 38), (51, 38), 'varie'); text(ax, 43.5, 43, r'$s$', 'varie', 'm')
text(ax, 24, 23, 'départ', 'encre', 's'); text(ax, 64, 23, r'après $s$', 'encre', 's')
text(ax, 44, 12, 'le haut passe en bas', 'encre', 's')
save(fig, '44-016')
