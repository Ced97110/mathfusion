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

fig, ax = canvas(70)
text(ax, 22, 64, '$H$ vide', 'limite', 'm'); text(ax, 66, 64, '$H$ non vide', 'sujet', 'm')
clock(ax, 22, 40, 13, {})
ax.add_patch(Circle((22, 53), 3.2, ec=COL['limite'], fc='none', lw=1.0, ls='--'))
text(ax, 22, 40, 'aucun\nélément', 'limite', 's')
text(ax, 22, 21, '0 absent : pas de neutre', 'limite', 's')
text(ax, 22, 14, 'rien à tester', 'limite', 's')
pos = clock(ax, 66, 40, 13, {0: 'sujet', 4: 'sujet', 8: 'sujet'}, dr=2.6, labels=(0, 4, 8))
text(ax, 66, 21, 'on choisit 4 deux fois', 'sujet', 's')
text(ax, 66, 14, '4 − 4 = 0 est dans $H$', 'resultat', 's')
save(fig, '46-044')
