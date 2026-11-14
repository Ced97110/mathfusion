import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def row(ax, x0, y, n, roles, labels=None, st=5.6, w=5.0, h=5.0):
    for k in range(1, n + 1):
        r = roles.get(k)
        box(ax, x0 + (k - 1) * st, y, w, h, r or "fixe", fill=r is not None, dash=r is None,
            label=(labels or {}).get(k), size="s", r=0.6)

fig, ax = canvas(66)
text(ax, 2, 62, 'vert : nombre qui engendre tout', 'resultat', 's', ha='left')
y = 40
for n, g in [(6, [1, 5]), (12, [1, 5, 7, 11]), (7, [1, 2, 3, 4, 5, 6])]:
    text(ax, 2, y + 9, f'{n} heures : {len(g)} générateurs', 'encre', 'm', ha='left')
    row(ax, 6, y, n, {k: 'resultat' for k in g}, labels={k: str(k) for k in g} if n != 7 else None)
    y -= 16
save(fig, '46-129')
