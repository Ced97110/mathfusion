import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cols = [(9, 1, 'midi'), (28, 2, '13 h'), (47, 4, '14 h'), (72, 8, '15 h')]
for cx, n, h in cols:
    for i in range(n):
        if n == 1: px, py = cx, 38
        elif n == 2: px, py = cx - 2 + 4 * i, 38
        elif n == 4: px, py = cx - 2 + 4 * (i % 2), 40 - 4 * (i // 2)
        else: px, py = cx - 6 + 4 * (i % 4), 40 - 4 * (i // 4)
        disc(ax, px, py, 1.6, 'sujet')
    text(ax, cx, 49, h, 'fixe', 'm')
    text(ax, cx, 27, str(n), 'sujet', 'l', weight='bold')
for a, b in ((14.5, 22), (33.5, 41), (52.5, 62)):
    arrow(ax, (a, 38), (b, 38), 'varie')
    text(ax, (a + b) / 2, 43, '×2', 'varie', 's')
brace(ax, 9, 72, 23, 'varie', '3 heures : 3 facteurs 2')
text(ax, 44, 8, r'$2\times2\times2=2^{3}=8$', 'resultat', 'l')
save(fig, '14-001')
