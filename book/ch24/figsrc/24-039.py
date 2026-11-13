import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
rows = [('isoler', r'$x+y=5$', r'$y=5-x$', 'y seul, mêmes solutions'),
        ('substituer', None, None, r'$y$ remplacé par $5-x$'),
        ('réduire', r'$2x+5-x$', r'$x+5$', 'même valeur')]
for i, (g, a, b, n) in enumerate(rows):
    yb = 70 - i * 26
    text(ax, 3, yb + 5, g, 'varie', 'l', ha='left', weight='bold')
    if a is not None:
        box(ax, 28, yb, 26, 10, 'sujet', label=a); box(ax, 62, yb, 24, 10, 'resultat', label=b)
    else:
        box(ax, 28, yb, 26, 10, 'sujet'); text(ax, 36, yb + 5, r'$2x+$', 'sujet')
        box(ax, 42, yb + 1.5, 9, 7, 'varie', label=r'$y$')
        box(ax, 62, yb, 24, 10, 'resultat'); text(ax, 70, yb + 5, r'$2x+$', 'resultat')
        box(ax, 74, yb + 1.5, 11, 7, 'varie', label=r'$5-x$')
    arrow(ax, (54, yb + 5), (62, yb + 5), 'varie'); text(ax, 58, yb - 5, n, 'fixe', 's')
save(fig, '24-039')
