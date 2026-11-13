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

fig, ax = canvas(66)
tile(ax, 14, 52, 7, P(0)); tile(ax, 74, 52, 7, P(0))
text(ax, 14, 41, 'départ', 'encre', 's'); text(ax, 74, 41, 'après', 'encre', 's')
arrow(ax, (23, 52), (65, 52), 'varie'); text(ax, 44, 57, 'ne rien faire', 'varie', 's')
arrow(ax, (44, 46), (44, 32), 'varie'); text(ax, 48, 39, 'se note', 'varie', 's', ha='left')
box(ax, 34, 14, 20, 18, 'sujet', label='1', size='xl')
text(ax, 44, 8, 'nom du geste, pas un nombre', 'encre', 's')
save(fig, '44-010')
