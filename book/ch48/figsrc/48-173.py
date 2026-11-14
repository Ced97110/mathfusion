import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
def row(y, els, h1, t1, r1, t2, r2):
    text(ax, 44, y + 17, h1, 'encre', 'm')
    n = len(els)
    for i, e in enumerate(els):
        box(ax, 44 + (i - n / 2) * 12.5 + 0.5, y + 3, 11.5, 9, 'sujet', label=str(e), size='m')
    text(ax, 44, y - 4, t1, r1, 's', weight='bold')
    if t2: text(ax, 44, y - 10, t2, r2, 's', weight='bold')
row(46, [0, 3, 6, 9], r'$m = 3$, $n = 4$', r'$n = 4$ et $m + 1 = 4$ : égaux', 'fixe', None, 'fixe')
row(16, [0, 2, 4, 6, 8], r'$m = 2$, $n = 5$', r'$n = 5$ : oui', 'resultat', r'$m + 1 = 3$ : non', 'limite')
save(fig, '48-173')
