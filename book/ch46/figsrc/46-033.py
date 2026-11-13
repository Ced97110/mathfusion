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
text(ax, 44, 57, r'{$e$} : un seul élément, le neutre', 'sujet', 'l')
xs = [12, 34, 56, 77]
clock(ax, xs[0], 36, 7.5, {0: 'sujet'})
clock(ax, xs[1], 36, 7.5, {k: 'fixe' for k in range(12)})
clock(ax, xs[2], 36, 7.5, {0: 'autre', 4: 'autre', 8: 'autre'})
clock(ax, xs[3], 36, 7.5, {})
ax.add_patch(Circle((xs[3], 36), 10, ec=COL['limite'], fc='none', lw=0.8, ls='--'))
ax.add_patch(Circle((xs[0], 36), 10, ec=COL['sujet'], fc='none', lw=0.9))
for x, a, b, r in zip(xs, ['{0}', '12 éléments', '{0, 4, 8}', 'aucun élément'], ['trivial', 'groupe entier', 'plusieurs', 'partie vide'], ['sujet', 'fixe', 'autre', 'limite']):
    text(ax, x, 20, a, r, 's'); text(ax, x, 14, b, r, 's')
text(ax, 44, 6, 'seul le sous-groupe trivial a 1 élément', 'encre', 's')
save(fig, '46-033')
