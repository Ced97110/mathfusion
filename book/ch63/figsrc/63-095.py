import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, r'6 paires de choix : $r$ puis $j$', 'fixe', 's')
cols = [r'$j\mapsto j$', r'$j\mapsto j^2$']
rows = [r'$r\mapsto r$', r'$r\mapsto jr$', r'$r\mapsto j^2r$']
xs = [34, 62]
for i, c in enumerate(cols):
    text(ax, xs[i] + 10, 59, c, 'sujet', 's')
n = 1
for j, r in enumerate(rows):
    y = 40 - j * 15
    text(ax, 16, y + 6, r, 'autre', 's')
    for i in range(2):
        box(ax, xs[i], y, 20, 12, 'fixe', label=str(n), size='m')
        n += 1
text(ax, 44, 3, r'$3\times2=6$ ; $[E:\mathbb{Q}(r)]=6/3=2$', 'resultat', 's')
save(fig, '63-095')
