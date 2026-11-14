import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
R = ['sujet', 'varie', 'resultat']
x0, x1 = 6, 82
f = lambda v: x0 + (v + 6) / 14 * (x1 - x0)
names = ['3ℤ', '1 + 3ℤ', '2 + 3ℤ']
for k in range(3):
    y = 78 - 15 * k
    line(ax, [(4, y), (84, y)], 'fixe', lw=0.6)
    for v in range(-6, 9):
        if v % 3 == k: disc(ax, f(v), y, 1.7, R[k])
    text(ax, 4, y + 5, names[k], R[k], 's', ha='left')
    if k > 0:
        disc(ax, f(0), y, 1.7, 'fixe', fill=False)
        arrow(ax, (f(0) + 1.5, y + 3.5), (f(k) - 1.5, y + 3.5), 'varie')
        text(ax, (f(0) + f(k)) / 2 + 2, y + 6.5, '+%d' % k, 'varie', 's')
yb = 18
line(ax, [(4, yb), (84, yb)], 'fixe', lw=0.6)
text(ax, 4, yb + 6, 'tous les entiers', 'encre', 's', ha='left')
for v in range(-6, 9):
    disc(ax, f(v), yb, 1.7, R[v % 3])
    if v % 2 == 0: text(ax, f(v), yb - 5, str(v).replace('-', '−'), R[v % 3], 's')
save(fig, '47-114')
