import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [3, 33, 63]
groups = [r'$S_3$ : 6', r'$A_3$ : 3', r'$1$ : 1']
fields = [r'$K$', r'$K(\sqrt{d})$', r'$E$ : racines']
for i, x in enumerate(xs):
    box(ax, x, 38, 23, 12, 'sujet', label=groups[i], size='s')
    box(ax, x, 8, 23, 12, 'resultat' if i == 2 else 'autre', label=fields[i], size='s')
    line(ax, [(x + 11.5, 38), (x + 11.5, 20)], 'fixe', dash=True)
for i, (a, b) in enumerate((('÷2', r'$+\sqrt{d}$'), ('÷3', r'$+\sqrt[3]{\ \ }$'))):
    arrow(ax, (xs[i] + 23, 44), (xs[i + 1], 44), 'varie')
    text(ax, xs[i] + 26.5, 47.5, a, 'varie', 's')
    arrow(ax, (xs[i] + 23, 14), (xs[i + 1], 14), 'varie')
    text(ax, xs[i] + 26.5, 17.5, b, 'varie', 's')
text(ax, 44, 55, 'une marche du groupe = un radical', 'encre', 's')
text(ax, 44, 3, r'arrêt quand le groupe est $1$', 'resultat', 's')
save(fig, '65-109')
