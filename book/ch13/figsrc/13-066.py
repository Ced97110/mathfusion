import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, expr):
    f = numberline(ax, 6, 78, y, 0, 9, labels=False)
    for v in (5, 8):
        text(ax, f(v), y - 3.6, f'${v}$', 'fixe')
    disc(ax, f(8), y, 1.8, 'sujet')
    disc(ax, f(5), y, 1.8, 'resultat')
    arrow(ax, (f(8) - 1, y + 3), (f(5) + 1, y + 3), 'varie', curve=0.4)
    text(ax, (f(8) + f(5)) / 2, y + 11, expr, 'varie', 'm')
row(46, r'$8-3$')
row(18, r'$8+(-3)$')
text(ax, 44, 65, 'deux écritures, une arrivée', 'encre', 's')
text(ax, 44, 4, 'même résultat : $5$', 'resultat', 'm')
save(fig, '13-066')
