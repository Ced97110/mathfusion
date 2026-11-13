import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, 'diviseurs de 12, puis reste dans la division par 5', 'encre', 's')
vals = [1, 2, 3, 4, 6, 12]; rem = [d % 5 for d in vals]
xs = [13 + i * 12.4 for i in range(6)]
for v, r, x in zip(vals, rem, xs):
    ok = r == 1
    box(ax, x - 5, 39, 10, 8, 'sujet', label=str(v))
    arrow(ax, (x, 38.4), (x, 31.6), 'varie')
    box(ax, x - 5, 22, 10, 9, 'resultat' if ok else 'limite', label=str(r), weight='bold' if ok else 'normal')
x1, x6 = xs[0], xs[4]
line(ax, [(x1 - 5, 18), (x1 - 5, 16), (x6 + 5, 16), (x6 + 5, 18)], 'resultat', lw=0.8)
text(ax, 44, 9, r'$n_5 \in \{1,\ 6\}$', 'resultat', 'l', weight='bold')
save(fig, '50-147')
