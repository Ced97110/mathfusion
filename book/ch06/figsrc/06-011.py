import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'4 morceaux, on en prend $a$', 'encre')
for y, a in ((34, 1), (20, 2), (6, 3)):
    for j in range(4):
        box(ax, 28 + j * 14, y, 14, 8, 'varie' if j < a else 'fixe', r=0.3)
    text(ax, 14, y + 4, rf'$a={a}$', 'varie')
save(fig, '06-011')
