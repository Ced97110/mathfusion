import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [34, 55, 76]
rows = [(68, 'premier', [r'$3x^2$', r'$x$', r'$-12$'], 'sujet'),
        (52, 'second', [r'$8x^2$', r'$-5x$', r'$+2$'], 'autre'),
        (30, 'signes changés', [r'$-8x^2$', r'$+5x$', r'$-2$'], 'varie'),
        (10, 'résultat', [r'$3-8=-5$', r'$1+5=6$', r'$-12-2=-14$'], 'resultat')]
for y, lab, v, r in rows:
    text(ax, 1, y + 4, lab, r, 's', ha='left')
    for x, s in zip(xs, v): box(ax, x - 10, y, 20, 8, r, label=s, size='s')
for x in xs: arrow(ax, (x, 51.5), (x, 39.0), 'varie')
for x in xs: arrow(ax, (x, 29.5), (x, 19.0), 'resultat')
text(ax, 44, 45, 'chaque signe change', 'varie', 's')
save(fig, '15-117')
