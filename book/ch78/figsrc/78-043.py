import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(r'$i$','sujet', r'$i$','varie', r'$j$','autre', r'$=0$'),
        (r'$i$','varie', r'$j$','autre', r'$i$','sujet', r'$=j$'),
        (r'$j$','autre', r'$i$','sujet', r'$i$','varie', r'$=-j$')]
for n, row in enumerate(rows):
    y = 48 - n * 17
    for c in range(3):
        box(ax, 8 + c * 18, y, 16, 12, row[2 * c + 1], label=row[2 * c])
    text(ax, 66, y + 6, row[6], 'encre', 'l')
    if n < 2: arrow(ax, (30, y - 0.5), (30, y - 4.5), 'varie', lw=0.9)
text(ax, 16, 65, r'$x$', 'sujet', 'm'); text(ax, 34, 65, r'$y$', 'varie', 'm'); text(ax, 52, 65, r'$z$', 'autre', 'm')
text(ax, 44, 8, 'tourner, puis additionner : 0', 'resultat', 'm')
save(fig, '78-043')
