import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(85)
R = ['sujet', 'varie', 'resultat']
x0, x1 = 5, 80
f = lambda v: x0 + (v + 6) / 15 * (x1 - x0)
names = ['3ℤ', '1 + 3ℤ', '2 + 3ℤ']
for k in range(3):
    y = 62 - 20 * k
    line(ax, [(4, y), (84, y)], 'fixe', lw=0.6)
    for v in range(-6, 10):
        if v % 3 == k: disc(ax, f(v), y, 1.7, R[k])
        else: disc(ax, f(v), y, 0.5, 'fixe')
    text(ax, 4, y + 5, names[k], R[k], 's', ha='left')
    if k > 0:
        disc(ax, f(0), y, 1.7, 'fixe', fill=False)
        arrow(ax, (f(0) + 1.5, y + 3.5), (f(k) - 1.5, y + 3.5), 'varie')
        text(ax, (f(0) + f(k)) / 2 + 2, y + 6.5, '+%d' % k, 'varie', 's')
y = 62
arrow(ax, (f(-3), y + 2), (f(3), y + 2), 'varie', curve=-0.5)
text(ax, f(0), y + 13, '−3 + 6 = 3 reste dedans', 'resultat', 's')
text(ax, 84, y - 6, 'sous-groupe', 'sujet', 's', ha='right')
text(ax, 84, 14, 'classes latérales', 'varie', 's', ha='right')
save(fig, '47-116')
