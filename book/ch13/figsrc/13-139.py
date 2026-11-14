import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def row(y, l, r, rl, rr):
    box(ax, 6, y, 30, 10, rl, label=l); text(ax, 44, y + 5, '=', 'encre', 'l'); box(ax, 52, y, 30, 10, rr, label=r)
row(54, r'$x + 5$', '2', 'sujet', 'fixe')
for x in (21, 67):
    arrow(ax, (x, 53), (x, 35), 'varie'); text(ax, x + 2, 44, r'$+(-5)$', 'varie', 's', ha='left')
row(24, r'$x$', r'$-3$', 'sujet', 'resultat')
text(ax, 44, 14, 'même nombre des deux côtés', 'varie', 's')
text(ax, 44, 8, r'$5 + (-5) = 0$', 'fixe', 's')
save(fig, '13-139')
