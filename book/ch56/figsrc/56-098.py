import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
f = lambda v: 12 + v * 1.2
ds = [48, 24, 12, 6, 3]
ys = [64, 52, 40, 28, 16]
for i, (d, y) in enumerate(zip(ds, ys)):
    vs = list(range(0, 49, d))
    assert len(vs) == [2, 3, 5, 9, 17][i]
    text(ax, 2, y, f'({d})', 'sujet', 's', ha='left')
    text(ax, 74, y, f'{len(vs)} points', 'fixe', 's', ha='left')
    prev = ds[i - 1] if i else None
    for v in vs:
        new = prev is not None and v % prev != 0
        disc(ax, f(v), y, 0.9, 'varie' if new else 'sujet')
        if i + 1 < len(ds):
            line(ax, [(f(v), y - 1.2), (f(v), ys[i + 1] + 1.2)], 'fixe', lw=0.5)
disc(ax, 22, 5, 0.9, 'sujet')
text(ax, 25, 5, 'gardé', 'sujet', 's', ha='left')
disc(ax, 52, 5, 0.9, 'varie')
text(ax, 55, 5, 'nouveau', 'varie', 's', ha='left')
save(fig, '56-098')
