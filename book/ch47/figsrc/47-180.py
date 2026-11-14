import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, r'$rH\cdot rH$', 'sujet', 'l')
for x, s in [(14, 'représentants'), (43, 'produit'), (72, 'classe')]:
    text(ax, x, 47, s, 'fixe', 's')
rows = [(r'$r\cdot r$', r'$r^2$', r'$r^2H$'), (r'$rs\cdot r$', r'$s$', r'$H$')]
for k, (a, b, c) in enumerate(rows):
    y = 34 - k * 20
    box(ax, 2, y, 24, 9, 'sujet', label=a)
    box(ax, 36, y, 14, 9, 'fixe', label=b)
    box(ax, 60, y, 24, 9, 'varie' if k == 0 else 'autre', label=c)
    arrow(ax, (26, y + 4.5), (36, y + 4.5), 'fixe')
    arrow(ax, (50, y + 4.5), (60, y + 4.5), 'fixe')
text(ax, 72, 28.5, r'$\neq$', 'limite', 'xl'); text(ax, 40, 28.5, 'deux résultats : pas de valeur', 'limite', 's')
save(fig, '47-180')
