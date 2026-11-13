import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(62)
box(ax, 2, 6, 40, 50, 'varie', fill=False, dash=True)
box(ax, 46, 6, 40, 50, 'resultat', fill=False, dash=True)
text(ax, 22, 50, r'$3\ \div\ \sqrt{5}$', 'varie', 'l')
text(ax, 22, 42, '√5 ≈ 2,236…', 'varie', 'm')
for i, d in enumerate('2236'):
    box(ax, 6 + i * 7.5, 28, 6.5, 8, 'varie', label=d)
text(ax, 38, 32, '…', 'varie', 'l')
text(ax, 22, 20, 'décimales sans fin', 'varie', 's')
text(ax, 22, 11, 'pénible à la main', 'varie', 's')
text(ax, 66, 50, r'$3\ \div\ 5$', 'resultat', 'l')
for i in range(5):
    box(ax, 50 + i * 6.8, 28, 6, 8, 'resultat', label='5' if i == 0 else None)
text(ax, 66, 20, 'un entier', 'resultat', 's')
text(ax, 66, 11, 'facile', 'resultat', 's')
save(fig, '22-083')
