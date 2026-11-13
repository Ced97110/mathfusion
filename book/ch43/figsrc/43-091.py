import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cl = [([1, 4], 1), ([2, 5], 2), ([3, 6], 0)]; ys = [52, 34, 16]
text(ax, 44, 67, r'$g(\bar{a})=f(a)$', 'sujet', 'l', weight='bold')
for (els, v), y in zip(cl, ys):
    box(ax, 6, y - 6, 28, 12, 'sujet')
    for k, n in enumerate(els): disc(ax, 14 + k * 12, y, 3.2, 'sujet', label=str(n))
    disc(ax, 74, y, 3.6, 'resultat', label=str(v))
    arrow(ax, (35, y), (69.5, y), 'sujet', lw=1.2)
text(ax, 52, 56, r'$g$', 'sujet', 'l')
text(ax, 20, 5, 'classes', 'sujet', 's'); text(ax, 74, 5, 'restes', 'resultat', 's')
save(fig, '43-091')
