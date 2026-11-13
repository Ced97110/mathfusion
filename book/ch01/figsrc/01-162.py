import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
X = lambda c: 22 + 8 * (c - 2)
rows = [(2, 60, 'T(2)', 63.5), (3, 48, 'T(3)', 51.5), (4, 36, 'T(4)', 39.5), (5, 24, 'T(5)', 27.5)]
for last, y, lab, yl in rows:
    text(ax, 4, yl, lab, 'encre', 'm', ha='left')
    for c in range(2, last + 1):
        if last == 2: role = 'resultat'
        elif c == last: role = 'varie'
        else: role = 'sujet'
        box(ax, X(c), y, 8, 7, role)
for c in range(2, 6):
    text(ax, X(c) + 4, 27.5, str(c), 'encre', 's')
text(ax, 50, 63.5, 'départ : T(2) = E(2)', 'resultat', 's')
for last, y in [(2, 60), (3, 48), (4, 36)]:
    xc = X(last) + 4
    arrow(ax, (xc, y), (xc + 8, y - 5), 'varie', curve=0.3)
text(ax, 72, 46, 'ajouter E(k + 1)', 'varie', 's')
text(ax, 72, 40, 'grâce au passage fort', 'varie', 's')
text(ax, 44, 15, 'récurrence ordinaire sur T', 'fixe', 's')
text(ax, 44, 6, 'donc E(n) vraie pour tout n', 'resultat', 'm')
save(fig, '01-162')
