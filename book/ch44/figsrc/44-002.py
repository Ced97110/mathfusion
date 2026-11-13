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

fig, ax = canvas(84)
text(ax, 14, 78, 'position', 'sujet', 'm', weight='bold'); text(ax, 42, 78, 'geste', 'varie', 'm', weight='bold'); text(ax, 72, 78, 'position', 'sujet', 'm', weight='bold')
tile(ax, 14, 44, 7, P(0)); text(ax, 14, 32, 'départ', 'encre', 's')
tile(ax, 72, 62, 7, P(1)); text(ax, 72, 51, 'obtenue', 'encre', 's')
tile(ax, 72, 24, 7, P(0, True)); text(ax, 72, 13, 'obtenue', 'encre', 's')
arrow(ax, (23, 48), (60, 62), 'varie', lw=1.6); text(ax, 40, 61, 'quart de tour', 'varie', 's')
arrow(ax, (23, 40), (60, 26), 'varie', lw=1.6); text(ax, 40, 26, 'retournement', 'varie', 's')
disc(ax, 5, 5, 1.6, 'varie'); text(ax, 8, 5, 'coin 1', 'varie', 's', ha='left')
disc(ax, 26, 5, 1.1, 'fixe'); text(ax, 29, 5, 'coin 2', 'fixe', 's', ha='left')
save(fig, '44-002')
