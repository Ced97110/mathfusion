import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 50, 59, r'on fixe seulement $\eta(1)=5$ (horloge à 12 h)', 'varie', 's')
text(ax, 8, 40, r'$n$', 'sujet', 'm')
text(ax, 8, 20, r'$\eta(n)$', 'varie', 'm')
xs = [22 + i * 16 for i in range(4)]
ns = [1, 2, 3, 7]
vals = [5, 10, 3, 11]
for i, (x, n, v) in enumerate(zip(xs, ns, vals)):
    box(ax, x, 35, 13, 10, 'sujet', label=str(n))
    box(ax, x, 15, 13, 10, 'varie' if i == 0 else 'resultat', label=str(v))
    arrow(ax, (x + 6.5, 34.5), (x + 6.5, 25.5), 'varie' if i == 0 else 'resultat')
text(ax, xs[2] + 6.5, 10, '15 − 12', 'fixe', 's')
text(ax, xs[3] + 6.5, 10, '35 − 24', 'fixe', 's')
text(ax, 54, 3, 'multiplier par 5, puis retour dans 12 h', 'resultat', 's')
save(fig, '57-058')
