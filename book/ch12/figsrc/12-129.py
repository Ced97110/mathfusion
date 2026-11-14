import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 76, 24, -4, 4, labels=False)
for v, lab in [(-3, r'$-3$'), (0, r'$O$'), (3, r'$3$')]:
    text(ax, f(v), 24 - 4.2, lab, 'fixe' if v == 0 else 'sujet', 'm')
    disc(ax, f(v), 24, 1.5, 'fixe' if v == 0 else 'sujet')
arrow(ax, (f(0) + 1.8, 31), (f(3), 31), 'varie')
arrow(ax, (f(0) - 1.8, 31), (f(-3), 31), 'varie')
text(ax, (f(0) + f(3)) / 2, 35, '3 unités', 'varie', 's')
text(ax, (f(0) + f(-3)) / 2, 35, '3 unités', 'varie', 's')
brace(ax, f(0), f(1), 17, 'fixe', 'unité')
text(ax, 44, 47, 'distance à $O$', 'encre', 'l')
save(fig, '12-129')
