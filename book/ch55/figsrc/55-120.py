import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'$\mathbb{Z}/5\mathbb{Z}$ : on calcule $x^5-x$', 'sujet', 'm', weight='bold')
xs = [0, 1, 2, 3, 4]
raw = [x ** 5 for x in xs]            # 0, 1, 32, 243, 1024
rest = [r % 5 for r in raw]           # 0, 1, 2, 3, 4
diff = [(r - x) % 5 for r, x in zip(rest, xs)]
assert raw == [0, 1, 32, 243, 1024] and rest == xs and diff == [0] * 5
fmt = lambda n: f'{n:,}'.replace(',', ' ')
rows = [
    (r'$x$', 'fixe', [str(x) for x in xs]),
    (r'$x^5$', 'fixe', [fmt(v) for v in raw]),
    ('reste', 'varie', [str(v) for v in rest]),
    (r'$x^5-x$', 'resultat', [str(v) for v in diff]),
]
y = 46
for lab, role, cells in rows:
    text(ax, 3, y + 4, lab, role, 'm', ha='left')
    for j, c in enumerate(cells):
        box(ax, 24 + j * 12.2, y, 11, 8, role, label=c, size='m')
    y -= 11
brace(ax, 24, 24 + 4 * 12.2 + 11, 11, 'resultat', label='0 pour les 5 éléments', size='m')
save(fig, '55-120')
