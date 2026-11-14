import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
x0, y0, s = 8, 6, 6
n = 0
for r in range(5):
    for c in range(5):
        if n >= 21: break
        box(ax, x0 + c * s, y0 + (4 - r) * s, s - 0.6, s - 0.6, 'fixe' if n < 20 else 'resultat', r=0.3, lw=0.6)
        n += 1
text(ax, 42, 40, '7 × 3 = 21 cases', 'sujet', 'm', ha='left')
text(ax, 42, 31, '4 lignes de 5', 'fixe', 'm', ha='left')
text(ax, x0 + 7.5, y0 + 2.7, 'reste 1 = le neutre', 'resultat', 'm', ha='left', weight='bold')
text(ax, 42, 19, 'donc 7 × 3 donne 1', 'resultat', 'm', ha='left')
text(ax, 42, 11, '3 est l’inverse de 7', 'encre', 'm', ha='left', weight='bold')
save(fig, '44-147')
