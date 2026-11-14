import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box; box = lambda ax, x, y, w, h, role, label=None, size="m", **k: _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(98)
box(ax, 2, 82, 26, 11, 'sujet', r'$1+2i$', 'm')
box(ax, 31, 82, 26, 11, 'sujet', r'$3+i$', 'm')
box(ax, 60, 82, 26, 11, 'resultat', r'$1+7i$', 'm')
text(ax, 29.5, 87.5, r'$\times$', 'varie', 'l'); text(ax, 58.5, 87.5, '=', 'varie', 'l')
for x, role in ((15, 'sujet'), (44, 'sujet'), (73, 'resultat')):
    arrow(ax, (x, 80.5), (x, 74), role)
box(ax, 2, 62, 26, 11, 'sujet', r'$N=5$', 'm')
box(ax, 31, 62, 26, 11, 'sujet', r'$N=10$', 'm')
box(ax, 60, 62, 26, 11, 'resultat', r'$N=50$', 'm')
# 5 rows of 10 dots = 50
x0, y0, d = 10, 22, 7.0
for r in range(5):
    for c in range(10):
        disc(ax, x0 + c * d, y0 + r * d, 2.2, 'resultat')
brace(ax, x0 - 2.2, x0 + 9 * d + 2.2, y0 - 3, 'sujet', '10 colonnes', True, 's')
text(ax, 4, y0 + 2 * d, '5', 'sujet', 'm', ha='center')
text(ax, 44, 57, r'$5\times 10 = 50$', 'resultat', 'l')
text(ax, 44, 8, r'$5+10 = 15 \neq 50$', 'limite', 'm')
save(fig, '51-258')
