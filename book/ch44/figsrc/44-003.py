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

fig, ax = canvas(62)
xs = [14, 44, 74]
tile(ax, xs[0], 40, 6, P(0)); tile(ax, xs[1], 40, 6, P(1))
tile(ax, xs[2], 40, 6, [3 - ((i + 1) % 4) for i in range(4)])
arrow(ax, (21, 40), (37, 40), 'varie'); text(ax, 29, 49, 'quart de tour', 'varie', 's')
arrow(ax, (51, 40), (67, 40), 'varie'); text(ax, 59, 49, 'retournement', 'varie', 's')
arrow(ax, (14, 33), (74, 33), 'resultat', curve=0.25)
text(ax, 44, 20, 'un seul mouvement', 'resultat', 's')
save(fig, '44-003')
