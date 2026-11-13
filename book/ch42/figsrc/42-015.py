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

fig, ax = canvas(92)
pos = layout(37, 24, 12, 22)
path = [(), ('a',), ('a', 'b'), ('a', 'b', 'c')]
edges(ax, pos, 8, 'fixe', 0.9)
for s, t in zip(path, path[1:]):
    line(ax, [(pos[s][0], pos[s][1] + 4), (pos[t][0], pos[t][1] - 4)], 'varie', lw=2.4)
bags(ax, pos, 20, 8, {s: 'varie' for s in path})
for l, n in enumerate(['3 choix', 'puis 2', 'puis 1']):
    text(ax, 86, 12 + 11 + l * 22, n, 'fixe', 's', ha='right')
text(ax, 44, 3, '3 × 2 × 1 = 6 chemins', 'varie', 'm', weight='bold')
save(fig, '42-015')
