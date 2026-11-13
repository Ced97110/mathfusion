import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

LV = [[()], [('a',), ('b',), ('c',)], [('a', 'b'), ('a', 'c'), ('b', 'c')], [('a', 'b', 'c')]]
def lab(s):
    return '∅' if not s else r'$\{' + ','.join(s) + r'\}$'
def layout(cx, step, y0, dy):
    pos = {}
    for l, row in enumerate(LV):
        for i, s in enumerate(row):
            pos[s] = (cx + (i - (len(row) - 1) / 2) * step, y0 + l * dy)
    return pos
def edges(ax, pos, h, role='fixe', lw=0.9, keep=None):
    for s in pos:
        for t in pos:
            if len(t) == len(s) + 1 and set(s) < set(t) and (keep is None or (s, t) in keep):
                line(ax, [(pos[s][0], pos[s][1] + h / 2), (pos[t][0], pos[t][1] - h / 2)], role, lw)
def bags(ax, pos, w, h, roles=None, size='m'):
    roles = roles or {}
    for s, (x, y) in pos.items():
        box(ax, x - w / 2, y - h / 2, w, h, roles.get(s, 'sujet'), label=lab(s), size=size)

fig, ax = canvas(88)
pos = layout(37, 24, 12, 22)
edges(ax, pos, 8, 'fixe', 1.0)
bags(ax, pos, 20, 8)
for l, n in enumerate(['0 objet', '1 objet', '2 objets', '3 objets']):
    text(ax, 86, 12 + l * 22, n, 'fixe', 's', ha='right')
save(fig, '42-008')
