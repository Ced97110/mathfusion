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

fig, ax = canvas(62)
text(ax, 44, 57, 'propre : différent du groupe entier', 'sujet', 'm')
xs = [11, 33, 55, 77]
clock(ax, xs[0], 36, 7.5, {0: 'sujet'})
clock(ax, xs[1], 36, 7.5, {0: 'sujet', 6: 'sujet'})
clock(ax, xs[2], 36, 7.5, {0: 'sujet', 4: 'sujet', 8: 'sujet'})
clock(ax, xs[3], 36, 7.5, {k: 'limite' for k in range(12)})
for x, a in zip(xs, ['{0}', '{0, 6}', '{0, 4, 8}', 'les 12 heures']):
    text(ax, x, 22, a, 'sujet' if x < 70 else 'limite', 's')
brace(ax, 3, 66, 19, 'sujet', 'sous-groupes propres', True)
text(ax, 77, 12, 'pas propre', 'limite', 's')
save(fig, '46-034')
