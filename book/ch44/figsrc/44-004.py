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
tile(ax, 16, 62, 6, P(0)); tile(ax, 72, 62, 6, P(1))
arrow(ax, (24, 66), (64, 66), 'varie'); text(ax, 44, 70.5, 'quart de tour', 'varie', 's')
arrow(ax, (64, 58), (24, 58), 'resultat'); text(ax, 44, 53.5, '3 quarts de tour : retour', 'resultat', 's')
tile(ax, 16, 24, 6, P(0)); tile(ax, 72, 24, 6, P(0, True))
arrow(ax, (24, 24), (64, 24), 'varie', both=True); text(ax, 44, 29, 'retournement', 'varie', 's')
text(ax, 44, 18, 'le même, 2 fois : retour', 'resultat', 's')
save(fig, '44-004')
