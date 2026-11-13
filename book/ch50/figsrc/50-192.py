import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
Hs = [0, 3, 6, 9]; Ks = [0, 2, 4, 6, 8, 10]
x0, y0, cw, ch = 16, 6, 11.3, 9
hi = {(0, 0): ('0', 'limite'), (2, 3): ('0', 'limite'), (1, 1): ('5', 'sujet'), (3, 4): ('5', 'sujet')}
for j, k in enumerate(Ks): text(ax, x0 + (j + 0.5) * cw, y0 + 4 * ch + 4, str(k), 'autre', 'm')
for i, h in enumerate(Hs):
    yy = y0 + (3 - i) * ch
    text(ax, x0 - 5, yy + ch / 2, str(h), 'sujet', 'm')
    for j, k in enumerate(Ks):
        assert (h + k) % 12 == {(0,0):0,(2,3):0,(1,1):5,(3,4):5}.get((i, j), (h + k) % 12)
        role = hi[(i, j)][1] if (i, j) in hi else 'fixe'
        box(ax, x0 + j * cw, yy, cw, ch, role, label=hi[(i, j)][0] if (i, j) in hi else None, size='m', lw=0.6, r=0.3, weight='bold')
save(fig, '50-192')
