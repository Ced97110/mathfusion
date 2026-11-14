import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
O = (40, 50); ux, uy = 8, 6
X = lambda a: O[0] + ux * a
Y = lambda b: O[1] + uy * b
arrow(ax, (O[0], Y(-6.6)), (O[0], Y(7.2)), 'fixe', lw=0.7)
line(ax, [(X(-4.6), O[1]), (X(4.4), O[1])], 'limite', dash=True, lw=1.1)
for a in range(-4, 5):
    for b in range(-6, 7):
        if b != 0:
            disc(ax, X(a), Y(b), 0.5, 'fixe')
line(ax, [(X(-3.3), Y(-6.6)), (X(3.3), Y(6.6))], 'sujet', lw=1.0)
for k in (1, 2, 3, -1, -2, -3):
    disc(ax, X(k), Y(2 * k), 1.4, 'sujet')
for k in (1, 2, 3):
    t = text(ax, X(k) + 2.5, Y(2 * k) - 0.8, f'({k}, {2 * k})', 'sujet', 's', ha='left')
    t.set_bbox(dict(fc='white', ec='none', pad=0.8))
text(ax, 43, 93, 'b', 'fixe', 'm')
text(ax, 3.5, O[1] + 3.2, 'a', 'fixe', 'm')
text(ax, 79, O[1] + 3, 'b = 0', 'limite', 's')
text(ax, 79, O[1] - 3, 'vide', 'limite', 's')
save(fig, '54-012')
