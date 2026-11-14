import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def clock(ax, cx, cy, r, roles=None, dr=1.8, labels=(), dashed=False):
    roles = roles or {}
    pos = {}
    for k in range(12):
        x, y = cx + r * math.sin(math.pi * k / 6), cy + r * math.cos(math.pi * k / 6)
        pos[k] = (x, y)
        if k in roles: disc(ax, x, y, dr, roles[k], label=(str(k) if k in labels else None), size='s')
        else: disc(ax, x, y, dr * 0.6, 'fixe', fill=False, lw=0.6)
    return pos

fig, ax = canvas(74)
text(ax, 44, 70, 'test : la différence de deux éléments', 'encre', 's')
clock(ax, 22, 44, 14, {0: 'sujet', 4: 'sujet', 8: 'sujet'}, dr=2.6, labels=(0, 4, 8))
clock(ax, 66, 44, 14, {0: 'autre', 1: 'autre', 2: 'autre', 11: 'limite'}, dr=2.6, labels=(0, 1, 2, 11))
text(ax, 22, 24, '{0, 4, 8}', 'sujet', 'm'); text(ax, 66, 24, '{0, 1, 2}', 'autre', 'm')
text(ax, 22, 16, '4 − 8 = 8', 'resultat', 'm'); text(ax, 66, 16, '1 − 2 = 11', 'limite', 'm')
text(ax, 22, 8, 'reste dedans', 'resultat', 's'); text(ax, 66, 8, 'sort de la partie', 'limite', 's')
save(fig, '46-043')
