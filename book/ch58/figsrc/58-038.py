import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
assert 7 + 2 == 9 and 3 * 7 == 21
text(ax, 20, 52, r'$R^{(1)}$ : listes à 1 case', 'sujet', 's')
text(ax, 68, 52, r'$R$ : nombres', 'autre', 's')
rows = [(32, '(7) + (2) = (9)', '7 + 2 = 9'), (10, '3 × (7) = (21)', '3 × 7 = 21')]
for y, a, b in rows:
    box(ax, 2, y, 36, 10, 'sujet', label=a)
    box(ax, 52, y, 34, 10, 'autre', label=b)
    arrow(ax, (39, y + 5), (51, y + 5), 'varie', both=True)
text(ax, 45, 44, 'même calcul', 'varie', 's')
save(fig, '58-038')
