import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(100)
s = 2.4
def cells(x, y, groups):
    i = 0
    for n, role in groups:
        for _ in range(n):
            box(ax, x + i * s, y, s, s, role, r=0.1, lw=0.5); i += 1
text(ax, 3, 95, r'$6$ divise $12$ et $18$', 'resultat', 's', ha='left')
cells(3, 86, [(6, 'sujet'), (6, 'varie')]); text(ax, 52, 87.2, r'$12 = 6 \times 2$', 'encre', 's', ha='left')
cells(3, 77, [(6, 'sujet'), (6, 'varie'), (6, 'sujet')]); text(ax, 52, 78.2, r'$18 = 6 \times 3$', 'encre', 's', ha='left')
text(ax, 3, 68, r'$18$ ne divise pas $12$', 'limite', 's', ha='left')
cells(3, 59, [(12, 'fixe')])
for i in range(6): box(ax, 3 + (12 + i) * s, 59, s, s, 'limite', fill=False, r=0.1, lw=0.5, dash=True)
text(ax, 52, 60.2, 'il en manque 6', 'limite', 's', ha='left')
text(ax, 3, 49, r'$x^2$ divise $x^2$ et $x^5$', 'resultat', 's', ha='left')
cells(3, 40, [(2, 'sujet')]); text(ax, 52, 41.2, r'$x^2 = x^2 \times 1$', 'encre', 's', ha='left')
cells(3, 31, [(2, 'sujet'), (3, 'varie')]); text(ax, 52, 32.2, r'$x^5 = x^2 \times x^3$', 'encre', 's', ha='left')
text(ax, 3, 22, r'$x^5$ ne divise pas $x^2$', 'limite', 's', ha='left')
cells(3, 13, [(2, 'fixe')])
for i in range(3): box(ax, 3 + (2 + i) * s, 13, s, s, 'limite', fill=False, r=0.1, lw=0.5, dash=True)
text(ax, 52, 14.2, 'il en manque 3', 'limite', 's', ha='left')
save(fig, '18-034')
