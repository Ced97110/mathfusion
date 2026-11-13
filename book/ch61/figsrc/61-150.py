import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
s = 4.5; base = 14
for i in range(6):
    n = i + 1; x = 8 + i * 11
    for k in range(n):
        box(ax, x - s / 2, base + k * s, s, s, 'sujet', r=0.2, lw=0.5)
    text(ax, x, base + n * s + 3, str(n), 'sujet', 's')
    text(ax, x, 8.5, r'$\sqrt[%d]{2}$' % n, 'encre', 's')
arrow(ax, (76, 14), (76, 42), 'varie')
text(ax, 76, 47, 'sans borne', 'varie', 's')
text(ax, 76, 9, 'degrés', 'fixe', 's')
save(fig, '61-150')
