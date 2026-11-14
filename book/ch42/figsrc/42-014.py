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

fig, ax = canvas(56)
box(ax, 34, 4, 20, 9, 'sujet', label=lab(('a',)), size='m')
for x, o in [(10, 'b'), (58, 'c')]:
    box(ax, x, 40, 20, 9, 'resultat', label=lab(('a', o)), size='m')
arrow(ax, (40, 13.5), (24, 39.5), 'varie'); arrow(ax, (48, 13.5), (64, 39.5), 'varie')
text(ax, 24, 27, f'+ ${"b"}$', 'varie', 'm', weight='bold', ha='right'); text(ax, 64, 27, '+ $c$', 'varie', 'm', weight='bold', ha='left')
text(ax, 44, 20, 'absents : $b$, $c$', 'fixe', 's') if False else None
text(ax, 44, 22, '2 absents', 'fixe', 's')
save(fig, '42-014')
