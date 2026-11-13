import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
def row(y, n, title, role):
    text(ax, 44, y + 13, title, role, 's', weight='bold')
    for i in range(8):
        x = 6 + i * 9.5
        if i == 0 and n == 7: box(ax, x, y, 8, 8, 'limite', fill=False, dash=True)
        elif i == 0: box(ax, x, y, 8, 8, 'varie', label='∅', size='s')
        else: box(ax, x, y, 8, 8, 'sujet')
row(56, 7, 'sans le sac vide : 7 sacs', 'limite')
row(36, 8, 'avec le sac vide : 8 sacs', 'resultat')
f = numberline(ax, 14, 50, 24, 0, 3, arrow_right=False)
disc(ax, f(0), 24, 1.6, 'varie')
text(ax, 44, 3.5, 'comme 0, il compte', 'varie', 's', weight='bold') if False else None
text(ax, 70, 24, '0 compte aussi', 'varie', 's')
save(fig, '42-011')
