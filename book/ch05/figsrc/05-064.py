import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
y = 14
xs = {2: 8, 3: 20, 6: 34, 10: 50, 59: 63, 60: 78}
for v, x in xs.items():
    box(ax, x - 5, y - 4.5, 10, 9, 'sujet' if v == 60 else 'fixe', label=str(v), size='m')
arrow(ax, (xs[60] - 2, y + 5), (xs[10] + 2, y + 5), 'resultat', curve=0.28)
arrow(ax, (xs[60] - 4, y + 5), (xs[6] + 2, y + 5), 'resultat', curve=0.28)
arrow(ax, (xs[6] - 2, y + 5), (xs[2] + 2, y + 5), 'varie', curve=0.35)
arrow(ax, (xs[6] - 1, y + 5), (xs[3] + 2, y + 5), 'varie', curve=0.35)
text(ax, 62, 32, "60 s'appuie sur 6 et 10", 'resultat', 's')
text(ax, 22, 32, "6 s'appuie sur 2 et 3", 'varie', 's')
arrow(ax, (xs[60] - 5.5, y), (xs[59] + 5.5, y), 'limite', lw=0.9)
line(ax, [(xs[59] + 6, y - 1.6), (xs[59] + 9, y + 1.6)], 'limite', lw=1.1)
line(ax, [(xs[59] + 6, y + 1.6), (xs[59] + 9, y - 1.6)], 'limite', lw=1.1)
text(ax, 66, 4, 'pas sur 59, le précédent', 'limite', 's')
save(fig, '05-064')
