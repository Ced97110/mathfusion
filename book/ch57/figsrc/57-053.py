import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'on fixe seulement $\eta(1)=3$', 'varie', 'm')
text(ax, 8, 36, r'$n$', 'sujet', 'm')
text(ax, 8, 12, r'$\eta(n)$', 'varie', 'm')
xs = [22 + i * 16 for i in range(4)]
ns = [1, 2, 3, 5]
vals = [3, 6, 9, 15]
for i, (x, n, v) in enumerate(zip(xs, ns, vals)):
    box(ax, x, 31, 13, 10, 'sujet', label=str(n))
    box(ax, x, 7, 13, 10, 'varie' if i == 0 else 'resultat', label=str(v), weight='bold' if i == 0 else 'normal')
    arrow(ax, (x + 6.5, 30.5), (x + 6.5, 17.5), 'varie' if i == 0 else 'resultat')
text(ax, 54, 3, r'$\eta(n)=3\times n$ pour tout $n$', 'resultat', 's')
save(fig, '57-053')
