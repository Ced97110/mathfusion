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

fig, ax = canvas(62)
box(ax, 2, 14, 84, 36, 'autre', dash=True)
text(ax, 44, 45, 'ensemble des parties', 'autre', 'm', weight='bold')
for i, s in enumerate(LV[0] + LV[1] + LV[2] + LV[3]):
    x, y = 5 + (i % 4) * 20.5, 28 - (i // 4) * 11 + 0
    box(ax, x, y, 18, 8, 'varie' if s == ('a', 'b') else 'sujet', label=lab(s), size='s')
    if s == ('a', 'b'): hx, hy = x + 9, y
arrow(ax, (hx, 8), (hx, hy - 0.5), 'varie')
text(ax, hx, 4, 'un sous-ensemble', 'varie', 's')
save(fig, '42-003')
