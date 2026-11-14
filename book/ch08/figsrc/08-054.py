import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
cx = [14.5, 29.5, 44.5, 59.5, 74.5]
for x, h in zip(cx, ['dizaines', 'unités', 'dixièmes', 'centièmes', 'millièmes']):
    text(ax, x, 80, h, 'fixe', 's')
text(ax, 44, 70, '8,315', 'sujet', 'l', weight='bold')
for x, d in zip(cx[1:], '8315'):
    box(ax, x - 6, 50, 12, 11, 'sujet', label=d, size='l')
for x, d in zip(cx[:4], '8315'):
    box(ax, x - 6, 24, 12, 11, 'resultat', label=d, size='l')
for a, b in zip(cx[1:], cx[:4]):
    arrow(ax, (a, 49), (b, 36), 'varie')
text(ax, cx[4], 29, '× 10', 'varie', 'm', weight='bold')
text(ax, 44, 12, '83,15', 'resultat', 'l', weight='bold')
for y in (55.5, 29.5):
    text(ax, (cx[1] + cx[2]) / 2, y - 1.5, ',', 'encre', 'xl', weight='bold')
save(fig, '08-054')
